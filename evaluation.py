# -*- coding: utf-8 -*-

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-o", "--original", dest="original",
                    help="ORIGINAL tweets", metavar="FILE")
parser.add_argument("-p", "--perturbed", dest="perturbed",
                    help="PERTURBED tweets", metavar="FILE")

args = parser.parse_args()

#evaluation("mondal_json_v2", "mondal_json_nows_toxicity")
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

def getEval():
    perturbedFile1 = open("perturbed_data/" + "mondal_json_4c_leetspeak_toxicity")
    perturbedFile2 = open("perturbed_data/" + "mondal_json_5c_leetspeak_toxicity")
    outputFile = open("perturbed_data/" + "dummy", 'w')

    
    
    p1Tweets = perturbedFile1.read().splitlines()
    p2Tweets = perturbedFile2.read().splitlines()
    
    for i in range(len(p1Tweets)):
        
        p1LineNumber = p1Tweets[i].split(',')[0]
        p1Score = p1Tweets[i].split(',')[1]
        
        p2Score = p2Tweets[int(p1LineNumber) - 1].split(',')[1]
    #    if(float(oScore) < 0.5):
    #        continue
        if(p1Score < p2Score):
            outputFile.write("%s," % p1Score)
            outputFile.write("%s\n" % p1Tweets[i].split(',')[2])
            outputFile.write("%s," % p2Score)
            outputFile.write("%s\n" % p2Tweets[int(p1LineNumber) - 1].split(',')[2])
            outputFile.write("\n")


def bucketDistribution(originalFile, perturbedFile):
    originalFile = open("data/" + originalFile)
    perturbedFile = open("perturbed_data/" + perturbedFile)
    
    originalTweets = originalFile.read().splitlines()
    perturbedTweets = perturbedFile.read().splitlines()
    
    
    o1 = o2 = o3 = p1 =  p2 = p3 = 0
    oTotal = len(originalTweets)
    pTotal = len(perturbedTweets)
    
    for i in range(len(originalTweets)):
        
        oScore = originalTweets[i].split(',')[1]
        
        if (float(oScore) < 0.33):
            o1 += 1
        elif(float(oScore) < 0.66):
            o2 += 1
        else:
            o3 += 1
            
    for i in range(len(perturbedTweets)):
        
        pScore = perturbedTweets[i].split(',')[1]
        
        if (float(pScore) < 0.33):
            p1 += 1
        elif(float(pScore) < 0.66):
            p2 += 1
        else:
            p3 += 1
    
    
    return o1, o2, o3, p1, p2, p3, oTotal, pTotal

def initialDataBucketDistribution(originalFile):
    originalFile = open("data/" + originalFile)
    
    originalTweets = originalFile.read().splitlines()
    
    
    o1 = o2 = o3 = 0
    oTotal = len(originalTweets)
    
    for i in range(len(originalTweets)):
        
        oScore = originalTweets[i].split(',')[1]
        
        if (float(oScore) < 0.33):
            o1 += 1
        elif(float(oScore) < 0.66):
            o2 += 1
        else:
            o3 += 1
    
    return o1, o2, o3,oTotal
    
def bucketShift(originalFile, perturbedFile):
    originalFile = open("data/" + originalFile)
    perturbedFile = open("perturbed_data/" + perturbedFile)
    
    originalTweets = originalFile.read().splitlines()
    perturbedTweets = perturbedFile.read().splitlines()
    
    totalShifts = 0
    
    for i in range(len(perturbedTweets)):
        
        pLineNumber = perturbedTweets[i].split(',')[0]
    
        oScore = originalTweets[int(pLineNumber) - 1].split(',')[1]
        pScore = perturbedTweets[i].split(',')[1]
        
        if(float(oScore) > 0.66 and float(pScore) <= 0.66):
            totalShifts += 1

    print("Percentage Shifts from Bucket 3: {}\n".format((totalShifts/ len(perturbedTweets)*100)))
        
        
        