def mod_mul_inverse(x, n):
	r1 = n
	r2 = x
	t1 = 0
	t2 = 1
	while r2>0:
		q = int(r1/r2)
		r = r1-(q*r2)
		r1 = r2
		r2 = r
		t = t1-(q*t2)
		t1 = t2
		t2 = t
		print(q,r1,r2,r,t1,t2,t)
	if r1 == 1:
		if t1>=0:
			return t1
		else:
			return n+t1
	else:
		return "[Error: No inverse Exists]"

n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))
print("The modular multiplicative inverse of",x,"in Z"+str(n)," is:\n",mod_mul_inverse(x, n))
