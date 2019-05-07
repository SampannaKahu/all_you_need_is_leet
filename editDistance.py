#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:21:21 2019

@author: naman
"""

# A Dynamic Programming based Python program for edit 
# distance problem 
def editDistDP(str1, str2, m, n): 
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m+1): 
        for j in range(n+1): 
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n] 

  
# Driver program to test the above function 
def calculateEditDist():
    
    outputFile = open("editDistanceResults", 'w')

    fileList = ["mondal_json_leetspeak_3w_toxicity", "mondal_json_nows_toxicity", "mondal_json_typos_toxicity", "mondal_json_underscores_toxicity", "mondal_json_zwsp_toxicity"]
    for fileName in fileList:
        originalFile = open("data/" + "mondal_json_v2")
        perturbedFile = open("perturbed_data/" + fileName)
        
        originalTweets = originalFile.read().splitlines()
        perturbedTweets = perturbedFile.read().splitlines()
        
        eDistAll = 0
        avgDistAll = 0
        line = 0
        for i in range(len(perturbedTweets)):
            line += 1
            pLineNumber = perturbedTweets[i].split(',')[0]
            pTweet = perturbedTweets[i].split(',')[2:]
            pTweet = ','.join(pTweet)
            
            oTweet = originalTweets[int(pLineNumber) - 1].split(',')[2:]
            oTweet = ','.join(oTweet)
            
            eDist = (editDistDP(pTweet, oTweet, len(pTweet), len(oTweet)))
            avgDist = eDist/len(oTweet)
            
            eDistAll += eDist
            avgDistAll += avgDist
            if(line % 1000 == 0):
                print(str(line) + " done")
        print(fileName)
        print(eDistAll/len(perturbedTweets))
        print(avgDistAll/len(perturbedTweets))
        outputFile.write("%s\n" % fileName)
        outputFile.write("%s\n" % str(eDistAll/len(perturbedTweets)))
        outputFile.write("%s\n" % str(avgDistAll/len(perturbedTweets)))
        