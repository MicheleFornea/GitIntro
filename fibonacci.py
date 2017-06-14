def fibo(N):
	x=1
	y=0
	for i in range(N):
		x=x+y
		y=x-y
	return x