# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:50:38 2017

@author: kyleh
"""

class Evaluator:
    
    def __init__(self):
        self.ttp=0
        self.ttn=0
        self.tfp=0
        self.tfn=0
    
    def evaluate(self, test, meta, results):
        classes=list(set(test[meta.names()[-1]]))
    #    print(classes)
    
        #assuming class 0 is Negative
        tp=0
        tn=0
        fp=0
        fn=0
        for i in range(0, len(results)):
            if results[i]==0:
                if classes.index(test[i][-1])==0:
                    tn+=1
                else:
                    fn+=1
            else:
                if classes.index(test[i][-1])==0:
                    fp+=1
                else:
                    tp+=1
    
        self.ttp+=tp
        self.ttn+=tn
        self.tfp+=fp
        self.tfn+=fn
        print('True Positives: '+str(tp))
        print('False positives: '+str(fp))
        print('True Negatives: '+str(tn))
        print('False Negatives: '+str(fn))