#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:22:27 2019

@author: naman
"""

from argparse import ArgumentParser
from googleapiclient import discovery
from ratelimit import limits, sleep_and_retry
import json

API_KEY='AIzaSyBU2AZtVmel0wV_NMhPTFKmChVHxb6_30Q'

# Generates API client object dynamically based on service name and version.
service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

parser = ArgumentParser()
parser.add_argument("-i", "--input", dest="input",
                    help="FILE to read", metavar="FILE")

args = parser.parse_args()

@sleep_and_retry
@limits(calls=6, period=1)
def call_api(analyze_request):
    return service.comments().analyze(body=analyze_request).execute()

# Open a file
inputFile = open(args.input, "r")
outputFileName = args.input + "_toxicity"
outputFile = open(outputFileName, 'w')

lines = inputFile.read().splitlines()

for line in lines:
    text = line.split(',')[1]
    analyze_request = {
      'comment': { 'text': text },
      'requestedAttributes': {'TOXICITY': {}}
    }
    
    response = call_api(analyze_request)
    toxicity = response['attributeScores']['TOXICITY']['summaryScore']['value']
    text_toxicity = str(toxicity) + "," + text
    outputFile.write("%s\n" % text_toxicity)
    
inputFile.close()
outputFile.close()