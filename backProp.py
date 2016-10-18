#Back prop bruhhhhhhhhhh by JOSH LEARN

#####################
#	Joshua Learn 	#
#	Period 1		#
#	6/11/2015		#
#####################




def randomlyAssignWeights():
	w = [[uniform(-1,1),uniform(-1,1),uniform(-1,1)] for row in range(9)]
	v = [[uniform(-1,1),uniform(-1,1),uniform(-1,1),uniform(-1,1),uniform(-1,1),uniform(-1,1),uniform(-1,1),uniform(-1,1)] for row in range(4)]

	return w,v

#---------------------------------------------------------------------------------------------------------------------------------------------------

def mult(v,m):

	assert len(v) == len(m), [len(v), len(m)]

	return [sum([ v[i]*m[i][j]
					for i in range (len(v))	])
						for j in range(len(m[0]))]

#---------------------------------------------------------------------------------------------------------------------------------------------------

def printAllData(w,h,v,y):

	print ("x = ")
	for cell in INPUTS:
		print(cell)
	print('='*50)

	print('w =')
	for row in w:
		for cell in row:
			print(cell, end=', ')
		print()
	print('='*50)

	print ("h = ")
	for cell in h:
		print(cell)
	print('='*50)

	print('v =')
	for row in v:
		for cell in row:
			print(cell, end=', ')
		print()
	print('='*50)

	print ("y = ", y)
	for cell in y:
		print(cell)
	print('='*50)		

#---------------------------------------------------------------------------------------------------------------------------------------------------

def sigmoid(x):
	return 1/(1 + exp(-x))

#---------------------------------------------------------------------------------------------------------------------------------------------------

def feedForward(x,w,v):
#---return dp, h, DP, y
	dp = mult(x, w)
	h = [sigmoid(dp[0]), sigmoid(dp[1]), sigmoid(dp[2]), -1]
	DP = mult(h, v)
	y = []
	for item in DP:
		y.append(sigmoid(item))

	return dp, h, DP, y

	pass

#---------------------------------------------------------------------------------------------------------------------------------------------------

def backPropagation(x,w,dp,h,v,DP,y):



	for j in range(len(v)):
		for k in range(len(v[0])):
			v[j][k] = v[j][k] - ALPHA*(y[k] - x[k])*y[k]*(1 - y[k])*h[j]

	for i in range(len(w)):
		for j in range(len(w[0])):
			delta = 0
			for k in range(len(v[0])):
				delta += ( (y[k] - x[k])*y[k] * v[j][k] )
			w[i][j] = w[i][j] - ( ALPHA * delta * h[j] * (1 - h[j]) * x[i] )


	return w, v

#---------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------------
  

def trained(w,v):
    for x in INPUTS:
        dp, h, DP, y = feedForward(x, w, v)
        for i in range(len(x)-1):
        	out = round(y[i])
        	t = x[i]
        	if out != t:
        		return False
    return True

#---------------------------------------------------------------------------------------------------------------------------------------------------


def verifyNetwork(epochs,w,v):
    print('---success---')
    print('Epochs = ' , epochs)
    for x in INPUTS:
   		dp, h, DP, y = feedForward(x, w, v)
   		for i in range(len(x)-1):
   			out = round(y[i])
   			t = x[i]
   			print('%5s'% (out == t) , '--->' , out,': ', t)
    
    

#---------------------------------------------------------------------------------------------------------------------------------------------------


def calculateE(y,t):
	E = 0
	for i in range(len(y)):
		E += 0.5*(y[i]-t[i])**2
	return E

def trainNetwork():
#---bookkeeping
	epochs = 0
	w, v = randomlyAssignWeights()
#---Train the perceptrons w-weights and v-weights.
	while epochs < TRIALS and not trained(w,v):
		for x in INPUTS:
			dp, h, DP, y = feedForward(x,w,v)
			w,v 		 = backPropagation(x,w,dp,h,v,DP,y)
		epochs+=1
		if epochs%100==0:
			print('E = ',  calculateE(y, x))
			print('epochs = ', epochs)
	return epochs, w, v

#---------------------------------------------------------------------------------------------------------------------------------------------------

from random import random, choice, shuffle, uniform, randint
from math import exp
TRIALS = 9000
ALPHA  = 0.2
INPUTS = [[1,0,0,0,0,0,0,0,-1],[0,1,0,0,0,0,0,0,-1],[0,0,1,0,0,0,0,0,-1],[0,0,0,1,0,0,0,0,-1],[0,0,0,0,1,0,0,0,-1],[0,0,0,0,0,1,0,0,-1],[0,0,0,0,0,0,1,0,-1],[0,0,0,0,0,0,0,1,-1]]

#---------------------------------------------------------------------------------------------------------------------------------------------------

def main():
	epochs,w,v = trainNetwork()
	verifyNetwork(epochs,w,v)

#---------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__': from time import clock; START_TIME = clock(); main(); print('--> Run time =', round(clock() - START_TIME, 2), 'seconds <--');