import json

with open('/home/sampanna/Study/SA/tweetf0rm/data/NLP+CSS_2016/20190326.json') as input_file_pointer:
    with open('./data/NLP_CSS_2016.txt', mode='w') as output_file_pointer:
        line = input_file_pointer.readline()
        while line:
            tweet = json.loads(line.strip())
            output_file_pointer.write('0,' + tweet['full_text'].replace('\n', ' ') + '\n')
            line = input_file_pointer.readline()
