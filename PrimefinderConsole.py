import random

"""Finds large primes p usable for Diffie Hellman Key Exchange.
That is p-1 could also be made divisible by a large prime.

This is done in to steps creating first the p-1 divisor,
then then p itself, both first by sieving, and then testing
likely prime values probabilistically with the Soloway Strassen method.

Want this to be overloaded to a really large integer class

Memory Usage: O(ln n)
Time Complexity: Yet to be computed

Cheers! """

#Still in bug test
def findSuperPrime(l):					#finds a prime P = 2rl+1 where l typically is a large prime
	arrlength = 3*l.bit_length()
	r_0 = 1						#r = r_0 + r1
	sqrtish = 2**( (arrlength.bit_length() + 1) // 2 )
	while True:
		print ':::::::::::'
		print 'Vi kjorer liste #%d ' %r_0
		worthTry = [True] * arrlength		#Array over likely r1 values
		for p in range(3, sqrtish, 2):
			print ' ----p = %d' %p
			r1 = 0
			while (2*(r_0+r1)*l + 1) % p != 0:
				print 'r1 = %d' %r1
				r1 += 1
			print 'first divisible P by p with r1 = %d' %r1
			while r1 < arrlength:
				print 'r1 = %d' %r1
				worthTry[r1] = False
				r1 += p
		print 'vi soker med Soloway Strassen'
		for r1 in range(0, arrlength):
			print 'I posisjon %d' %r1
			if worthTry[r1]:
				print 'likely value i r1 = %d' %r1
				z = 2*(r_0+r1)*l + 1
				if testPrime(z):
					return (z)
				print '%d ikke funnet til aa vaere prime' %z
		r_0 += arrlength

def findPrime(startInt):				#Routine for searching for primes
	arrlength = 2*startInt.bit_length()		#Looking in 2*log(n) interval. NB: Decides memory needed asymptotically!
	crtStartInt = startInt
	sqrtish = 2**( (arrlength.bit_length() + 1) // 2 )
	while True:					
		worthTry = [True] * arrlength		#An array over numbers to look for primes
		for p in range(2, sqrtish):
			nullerPos = -crtStartInt % p
			while nullerPos < arrlength:
				worthTry[nullerPos] = False
				nullerPos += p
		for x in range(0, arrlength):
			if worthTry[x]:
				z = crtStartInt + x
				if testPrime(z):
					return (z)
		crtStartInt += arrlength

def eratosthenes(maxInt):				#finds all primes up to, and not including maxInt
	worthTry = [True] * maxInt
	primelist = []
	sqrtish = 2**( (maxInt.bit_length() + 1) // 2 ) #this seems a bit slow, but since sqrt(maxInt) will be low, it shouldnt matter
	for x in range(2,sqrtish):
		if worthTry[x]:
			primelist.append(x)
			i = x
			while i < maxInt:
				worthTry[i] = False
				i += x
	for x in range(sqrtish,maxInt):
		if worthTry[x]:
			primelist.append(x)
	return primelist

def testPrime(z):					#implement soloway strassen method
	for i in range(0,100):
		a = random.randint(1,z)
		if jacobianSymbol(a,z) % z != rSidePower(a,z) % z:
			return False
	return True
def jacobianSymbol(a,z):
		b = a
		n = z
		crtval = 1
		while True:
			while (b % 2) == 0:
				if not (n % 8 == 1) | (n % 8 == 7):
					crtval = -crtval
				b = b / 2

			if b % n == 0:
				return 0
			if b == 1:
				return crtval

			if (b % 4 == 3) & (n % 4 == 3):
				crtval = -crtval
			load = n % b			#swap values and mod
			n = b
			b = load
def rSidePower(a,z):
	po = 1
	bitsleft = (z-1)/2
	crt = a
	while not bitsleft == 0:
		if bitsleft % 2 == 1:
			po = (po * crt) % z
			bitsleft -= 1
		bitsleft = bitsleft / 2
		crt = (crt*crt) % z
	return po

a = findPrime(1000)
print a
b = findSuperPrime(a)
print b

