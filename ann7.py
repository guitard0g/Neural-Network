#part 7


from random import choice



def yValue(x,w,v):
	h = [0,0,-1]
	h[0] = int( (w[0][0]*x[0] + w[1][0]*x[1] + w[2][0]*x[2]) > 0)
	h[1] = int( (w[0][1]*x[0] + w[1][1]*x[1] + w[2][1]*x[2]) > 0)
	y = int( (v[0]*h[0] + v[1]*h[1] + v[2]*h[2]) > 0)
	return y

def trained(w,v):
	for x in INPUTS:
		y = yValue(x,w,v)
		t = x[3]
		if y != t:
			return False
	return True


def verifyNetwork(epochs, w,v):
	print(' Epochs = ', epochs)

	for x in INPUTS:
		t = x[3]
		y = yValue(x,w,v)
		print('%5s'%(y==t), '-->',  yValue(x,w,v), x)
		print('\n=== Statistics ===')
		print()



def initializeWeights():
	w = [[-1,1,], [-1,1,], [-1.5,0.5],]
	v = [1,1,1.5]
	return w,v

def improveWeights():
	w0 = int(random()*2)-1
	w1 = int(random()*2)-1
	w2 = int(random()*2)-1
	
	return (w0,w1,w2),v

def trainNetwork():

	epochs = 0

	h = [0,0,-1]

	w,v = initializeWeights()

	while epochs < TRIALS and not trained(w,v):
		x = choice(INPUTS)

		w,v = improveWeights(w,v)

		h[0] = int( (w[0][0]*x[0] + w[1][0]*x[1] + w[2][0]*x[2]) > 0)
		h[1] = int( (w[0][1]*x[0] + w[1][1]*x[1] + w[2][1]*x[2]) > 0)

		epochs+=1
	return epochs,w,v

from random import choice, random, shuffle
TRIALS = 9000
ALPHA = 0.25
INPUTS = [(1,0,-1,1),(0,1,-1,1),(0,0,-1,0),(1,1,-1,0)]


def main():
	epochs,w,v = trainNetwork()
	verifyNetwork(epochs,w,v)


main()