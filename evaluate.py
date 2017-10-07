# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:50:38 2017

@author: kyleh
"""

class Evaluator:
    
    def __init__(self):
        self.macP=0.
        self.macR=0.
        self.macF=0.
        self.micP=0.
        self.micR=0.
        self.micF=0.
    
    def evaluate(self, test, meta, results):
        classes=list(set(test[meta.names()[-1]]))
    #    print(classes)
    
        #assuming class 0 is Negative
        tp=0.
        tn=0.
        fp=0.
        fn=0.
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
    
        acc=(tp+tn)/(tp+tn+fp+fn)
        precA=tp/(tp+fp)
        precB=tn/(tn+fn)
        recA=tp/(tp+fn)
        recB=tn/(tn+fp)
        f1A=(2*recA*precA)/(recA+precA)
        f1B=(2*recB*precB)/(recB+precB)
        
        microP=(tp+tn)/(tp+tn+fp+fn)
        microR=(tp+tn)/(tp+tn+fn+fp)
        microF=(2*microP*microR)/(microP+microR)
        macroP=(precA+precB)/2
        macroR=(recA+recB)/2
        microF=(f1A+f1B)/2
        
        self.macP+=macroP/10.
        self.macR+=macroR/10.
        self.macF+=macroF/10.
        self.micP+=microP/10.
        self.micR+=microR/10.
        self.micF+=microF/10.
        
        print('Micro Precision: '+str(microP))
        print('Micro Recall: '+str(microR))
        print('Micro F1: '+str(microF))
        print('Macro Precision: '+str(macroP))
        print('Macro Recall: '+str(macroR))
        print('Macro F1: '+str(macroF))