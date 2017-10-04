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

########get data from file
fileName=sys.argv[1]
f=open(fileName, 'r')
data, meta = scipy.io.arff.loadarff(f)

########prepare to partition
d = data.copy()
numpy.random.shuffle(d)

########partition, preprocess, and classify
partitions=partition.partition(d)
for i in range(0, len(partitions)):
    test=partitions.pop(i)
    numpy.concatenate(partitions)
    #classify
    #evaluate
    partitions.append(test)