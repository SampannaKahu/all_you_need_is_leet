#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json

from nltk.tokenize import TweetTokenizer

from PerspectiveServiceClient import PerspectiveAPIClient

API_KEY = 'AIzaSyBG_1zyVQwCKnqFoPyz7IjAKCS0xu_KXG0'

# Initialize the service client
service_client = PerspectiveAPIClient(api_key=API_KEY, cache_file='cache/word_toxicity_scores.ini')

tknzr = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)


# scores1 = service_client.get_toxicity_of_words('Hello world.'.split(' '))
# print(scores1)
#
# scores2 = service_client.get_toxicity_of_words('Hello dear world.'.split(' '))
# print(scores2)
#
# score = service_client.get_toxicity_for_sentence('Hello world.')
# print(score)

def get_word_toxicities(sentence):
    # words = sentence.split(' ')
    words = tknzr.tokenize(sentence)
    chunks = [words[x:x + 9] for x in range(0, len(words), 9)]
    my_dict = {}
    for chunk in chunks:
        my_dict = {**my_dict, **service_client.get_toxicity_of_words(chunk)}
    return my_dict


with open('data/NLP_CSS_2016.csv') as input_file:
    with open('data/NLP_CSS_2016_word_level_toxicities_v2.csv', mode='w') as output_file:
        output_fieldnames = ['tweets', 'word_level_score_dict']
        writer = csv.DictWriter(output_file, fieldnames=output_fieldnames)
        writer.writeheader()
        csv_reader = csv.DictReader(input_file, fieldnames=['tweets'])
        for row in csv_reader:
            print('Processing...')
            try:
                tweet = row['tweets']
                writer.writerow({
                    'tweets': tweet,
                    'word_level_score_dict': json.dumps(get_word_toxicities(tweet))
                })
            except ValueError:
                pass
