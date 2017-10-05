# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 23:38:34 2017

@author: kyleh
"""

import numpy

def classify(train, test, meta):
    train.sort(order=meta.names()[0])
    
    ########useful variables
    n=len(train)
    classLabel=meta.names()[-1]
    classes=list(set(train[classLabel]))
    numOfAtts=len(meta.names())
    m=len(set(train[classLabel]))
    
    ########create tables to hold probabilities
    priorProbs=[0.]*m
    maxWidth=-1
    for att in meta.names():
        w=len(set(train[att]))
        if w>maxWidth:
            maxWidth=w
    postProbs=numpy.empty((m, numOfAtts-1, maxWidth))
    postProbs[:][:][:]=1.
#    print(postProbs)
    
    ######## get prior probabilities and class counts
    for sample in train:
        priorProbs[classes.index(sample[-1])]+=1
    for i in range(0,len(priorProbs)):
        priorProbs[i]/=n
    print(priorProbs)
    
    ########get posterior probabilities
    for att in meta.names()[:-1]:
        atts=list(set(train[att]))
        for i in range(0,n):
            postProbs[classes.index(train[i][-1]),meta.names().index(att),atts.index(train[att][i])]+=1
        for c in range(0,m):
            for i in range(0,len(atts)):
                postProbs[c][meta.names().index(att),i]/=(priorProbs[c]*n)
    print(postProbs)