#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json

from nltk.tokenize import TweetTokenizer

from PerspectiveServiceClient import PerspectiveAPIClient

API_KEY = 'AIzaSyBG_1zyVQwCKnqFoPyz7IjAKCS0xu_KXG0'

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


with open('data/NAACL_SRW_2016.txt_toxicity_2') as input_file:
    with open('data/NAACL_SRV_2016_word_level_toxicities_v2_2.csv', mode='w') as output_file:
        output_fieldnames = ['tweets', 'word_level_score_dict']
        writer = csv.DictWriter(output_file, fieldnames=output_fieldnames)
        writer.writeheader()
        tweet = input_file.readline()
        while tweet:
            original_toxicity = float(tweet.split(',')[0])
            tweet = ','.join(tweet.split(',')[1:])
            words = tknzr.tokenize(tweet)
            try:
                writer.writerow({
                    'tweets': tweet,
                    'word_level_score_dict': json.dumps(
                        service_client.get_toxicity_of_words_v2(list_of_words=words,
                                                                original_toxicity=original_toxicity))
                })
            except ValueError:
                print('Error for tweet: ', tweet)
            tweet = input_file.readline()
            print('Processing...')
