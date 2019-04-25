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

    perturbed_filename = "mondal_json_zwsp"
    perturbedFile = open("perturbed_data/" + perturbed_filename)
    perturbedTweets = perturbedFile.read().splitlines()

    oDist = []
    pDist = []
    shifts = 0
    for i in range(len(perturbedTweets)):
        pLineNumber = perturbedTweets[i].split(',')[0]

        oTweet = originalTweets[int(pLineNumber) - 1].split(',')[2:]
        oTweet = ','.join(oTweet)
        oRes = sonar.ping(text=oTweet)
        if oRes['top_class'] is not 'neither':
            oDist.append('Hateful')
        else:
            oDist.append('Not Hateful')

        pTweet = perturbedTweets[i].split(',')[2:]
        pTweet = ','.join(pTweet)
        pRes = sonar.ping(text=pTweet)
        if pRes['top_class'] is not 'neither':
            pDist.append('Hateful')
        else:
            pDist.append('Not Hateful')

        if oRes['top_class'] != 'neither' and pRes['top_class'] == 'neither':
            shifts += 1

    originalDist = sorted(Counter(oDist).items())
    perturbedDist = sorted(Counter(pDist).items())

    print(originalDist)
    print(perturbedDist)
    pShifts = (shifts / len(perturbedTweets)) * 100
    print("Shifts: " + str(pShifts))

    # O1 is not hateful
    o1, o3, p1, p3, oTotal, pTotal = originalDist[1][1], originalDist[0][1], \
                                     perturbedDist[1][1], perturbedDist[0][1], len(
        originalTweets), len(originalTweets)

    A = [(o1 / oTotal) * 100, (o3 / oTotal) * 100]
    B = [(p1 / pTotal) * 100, (p3 / pTotal) * 100]

    N = 2
    ind = np.arange(N)  # the x locations for the groups
    width = 0.27  # the width of the bars
    fig = plt.figure()
    ax = fig.add_subplot(111)

    yvals = A
    rects1 = ax.bar(ind, yvals, width)
    zvals = B
    rects2 = ax.bar(ind + width, zvals, width)
    ax.set_ylabel('Percentage')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('Not Hateful', 'Hateful'))
    ax.legend((rects1[0], rects2[0]), ("Original", "Perturbed"), loc=2)

    ax.set_ylim([0, 100])

    # ax.ylim([0, 100])

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%.1f' % float(h),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    plt.savefig("figures/" + perturbed_filename + "_hatesonar.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    leetSpeak()
