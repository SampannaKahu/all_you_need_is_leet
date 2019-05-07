#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:22:27 2019

@author: naman
"""

from argparse import ArgumentParser
import CredentialManager

from PerspectiveServiceClient import PerspectiveAPIClient
from HatesonarServiceClient import HatesonarAPIClient

API_KEY = CredentialManager.get_my_api_key()

parser = ArgumentParser()
parser.add_argument("-i", "--input", dest="input",
                    help="FILE to read", metavar="FILE")

args = parser.parse_args()

# Open a file
inputFile = open(args.input, "r")
outputFileName = args.input + "_toxicity"
outputFile = open(outputFileName, 'w')

lines = inputFile.read().splitlines()
num = 1
exNum = 0
# Initialize the service client
service_client = PerspectiveAPIClient(api_key=API_KEY, cache_file="cache/word_toxicity_scores_v2.json")
#service_client =  HatesonarAPIClient()
print("Using API Key: " + API_KEY)
for line in lines:
    if(num % 500 == 0):
        print(str(num) + " tweets processed\n")
    num = num + 1
    text = ",".join(line.split(',')[2:])
    lineNum = line.split(',')[0]
    
    try:
        toxicity = service_client.get_toxicity_for_sentence(sentence=text)
        text_toxicity = str(lineNum) + "," + str(toxicity) + "," + text
        outputFile.write("%s\n" % text_toxicity)
    except:
        exNum = exNum + 1
        print(str(exNum) + " exception(s) occurred:")
        
inputFile.close()
outputFile.close()