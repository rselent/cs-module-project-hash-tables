def word_count(s):
	# Your code here
	import re

	counts = {}
	words = s.split()
	chars = '":;,.-+=/\\|[]{}()*^&'
	charCheck = set( chars).difference( s)

	if len( charCheck) == len( chars):
		return counts

	words = re.sub( '[^A-Za-z0-9 \']+', ' ', s.lower()).split()
	for word in words:
		if word in counts:
			counts[ word] += 1
		else:
			counts[ word] = 1
	items = dict( counts.items())

	return items


if __name__ == "__main__":
	print(word_count(""))
	print(word_count("Hello"))
	print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
	print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

	############## TEST FILE ERROR: ##############
	# INSTRUCTIONS FROM README:
	# If the input contains no ignored characters, return an empty dictionary.
	##############					##############
	print( word_count("Hello    hello"))
	print( word_count('a a\ra\na\ta \t\r\n'))