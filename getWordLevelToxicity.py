#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json

from nltk.tokenize import TweetTokenizer

from PerspectiveServiceClient import PerspectiveAPIClient

API_KEY = 'AIzaSyBU2AZtVmel0wV_NMhPTFKmChVHxb6_30Q'

# Initialize the service client
service_client = PerspectiveAPIClient(api_key=API_KEY, cache_file='cache/word_toxicity_scores_v2.json')
# Initialize tokenizer.
tknzr = TweetTokenizer(preserve_case=False, reduce_len=False, strip_handles=False)


def get_word_toxicities(sentence):
    # words = sentence.split(' ')
    words = tknzr.tokenize(sentence)
    chunks = [words[x:x + 9] for x in range(0, len(words), 9)]
    my_dict = {}
    for chunk in chunks:
        my_dict = {**my_dict, **service_client.get_toxicity_of_words(chunk)}
    return my_dict

i = 0
with open('data/mondal_json_toxicity') as input_file:
    with open('data/mondal_json_toxicity.csv', mode='w') as output_file:
        output_fieldnames = ['tweets', 'word_level_score_dict', 'score']
        writer = csv.DictWriter(output_file, fieldnames=output_fieldnames)
        writer.writeheader()
        tweet = input_file.readline()
        while tweet:
            i += 1
            if (i % 500 == 0):
                print(str(i) + " processed")
            original_toxicity = float(tweet.split(',')[1])
            tweet = ','.join(tweet.split(',')[2:])
            words = tknzr.tokenize(tweet)
            try:
                writer.writerow({
                    'tweets': tweet,
                    'word_level_score_dict': json.dumps(
                        service_client.get_toxicity_of_words_v2(list_of_words=words,
                                                                original_toxicity=original_toxicity)),
                            'score': original_toxicity
                })
            except ValueError:
                print('Error for tweet: ', tweet)
            tweet = input_file.readline()
            #print('Processing...')
