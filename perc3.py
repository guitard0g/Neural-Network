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
from random import choice

# INPUTS = [(1,0,-1,1),(0,1,-1,1),(0,0,-1,0),(1,1,-1,1)]
INPUTS = [(1,0,0,-1,1),(0,1,0,-1,1),(0,0,1,-1,0),(1,1,1,-1,0)]

def func(w, x): #ACTIVATION FUNCTION
    return int( (w[0]*x[0] + w[1]*x[1] + w[2]*x[2] + x[3]*w[3]) > 0)

#------------------------------------------------------------------

def trained(w):
    flag=0
    for curTest in INPUTS:
        if not func(w,curTest) == curTest[4]:
            flag=1
    return not flag

    
def verifyNetwork(w, epochs):
    print("--done--")
    print (' Epochs = ', epochs)
    for curTest in INPUTS:
        if func(w,curTest) == curTest[4]:
            print(" True " + str(func(w,curTest)) + " " + str(curTest))
        else:
            print(" False " + str(func(w,curTest)) + " " + str(curTest))
    print(" Line Generated: y= "+str(-1*round(w[0]/w[1],2))+"x + "+str(round(w[2]/w[1],2)))
      
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
    epochs = 0
    while not trained(w):
        # if not trained(w):
        #     w = deltaThisShiz(w, INPUTS[i%4])
        #     # verifyNetwork(i,w)
        # i+=1
        w = deltaThisShiz(w, choice(INPUTS))
        epochs+=1
        print("epochs = ", epochs)
    # print(w, ': ', trained(w))

    return w, epochs

def main():
    w, epochs = trainPerceptronWeights()
    verifyNetwork(w, epochs)

main()


