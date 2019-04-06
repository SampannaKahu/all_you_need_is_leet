#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import atexit
import json
import copy

from googleapiclient import discovery
from googleapiclient.errors import HttpError
from ratelimit import limits, sleep_and_retry


@sleep_and_retry
@limits(calls=8, period=1)
def call_api(service, analyze_request):
    try:
        return service.comments().analyze(body=analyze_request).execute()
    except HttpError:
        print('Api error for: ', analyze_request)
        raise ValueError('Error while calling Perspective API')


class PerspectiveAPIClient:
    def __init__(self, api_key=None, cache_file=None):
        self.cache_file = cache_file
        self.service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=api_key)

        with open(cache_file) as my_file:
            contents = my_file.read()
            self.word_toxicity_cache = json.loads(contents)
        atexit.register(self.cleanup)

    def get_toxicity_of_words_v2(self, list_of_words=None, original_toxicity=0):
        # Some sanity checks.
        if not list_of_words or not isinstance(list_of_words, list) or len(list_of_words) == 0:
            raise ValueError('Please pass a valid list of words.')

        stripped_words = [x.strip().strip('.').lower() for x in list_of_words if x.strip().strip('.').lower()]

        my_dict = {}
        for idx, word in enumerate(stripped_words):
            stripped_words_copy = copy.deepcopy(stripped_words)
            del stripped_words_copy[idx]
            my_dict[word] = original_toxicity - self.get_toxicity_for_sentence(sentence=' '.join(stripped_words_copy))

        return my_dict

    def get_toxicity_of_words(self, list_of_words=None):
        """
        Gets word-level toxicity using Perspective API.
        :param list_of_words: List of str with the input words. Any empty strings or Nones will be ignored. Length should be less than 10.
        :return: Dict of the lower-cased original words as keys and the respective toxicity scores as values.
        """

        # Some sanity checks.
        if not list_of_words or not isinstance(list_of_words, list) or len(list_of_words) == 0:
            raise ValueError('Please pass a valid list of words.')

        # De-duplicate
        list_of_words = list(set(list_of_words))

        # Some pre-processing
        stripped_words = [x.strip().strip('.').lower() for x in list_of_words if x.strip().strip('.').lower()]

        if len(stripped_words) > 10:
            raise ValueError('Perspective API does not support text with more then 10 sentences.')

        # Search for words in cache.
        cache_toxicities = {word: float(self.word_toxicity_cache[word]) for word in stripped_words if
                            word in self.word_toxicity_cache}

        # remove words found in cache.
        for found_word in cache_toxicities.keys():
            stripped_words.remove(found_word)

        # Capitalize before sending to Perspective API.
        capitalized_list_of_words = [x.capitalize() for x in stripped_words if x]

        if not capitalized_list_of_words:
            return cache_toxicities

        capitalized_sentence = '. '.join(capitalized_list_of_words)

        analyze_request = {
            'comment': {'text': capitalized_sentence},
            'requestedAttributes': {'TOXICITY': {}},
            'spanAnnotations': True
        }

        response = call_api(self.service, analyze_request)

        try:
            span_scores = response['attributeScores']['TOXICITY']['spanScores']
        except TypeError:
            print('Type error encountered. Response:', response)
            return {}

        # Dict comprehension
        response_toxicities = {capitalized_sentence[span_score['begin']: span_score['end']].strip().strip('.').lower():
                                   span_score['score']['value'] for span_score in span_scores}

        # Update the local cache. (Clean-up function will persist it to the file.)
        self.word_toxicity_cache = {**self.word_toxicity_cache, **response_toxicities}

        # Return toxicity dict
        return {**cache_toxicities, **response_toxicities}

    def get_toxicity_for_sentence(self, sentence=None):
        """
        Get the toxicity for the entire passed 'sentence'. 'sentence' can even be multiple sentences.
        :param sentence: Input str. Can be multiple sentences, but only one toxicity score will be returned.
        :return: An int representing the toxicity score.
        """

        if not sentence or not isinstance(sentence, str) or not sentence.strip():
            raise ValueError('Please pass a valid sentence.')

        analyze_request = {
            'comment': {'text': sentence},
            'requestedAttributes': {'TOXICITY': {}},
            'spanAnnotations': False
        }

        response = call_api(self.service, analyze_request)

        toxicity_score = response['attributeScores']['TOXICITY']['summaryScore']['value']

        return toxicity_score

    def cleanup(self):
        """
        Clean-up function. Persists the toxicity_cache map back into the file for future use.
        """

        print('Attempting safe shutdown of PerspectiveServiceClient...')
        with open(self.cache_file, mode='w') as cache_file_path:
            cache_file_path.write(json.dumps(self.word_toxicity_cache))
        print('PerspectiveServiceClient successfully closed.')
