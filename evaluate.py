# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:50:38 2017

@author: kyleh
"""

def evaluate(test, results):
    classes=list(set(test[:][-1]))
    correct=0
    incorrect=0
    for i in range(0,len(results)):
        if results[i]==classes.index(test[i][-1]):
            correct+=1
        else:
            incorrect+=1
            
    print(correct/(correct+incorrect))