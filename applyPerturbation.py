import csv
import json
import operator

import leetSpeak


def find_most_toxic_word(my_dict):
    return max(my_dict.items(), key=operator.itemgetter(1))[0]


with open('data/NAACL_SRW_2016_word_level_toxicities_v2.csv') as input_file:
    with open('perturbed_data/NAACL_SRW_2016_leetspeak', mode='w') as output_file:
        reader = csv.reader(input_file, delimiter=',')
        for row in reader:
            tweet = row[0]
            toxicity_dict = json.loads(row[1])
            most_toxic_word = find_most_toxic_word(toxicity_dict)
            perturbed_word = leetSpeak.word2Leet(most_toxic_word, len(most_toxic_word))
            # TODO: Check whether this ig a replaceAll or just a single replace.
            perturbed_tweet = tweet.replace(most_toxic_word, perturbed_word)
            output_file.write('0,' + perturbed_tweet + '\n')
