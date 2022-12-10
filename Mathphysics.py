import numpy as np

def Trap(xi, xf, n, f):
	x, h = np.linspace(xi, xf, n, retstep = True)
	y = f(x)
	return 0.5*h*(y[0] + 2*sum(y[1: n-1: 1]) + y[n-1])
	
	
def Simp(xi, xf, n, f):
	x, h = np.linspace(xi, xf, n, retstep = True)
	y = f(x)
	return h*(y[0] + 4*sum(y[1: n-1: 2]) + 2*sum(y[2: n-1: 2]) + y[n-1])/3
	
	
def NR(x, f, df, err):
	if df(x) == 0:
	    raise ValueError("You had guessed the the point at maximum or minimum of the function")
	while abs(f(x)) >= err:
		x -= f(x)/df(x)
	return x
	

def Bisection(a, b, f, err):
	itr = 0
	while abs(b-a) >= err:
		itr += 1
		if f(a)*f(b) < 0:
			c = (a+b)/2
			if f(c)*f(a) < 0:
				b = c
			elif f(c)*f(b) < 0:
				a = c
			else:
				return c, itr
		elif f(a)*f(b) == 0:
			if f(a) == 0:
				return a
			else: return b
		else:
			raise ValueError("Choose another guesses.")
	return c, itr
	
def FirstEuler(diffEq, t, x, h, tf):
	tt, xx = [t], [x]
	while t <= tf:
		t += h
		x += h*diffEq(t, x)
		tt.append(t)
		xx.append(x)
	return tt, xx
	
def SecondEuler(diffEq, t, x, v, h, tf):
	tt, xx = [t], [x]
	while t <= tf:
		t += h
		x += h*v
		v += h*diffEq(t, x, v)
		tt.append(t)
		xx.append(x)
	return tt, xx
	
#For Linear algebra

def matrixMul(A, B):
	row = len(A); col = len(B[0])
	if len(A[0]) != len(B):
		raise ValueError(f"Column of {A} is not equal to row of {B}")
	C = np.zeros((row, col))
	for i in range(row):
		for j in range(col):
			for k in range(len(B)):
				C[i][j] += A[i][k]*B[k][j]
				
	return C
	
def Add(A, B):
	if len(A) != len(B) and len(A[0]) != len(B[0]):
		raise ValueError ("Addition is not possible diffarential dimensions")
	C = np.zeros((len(A)))
	for i in range(len(A)):
		for j in range(len(A)):
			C[i][j] = A[i][j] + B[i][j]
	return C

def Sub(A, B):
	if len(A) != len(B) and len(A[0]) != len(B[0]):
		raise ValueError ("Substraction is not possible diffarential dimensions")
	row = len(A); col = len(B[0])
	C = np.zeros((row, col))
	for i in range(len(A)):
		for j in range(len(A)):
			C[i][j] = A[i][j] - B[i][j]
	return C
	
def Trace(A):
	if len(A) != len(A[0]):
		raise ValueError ("Trace is only possible for square matrix")
	Sum = 0
	for i in range(len(A)):
		Sum += A[i][i]	
	return Sum
	
def Transpose(A):
	if len(A) != len(A[0]):
		raise ValueError ("Transpose is only possible for square matrix")
	C = np.zeros((len(A), len(A)))
	for i in range(len(A)):
		C[i][j] = A[j][i]
		
	return C
	

#Some special function to evalute some physical quantity

#To find terminal velocity
def terVelocityCheck(v, err):
	for i in range(len(v)):
		if abs(v[i] - v[i+1]) <= err:
			return v[i]
