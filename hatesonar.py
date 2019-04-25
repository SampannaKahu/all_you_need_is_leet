#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:59:32 2019

@author: naman
"""
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from hatesonar import Sonar
sonar = Sonar()

def leetSpeak():
    originalFile = open("data/" + "mondal_json_v2")
    originalTweets = originalFile.read().splitlines()
    
    oDist = []
    pDist = []
    shifts = 0
    for i in range(len(originalTweets)):
        oTweet = originalTweets[i].split(',')[2]
        oRes = sonar.ping(text=oTweet)
        oDist.append(oRes['top_class'])
        
        pTweet = oTweet.replace(" ","")
        pRes = sonar.ping(text=pTweet)
        pDist.append(pRes['top_class'])
        
        if(oRes['top_class'] == 'hate_speech' and pRes['top_class'] != 'hate_speech'):
            shifts += 1
        
    originalDist = sorted(Counter(oDist).items())
    perturbedDist = sorted(Counter(pDist).items())
    
    print(originalDist)
    print(perturbedDist)
    pShifts = (shifts/len(originalTweets)) * 100 
    print("Shifts: " + str(pShifts))
    
    o1, o2, o3, p1, p2, p3, oTotal, pTotal = originalDist[1][1], originalDist[2][1], originalDist[0][1], perturbedDist[1][1], perturbedDist[2][1], perturbedDist[0][1], len(originalTweets), len(originalTweets)
    
    A = [(o1/oTotal)*100, (o2/oTotal)*100, (o3/oTotal)*100]
    B = [(p1/pTotal)*100, (p2/pTotal)*100, (p3/pTotal)*100]
    
    N = 3
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27       # the width of the bars
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    yvals = A
    rects1 = ax.bar(ind, yvals, width)
    zvals = B
    rects2 = ax.bar(ind+width, zvals, width)
    ax.set_ylabel('Percentage')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('Neither','Offensive','Hate') )
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
    plt.savefig("figures/" + "hatesonar_leet.png", dpi=300)
    plt.show()
        

        
        