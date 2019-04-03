# -*- coding: utf-8 -*-

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-o", "--original", dest="original",
                    help="ORIGINAL tweets", metavar="FILE")
parser.add_argument("-p", "--perturbed", dest="perturbed",
                    help="PERTURBED tweets", metavar="FILE")

args = parser.parse_args()


originalFile = open(args.original, "r")
perturbedFile = open(args.perturbed, "r")

originalTweets = originalFile.read().splitlines()
perturbedTweets = perturbedFile.read().splitlines()

if(len(originalTweets) != len(perturbedTweets)):
    raise Exception('Files must have same number of tweets!')

totalOrginalScore = 0
totalPerturbedScore = 0

for i in range(len(originalTweets)):
    
    oScore = originalTweets[i].split(',')[0]
    pScore = perturbedTweets[i].split(',')[0]
    
    totalOrginalScore += float(oScore)
    totalPerturbedScore += float(pScore)

print("Average original toxicity score: {}\n".format(totalOrginalScore/len(originalTweets)))
print("Average perturbed toxicity score: {}\n".format(totalPerturbedScore/len(originalTweets)))

print("Average change in toxicity score: {}\n".format((totalOrginalScore - totalPerturbedScore)/len(originalTweets)))



    