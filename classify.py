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
    priorProbs=[]*m
    postProbs=numpy.ndarray((m, numOfAtts), list)
    postProbs[:][:]=[]
    
    ######## get prior probabilities and class counts
    for sample in train:
        priorProbs[classes.index(sample[-1])]+=1
    for c in priorProbs:
        c/=n
    print(priorProbs)
    
    ########get posterior probabilities
    for att in meta.names()[:-1]:
        atts=list(set(train[att]))
        for c in postProbs[:][meta.names().index(att)]:
            c=[]*len(atts)
        for i in range(0,n):
            postProbs[train[att][-1],atts.index(train[att][i])]+=1
        for i in  range(0, postProbs[:][meta.names().index(att)]):
            c/=priorProbs[i]
    print(postProbs)