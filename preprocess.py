# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:51:14 2017

@author: kyleh
"""
import numpy

def preprocess(data, meta):
#######useful variables
    n=len(data)
    classLabel=meta.names()[-1]
    classes=list(set(data[classLabel]))
    numOfAtts=len(meta.names())
    m=len(set(data[classLabel]))
    
    
    #######fix missing values
    count=0
    for j in range(0,numOfAtts-1):
        classCounts=numpy.ndarray((len(set(data[meta.names()[j]])),m))
        classCounts[:][:]=0
        l=set(data[meta.names()[j]])
        l=list(l)
        for k in range(0, n):
            classCounts[l.index(data[k][j])][classes.index(data[k][-1])]+=1
        for i in range(0,n):
            if data[i][j]==b'?':
                c=data[i][-1]
                data[i][j]=l[classCounts[classes.index(c)].tolist().index(max(classCounts[classes.index(c)][:]))]
                count+=1
    
    #print(count)
                
    #######discretize
    def entropy(lBound=0, rBound=-1):
        if rBound==-1:
            rBound=n
        classCounts=[0]*m
        for i in range(lBound, rBound):
            classCounts[classes.index(data[classLabel][i])]+=1
        size=rBound-lBound
        entropy=0
        for count in classCounts:
            if count==0 or size==0:
                continue
            prob=count/size
            entropy-=prob*numpy.log2(prob)
        return entropy
    
    def findMPs(att):
        if len(set(data[att]))<1000:
            return entropyBasedMPs(att, [], 1, -1, e)
        else:
            vals=list(set(data[att]))
            vals=numpy.sort(vals)
            MP=(vals[0]+vals[-1])/2
            ret=[]
            for i in range(0,len(vals)):
                if vals[i]>MP:
                    ret.append((i-1,MP))
                    break
            return ret
    
    def entropyBasedMPs(att, MPs, lBound, rBound, eOld):
#        print(MPs)
        if rBound==-1:
            rBound=n
        bestInfo=1.
        bestMP=-1.
        bestI=-1
        size=rBound-lBound
        for i in range(lBound+1,rBound):
            if data[att][i]==data[att][i-1]:
                continue
            else:
                midpoint=int((data[att][i]+data[att][i-1])/2)
                eL=entropy(lBound,i)
                eR=entropy(i, rBound)
    #            print('EntropyL: '+str(eL))
    #            print('EntropyR: '+str(eR))
    #            print('Size: '+str(size))
    #            print('i-lBound: '+str(i-lBound))
    #            print('rBound-i: '+str(rBound-i))
                info=((i-lBound)/size)*eL+(rBound-i)/size*eR
    #            print('Info: '+str(info))
                if info<bestInfo:
                    bestInfo=info
                    bestMP=midpoint
                    bestI=i
    #                print((bestMP, bestInfo))
        gain=eOld-bestInfo
    #    print('eOld: '+str(eOld))
    #    print('Best Info: '+str(bestInfo))
    #    print('Gain: '+str(gain))
        if bestMP==-1 or bestMP==lBound or bestMP==rBound:
            return MPs
        if gain<.1 and len(MPs)>0:
    #        print('Gain too low')
            if len(MPs)==0:
                MPs.append((bestI,bestMP))
            return MPs
        MPs.append((bestI,bestMP))
    #    print('\n')
    #    print('BestInfo: '+str(bestInfo))
        if bestInfo>.05:
            MPs=entropyBasedMPs(att, MPs, lBound, bestI, bestInfo)
            MPs=entropyBasedMPs(att, MPs, bestI, rBound, bestInfo)
            return MPs
    #    print(MPs)
        else:
            return MPs
    
    #data.sort(order='fnlwgt')
    #print(data['fnlwgt'].tolist())
    
    e=entropy()
    for i in range(0, numOfAtts-1):
        if meta.types()[i]=='numeric':
    #        print(meta.names()[i])
            data.sort(order=meta.names()[i])
            MPs=sorted(findMPs(meta.names()[i]))
    #        print(MPs)
            prev=0
            for mp in MPs:
                val=mp[1]
    #            for sample in data[meta.names()[i]][prev:mp[0]]:
    #                print(type(sample))
    #            prev=mp[0]
                data[meta.names()[i]][prev:mp[0]]=val
                prev=mp[0]
            data[meta.names()[i]][prev:]=data[meta.names()[i]][-1]    
                    
#    data.sort(order=meta.names()[2])
    return data          