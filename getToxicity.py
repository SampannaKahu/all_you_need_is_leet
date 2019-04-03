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

# Initialize the service client
service_client = PerspectiveAPIClient(api_key=API_KEY)

for line in lines:
    text = line.split(',')[1]
    toxicity = service_client.get_toxicity_for_sentence(sentence=text)
    text_toxicity = str(toxicity) + "," + text
    outputFile.write("%s\n" % text_toxicity)
    
inputFile.close()
outputFile.close()