# -*- coding: utf-8 -*-

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-o", "--original", dest="original",
                    help="ORIGINAL tweets", metavar="FILE")
parser.add_argument("-p", "--perturbed", dest="perturbed",
                    help="PERTURBED tweets", metavar="FILE")

args = parser.parse_args()

def evaluation(originalFile, perturbedFile):
    originalFile = open("data/" + originalFile)
    perturbedFile = open("perturbed_data/" + perturbedFile)
    
    originalTweets = originalFile.read().splitlines()
    perturbedTweets = perturbedFile.read().splitlines()
    
    
    totalOrginalScore = 0
    totalPerturbedScore = 0
    
    totalEvals = 0
    
    for i in range(len(perturbedTweets)):
        
        pLineNumber = perturbedTweets[i].split(',')[0]
    
        oScore = originalTweets[int(pLineNumber) - 1].split(',')[1]
    #    if(float(oScore) < 0.5):
    #        continue
        pScore = perturbedTweets[i].split(',')[1]
        
        totalEvals += 1
        
        totalOrginalScore += float(oScore)
        totalPerturbedScore += float(pScore)
    
    
    print("Total Evaluations: {}\n".format(totalEvals))
    
    print("Average original toxicity score: {}\n".format(totalOrginalScore/totalEvals))
    print("Average perturbed toxicity score: {}\n".format(totalPerturbedScore/totalEvals))
    
    print("Average change in toxicity score: {}\n".format((totalOrginalScore - totalPerturbedScore)/totalEvals))
    
    return (totalOrginalScore - totalPerturbedScore)/totalEvals
    
    
    
        