# Your code here
import time


cache = {}

def expensive_seq(x, y, z):
	# Your code here
	key = (x, y, z)

	if x <= 0: 
		return y + z

	if key not in cache:
		cache[ key] = expensive_seq( x-1, y+1, z) + \
					  expensive_seq( x-2, y+2, z*2) + \
					  expensive_seq( x-3, y+3, z*3)
	return cache[ key]



if __name__ == "__main__":

	start = time.time()
	for i in range(10):
		x = expensive_seq(i*2, i*3, i*4)
		print(f"{i*2} {i*3} {i*4} = {x}")

	endSmall = time.time()
	print(expensive_seq(150, 400, 800))

	endBig = time.time()
	print( "1-10\n{:.5f} sec".format( endSmall - start))
	print( "150+\n{:.5f} sec".format( endBig - start))


"""
1-10
0.00600 sec
150+
0.13899 sec
"""

