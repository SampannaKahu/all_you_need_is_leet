# -*- coding: utf-8 -*-

def swap(c, i, j):
    c = list(c)
    c[i], c[j] = c[j], c[i]
    return ''.join(c)

def insertTypos(word):
    
    if (len(word) < 4):
        return word
    
    if(len(word) % 2 == 0):
        pos = int(len(word)/2)
        return swap(word, pos, pos-1)
    
    else:
        pos = int(len(word)/2)
        return swap(word, pos-1, pos+1)
        