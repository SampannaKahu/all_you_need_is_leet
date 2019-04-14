import csv
import json
import operator

from nltk.tokenize import TweetTokenizer

import Typo
import leetSpeak

# Initialize tokenizer.
tknzr = TweetTokenizer(preserve_case=False, reduce_len=False, strip_handles=False)


def find_most_toxic_words(my_dict):
    sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)
    return [sorted_dict[0][0], sorted_dict[1][0]]


def replace_word(original_sentence, original_word, new_word):
    perturbed_tweet = original_sentence
    index = perturbed_tweet.lower().find(original_word.lower())
    end = index + len(original_word.lower())
    perturbed_word = new_word
    return perturbed_tweet[:index] + perturbed_word + perturbed_tweet[end:]


def insertLeetSpeak():
    count = 0
    i = 1
    with open('data/mondal_json_toxicity.csv') as input_file:
        with open('perturbed_data/mondal_json_6c_leetspeak', mode='w') as output_file:
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
                    perturbed_word = leetSpeak.word2Leet(word, 6)
                    perturbed_tweet = replace_word(tweet, word, perturbed_word)
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
                    perturbed_tweet = replace_word(perturbed_tweet, word, perturbed_word)
                if(perturbed_tweet == tweet):
                        countSame += 1
                        print(str(countSame) + " " + tweet + " unchanged")
                output_file.write(str(i) + ',0,' + perturbed_tweet)
                i += 1


def insertUnderscore():
    count = 0
    i = 1
    with open('data/mondal_json_toxicity.csv') as input_file:
        with open('perturbed_data/mondal_json_underscores', mode='w') as output_file:
            reader = csv.reader(input_file, delimiter=',')
            for row in reader:
                count += 1
                if count % 1000 == 0:
                    print(str(count) + " done")
                tweet = row[0]
                perturbed_tweet = tweet.replace(' ', '_')
                output_file.write(str(i) + ',0,' + perturbed_tweet)
                i += 1


def insertZwsp():
    count = 0
    i = 1
    countSame = 0
    with open('data/mondal_json_toxicity.csv') as input_file:
        with open('perturbed_data/mondal_json_zwsp', mode='w') as output_file:
            reader = csv.reader(input_file, delimiter=',')
            for row in reader:
                count += 1
                if count % 1000 == 0:
                    print(str(count) + " done")
                tweet = row[0]
                toxicity_dict = json.loads(row[1])
                most_toxic_words = find_most_toxic_words(toxicity_dict)
                perturbed_tweet = tweet
                for word in most_toxic_words:
                    perturbed_word = "".join([c + 5 * u'\u200b' for c in word])
                    perturbed_tweet = replace_word(perturbed_tweet, word, perturbed_word)
                if (perturbed_tweet == tweet):
                    countSame += 1
                    print(str(countSame) + " " + tweet + " unchanged")
                output_file.write(str(i) + ',0,' + perturbed_tweet + '\n')
                i += 1


if __name__ == "__main__":
    pass
    # Call the function that you want to run here.
    # insertZwsp()
