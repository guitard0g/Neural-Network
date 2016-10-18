# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:14:34 2015

@author: J


PERCEPTRON (NEURAL NETWORKS PART I)

"""

"""-----------------------------FRAMEWORK--------------------------
"""

import math
import random
from random import choice , shuffle

# INPUTS = [(1,0,-1,1),(0,1,-1,1),(0,0,-1,0),(1,1,-1,1)]
INPUTS = [(1,0,-1,1),(0,1,-1,1),(0,0,-1,0),(1,1,-1,1)]

def func(w, x): #ACTIVATION FUNCTION
    return int( (w[0]*x[0] + w[1]*x[1] + w[2]*x[2]) > 0)

#------------------------------------------------------------------

  
def trained(w):
    flag=0
    for curTest in INPUTS:
        if not func(w,curTest) == curTest[3]:
            flag=1
    return not flag

    
def verifyNetwork(w, epochs):
    print("--done--")
    print (' Epochs = ', epochs)
    for curTest in INPUTS:
        if func(w,curTest) == curTest[3]:
            print(" True " + str(func(w,curTest)) + " " + str(curTest))
        else:
            print(" False " + str(func(w,curTest)) + " " + str(curTest))
    print(" Line Generated: y= "+str(-1*round(w[0]/w[1],2))+"x + "+str(round(w[2]/w[1],2)))
      
#-------------------------------------------------------------------
def deltaThisShiz(w, x):
    y = func(w, x)
    t = x[3]

    alpha = 0.1
    w0 = w[0]
    
    w1 = w[1]

    w2 = w[2]

    w0 = w0 - alpha*(y-t)*x[0]
    
    w1 = w1 - alpha*(y-t)*x[1]    

    w2 = w2 - alpha*(y-t)*x[2]

    return (w0, w1, w2)


# def printAllData(w,h,v,y)

def trainPerceptronWeights():
#---Create random weights
    w0 = int(random.random()*10)
    
    w1 = int(random.random()*10)
    
    w2 = int(random.random()*10)
    
    w = [w0, w1, w2]
#---TEST CASES
    # (0, 0) - FALSE
    # (0, 1) - TRUE  
    # (1, 0) - TRUE
    # (1, 1) - TRUE
    
    
    
#---Train perceptron weights for limited number of sessions

#-----feed forward

#-----correct weights with delta rule

    epochs = 0
    INPUTS2 = INPUTS[:]
    shuffle(INPUTS2)
    while not trained(w):
        for item in INPUTS2:
            w = deltaThisShiz(w, item)
            epochs+=1
            print("epochs = ", epochs)
        shuffle(INPUTS2)
    
    return w, epochs
def main():
    w, epochs = trainPerceptronWeights()
    verifyNetwork(w, epochs)

if __name__ == '__main__': from time import clock; START_TIME = clock(); main(); print('--> Run Time = ', round(clock()-START_TIME, 2), 'seconds <--');

    