# -*- coding: utf-8 -*-

import csv
import json
import operator

import leetSpeak


def find_most_toxic_word(my_dict):
    return max(my_dict.items(), key=operator.itemgetter(1))[0]


count = 0
i = 1
with open('data/mondal_json_toxicity.csv') as input_file:
    with open('data/mondal_json_v2', mode='w') as output_file:
        reader = csv.reader(input_file, delimiter=',')
        for row in reader:
            count += 1
            if(count % 1000 == 0):
                print (str(count) + " done")
            tweet = row[0]
            toxicity_dict = json.loads(row[1])
            most_toxic_word = find_most_toxic_word(toxicity_dict)
            perturbed_word = most_toxic_word
            # TODO: Check whether this ig a replaceAll or just a single replace.
            perturbed_tweet = tweet.replace(most_toxic_word, perturbed_word)
            output_file.write(str(i) + ',' + row[2] + ',' + perturbed_tweet)
            i += 1
