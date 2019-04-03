#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:22:27 2019

@author: naman
"""

from argparse import ArgumentParser

from PerspectiveServiceClient import PerspectiveAPIClient

API_KEY='AIzaSyBU2AZtVmel0wV_NMhPTFKmChVHxb6_30Q'

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
service_client = PerspectiveAPIClient(api_key=API_KEY)

for line in lines:
    if(num % 500 == 0):
        print(str(num) + " tweets processed\n")
    num = num + 1
    text = line.split(',')[1]
    analyze_request = {
      'comment': { 'text': text },
      'requestedAttributes': {'TOXICITY': {}}
    }
    
    try:
        response = call_api(analyze_request)
        toxicity = service_client.get_toxicity_for_sentence(sentence=text)
        text_toxicity = str(toxicity) + "," + text
        outputFile.write("%s\n" % text_toxicity)
    except:
        exNum = exNum + 1
        print(str(exNum) + " exception(s) occurred:")
        
inputFile.close()
outputFile.close()