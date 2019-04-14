# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import os
import evaluation

def dataDistribution():
    originalFile = open("data/mondal_json_v2", "r")

    scores = []
    
    originalTweets = originalFile.read().splitlines()
    
    for i in range(len(originalTweets)):
        
        oScore = float(originalTweets[i].split(',')[1])
        scores.append(oScore)
    
    def count_range_in_list(li, min):
    	ctr = 0
    	for x in li:
    		if (x > min):
    			ctr += 1
    	return ctr
    
   
    docs = np.arange(0.0, 1.05, 0.1)
    
    counts = []
    for v in docs:
        counts.append(count_range_in_list(scores, v))
    
    plt.xticks(docs)
    plt.xlabel("Toxicity score threshold")
    plt.ylabel("Number of tweets")
    
    plt.plot(docs, counts, marker='o', color='b')
    plt.show()
    
def parameterVis():
    originalFile = "mondal_json_v2"
    scores = []
    for i in range(1,9):
        pFile = "mondal_json_" + str(i) + "c_leetspeak_toxicity"
        scores.append(evaluation.evaluation(originalFile, pFile))
    print(scores)
    docs = np.arange(1, 9, 1)
    plt.xticks(docs)
    plt.xlabel("Number of characters changed")
    plt.ylabel("Mean decrease in toxicity score")
    plt.plot(docs, scores, marker='o', color='b')
    plt.show()
    
    
    
