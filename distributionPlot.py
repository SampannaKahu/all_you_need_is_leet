# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import os
import evaluation
import pandas as pd


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
    
   
    docs = np.arange(0.0, 1.05, 0.05)
    
    counts = []
    for v in docs:
        counts.append(count_range_in_list(scores, v))
    
    plt.xticks(docs)
    plt.xlabel("Toxicity score threshold")
    plt.ylabel("Number of tweets")
    
    plt.plot(docs, counts, marker='o', color='b')
    plt.savefig("figures/data_toxicity_dist.png", dpi=300)
    plt.show()
    
def parameterVis():
    originalFile = "mondal_json_v2"
    scores = []
    for i in range(1,5):
        pFile = "mondal_json_leetspeak_" + str(i) +"w_toxicity"
        scores.append(evaluation.evaluation(originalFile, pFile))
    print(scores)
    docs = np.arange(1, 5, 1)
    plt.xticks(docs)
    plt.xlabel("Number of words changed")
    plt.ylabel("Mean decrease in toxicity score")
    plt.plot(docs, scores, marker='o', color='b')
    plt.savefig("figures/leetspeak_w_plot", dpi=300)
    plt.show()
    
    
def bucketVis(filename):
    o1, o2, o3, p1, p2, p3, oTotal, pTotal = evaluation.bucketDistribution("mondal_json_v2", "mondal_json_leetspeak_3w_zws_toxicity")
    
    
    A = [(o1/oTotal)*100, (o2/oTotal)*100, (o3/oTotal)*100]
    B = [(p1/pTotal)*100, (p2/pTotal)*100, (p3/pTotal)*100]
    
    N = 3
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27       # the width of the barsmondal_json_zwsp_toxicity
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    yvals = A
    rects1 = ax.bar(ind, yvals, width)
    zvals = B
    rects2 = ax.bar(ind+width, zvals, width)
    ax.set_ylabel('Percentage')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('Non Toxic','Maybe Toxic','Toxic') )
    ax.legend( (rects1[0], rects2[0]), ("Original", "Perturbed"),loc=2 )
    
    ax.set_ylim([0,100])
    #ax.ylim([0, 100])
    
    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%.1f'%float(h),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)   
    plt.savefig("figures/" + filename, dpi=300)
    plt.show()
    
def initialBucketVis():
    o1, o2, o3, oTotal = evaluation.initialDataBucketDistribution("mondal_json_v2")
    
    
    A = [(o1/oTotal)*100, (o2/oTotal)*100, (o3/oTotal)*100]
    
    N = 3
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27       # the width of the bars
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    yvals = A
    rects1 = ax.bar(ind, yvals, width)
    
    ax.set_ylabel('Percentage')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('Non Toxic','Maybe Toxic','Toxic') )
    ax.legend( (rects1[0]), ("Original") )
    ax.set_ylim([0,100])
    #ax.ylim([0, 100])
    
    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%.1f'%float(h),
                    ha='center', va='bottom')

    autolabel(rects1)
    plt.savefig("figures/originialBuckets.png", dpi=300)
    plt.show()

    
    
