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

# INPUTS = [(1,0,-1,1),(0,1,-1,1),(0,0,-1,0),(1,1,-1,1)]
INPUTS = [(1,0,0,-1,1),(0,1,0,-1,1),(0,0,1,-1,0),(1,1,1,-1,0)]

def func(w, x): #ACTIVATION FUNCTION
    return int( (w[0]*x[0] + w[1]*x[1] + w[2]*x[2] + x[3]*w[3]) > 0)

#------------------------------------------------------------------

def trained(w):
    for x in INPUTS:
        y = func(w,x)
        t = x[4]
        if y != t:
            return False
    return True

def verifyNetwork(epochs, w):
    print(' Epochs = ', epochs)

    for x in INPUTS:
        t = x[4]
        y = func(w,x)
        print('%5s'%(y==t), '-->',  y, x)
        print('\n=== Statistics ===')
        print()    
#-------------------------------------------------------------------
def deltaThisShiz(w, x):
    y = func(w, x)
    t = x[4]

    alpha = 0.1
    w0 = w[0]
    
    w1 = w[1]

    w2 = w[2]

    w3 = w[3]

    w0 = w0 - alpha*(y-t)*x[0]
    
    w1 = w1 - alpha*(y-t)*x[1]    

    w2 = w2 - alpha*(y-t)*x[2]

    w3 = w3 - alpha*(y-t)*x[3]

    return (w0, w1, w2, w3)


# def printAllData(w,h,v,y)

def trainPerceptronWeights():
#---Create random weights
    w0 = int(random.random()*10)
    
    w1 = int(random.random()*10)
    
    w2 = int(random.random()*10)

    w3 = int(random.random()*10)
    
    w = [w0, w1, w2, w3]
#---TEST CASES
    # (0, 0) - FALSE
    # (0, 1) - TRUE  
    # (1, 0) - TRUE
    # (1, 1) - TRUE
    
    
    
#---Train perceptron weights for limited number of sessions

#-----feed forward

#-----correct weights with delta rule
    # i = 0
    while not trained(w):
        # if not trained(w):
        #     w = deltaThisShiz(w, INPUTS[i%4])
        #     # verifyNetwork(i,w)
        # i+=1
        for i in range(4):
            w = deltaThisShiz(w, INPUTS[i%4])

    print(w, ': ', trained(w))

def main():
    trainPerceptronWeights()

main()
    