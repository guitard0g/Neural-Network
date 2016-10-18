#fib


#####################
#	Dynamic 		#
#	Programming		#
#	Joshua Learn 	#
#	Period 1		#
#	6/11/2015		#
#####################



###########################################################################
# Richard Bellman worked for a Theoretical Physics Division group in Los Alamos during WWII.
###########################################################################

def fib1(n):
	if n<3:
		return n
	a = b = 1
	for i in range(n-2):
		a, b = b, a+b
	return b

def fib2(n):
	if n<3:
		return 1
	
	return fib2(n-1) + fib2(n-2)

def fib3(Dic, n):
	if n in Dic:
		return Dic[n]

	Dic[n] = fib3(Dic, n-1) + fib3(Dic, n-2)
	return Dic[n]

def fib4(n):
	if n in fib4.dict:
		return fib4.dict[n]

	fib4.dict[n] = fib4(n-1) + fib4(n-2)
	return fib4.dict[n]
fib4.dict = {1:1, 2:1}

def fib5(n):
	def fib(n):
		if n in fib.dict:
			return fib.dict[n]

		fib.dict[n] = fib(n-1) + fib(n-2)
		return fib.dict[n]
	fib.dict = {1:1, 2:1}

	return fib(n)


def main():
	Dic = {1:1, 2:1}
	print(Dic[2])
	print(fib2(10))

main()