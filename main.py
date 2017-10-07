# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 23:18:25 2017

@author: kyleh
"""

import scipy.io.arff
import numpy
import sys
import preprocess as pp
import partition
import classify
import evaluate

########get data from file
fileName=sys.argv[1]
f=open(fileName, 'r')
data, meta = scipy.io.arff.loadarff(f)

########prepare to partition
d = data.copy()
numpy.random.seed=(80085)
numpy.random.shuffle(d)

########create evaluator
evaluator=evaluate.Evaluator()

########partition, preprocess, and classify
partitions=partition.partition(d)
for i in range(0, len(partitions)):
    print('Fold '+str(i+1))
    test=partitions.pop(0)
    train=numpy.concatenate(partitions).copy()
    #preprocess
#    print('Preprocessing...')
    train=pp.preprocess(train, meta)
    #classify
#    print('Classifying...')
    results=classify.classify(train, test, meta)
    #evaluate
    evaluator.evaluate(test, meta, results)
    partitions.append(test)

print('\n')
print('Average Micro Precision: '+str(evaluator.micP))
print('Average Micro Recall: '+str(evaluator.micR))
print('Average Micro F1: '+str(evaluator.micF))
print('Average Macro Precision: '+str(evaluator.macP))
print('Average Macro Recall: '+str(evaluator.macR))
print('Average Macro F1: '+str(evaluator.macF))
print('Average Accuracy: '+str(evaluator.acc))