import csv

path = 'data/'

# input_file_path = 'NLP_CSS_2016.txt'
# output_file_path = 'NLP_CSS_2016.csv'
input_file_path = 'NAACL_SRW_2016.txt'
output_file_path = 'NAACL_SRW_2016.csv'

with open(path + input_file_path) as input_file:
    lines = input_file.readlines()
    with open(path + output_file_path, mode='w') as output_file:
        my_writer = csv.writer(output_file, delimiter=',', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
        my_writer.writerow(['tweets'])
        for line in lines:
            line = line[2:].strip()
            my_writer.writerow([line])
