# -*- coding: utf-8 -*-

originalFile = open("data/NAACL_SRW_2016.txt_toxicity", "r")

scores = []

originalTweets = originalFile.read().splitlines()

for i in range(len(originalTweets)):
    
    oScore = float(originalTweets[i].split(',')[0])
    scores.append(oScore)

import matplotlib.pyplot as plt


def count_range_in_list(li, min):
	ctr = 0
	for x in li:
		if (x > min):
			ctr += 1
	return ctr

import numpy as np
docs = np.arange(0.0, 1.05, 0.05)

counts = []
for v in docs:
    counts.append(count_range_in_list(scores, v))

plt.xticks(docs)
plt.xlabel("Toxicity score threshold")
plt.ylabel("Number of tweets")

plt.plot(docs, counts, marker='o', color='b')
plt.show()