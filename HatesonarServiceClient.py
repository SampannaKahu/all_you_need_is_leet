#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy

from hatesonar import Sonar


def call_api(service, analyze_request):
    try:
        return service.ping(analyze_request)
    except:
        print('Api error for: ', analyze_request)
        raise ValueError('Error while calling Hatesonar API')


class HatesonarAPIClient:
    def __init__(self):
        self.service = Sonar()

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

    def get_toxicity_for_sentence(self, sentence=None):

        if not sentence or not isinstance(sentence, str) or not sentence.strip():
            raise ValueError('Please pass a valid sentence.')

        response = call_api(self.service, sentence)

        parsed_response = self.parse_hatesonar_response(response)

        return parsed_response[1]

    def parse_hatesonar_response(self, response):
        hate_speech_probability = 0
        offensive_language_probability = 0
        neither_probability = 0

        top_class = response['top_class']
        probabilities = response['classes']
        for probability in probabilities:
            if probability['class_name'] is 'hate_speech':
                hate_speech_probability = probability['confidence']
            elif probability['class_name'] is 'offensive_language':
                offensive_language_probability = probability['confidence']
            elif probability['class_name'] is 'neither':
                neither_probability = probability['confidence']
        return top_class, hate_speech_probability, offensive_language_probability, neither_probability
