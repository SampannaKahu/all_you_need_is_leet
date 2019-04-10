import csv
import json
import operator

import leetSpeak
import Typo


def find_most_toxic_words(my_dict):
    sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)
    return [sorted_dict[0][0], sorted_dict[1][0], sorted_dict[2][0]]


def insertLeetSpeak():
    count = 0
    i = 1
    with open('data/mondal_json_toxicity.csv') as input_file:
        with open('perturbed_data/mondal_json_leetspeak_3w', mode='w') as output_file:
            reader = csv.reader(input_file, delimiter=',')
            for row in reader:
                count += 1
                if(count % 1000 == 0):
                    print (str(count) + " done")
                tweet = row[0]
                toxicity_dict = json.loads(row[1])
                most_toxic_words = find_most_toxic_words(toxicity_dict)
                perturbed_tweet = tweet
                for word in most_toxic_words:
                    perturbed_word = leetSpeak.word2Leet(word, len(word))
                # TODO: Check whether this ig a replaceAll or just a single replace.
                    perturbed_tweet = perturbed_tweet.replace(word, perturbed_word)
                output_file.write(str(i) + ',0,' + perturbed_tweet)
                i += 1

def insertTypos():
    count = 0
    i = 1
    countSame = 0
    with open('data/mondal_json_toxicity.csv') as input_file:
        with open('perturbed_data/mondal_json_typos', mode='w') as output_file:
            reader = csv.reader(input_file, delimiter=',')
            for row in reader:
                count += 1
                if(count % 1000 == 0):
                    print (str(count) + " done")
                tweet = row[0]
                toxicity_dict = json.loads(row[1])
                most_toxic_words = find_most_toxic_words(toxicity_dict)
                perturbed_tweet = tweet
                for word in most_toxic_words:
                    perturbed_word = Typo.insertTypos(word)
                # TODO: Check whether this ig a replaceAll or just a single replace.
                    perturbed_tweet = perturbed_tweet.replace(word, perturbed_word)
                if(perturbed_tweet == tweet):
                        countSame += 1
                        print(str(countSame) + " " + tweet + " unchanged")
                output_file.write(str(i) + ',0,' + perturbed_tweet)
                i += 1
