# Your code here
import math
import random
import time


def slowfun_too_slow(x, y):
	v = math.pow(x, y)
	v = math.factorial(v)
	v //= (x + y)
	v %= 982451653

	return v

def slowfun(x, y):
	"""
	Rewrite slowfun_too_slow() in here so that the program produces the same
	output, but completes quickly instead of taking ages to run.
	"""
	# Your code here
	return cache[ x, y]


cache = {}

def lookupTable():
	for x in range( 2, 14):
		for y in range( 3, 6):
			v = math.pow( x, y)
			v = math.factorial( v)
			v //= (x + y)
			v %= 982451653
			cache[ x, y] = v


start = time.time()
lookupTable()

start100 = time.time()

# Do not modify below this line!

for i in range(50000):
	x = random.randrange(2, 14)
	y = random.randrange(3, 6)
	print(f'{i}: {x},{y}: {slowfun(x, y)}')

end = time.time()

print( "{:.5f} sec".format( end - start100))
print( "{:.5f} sec".format( end - start))


"""
range 100
fun_slow =  ~9.000s
fun before =  .015s
fun after =  2.850s

range 50k
fun_slow = inf
fun before = 6.467s
fun after =  9.054s
"""

