#!/usr/bin/env python
import random, math, re

def gen_key(numkey,size):

	key = []
	for i in range(size):
		key.append([])
		for j in range(size):
			key[i].append(0)

	for i in numkey:
		key[int(i)/size][int(i)%size] = 1

	return key


def rot90(key, size):

	new_key = []
	k = 0

	for i in range(0,size):
		l = 0
		new_key.append([])
		for j in range(size-1,-1,-1):
			new_key[k].append(key[j][i])
		
		k += 1

	return new_key

def readCipher(cipher, key, size):

	plain = ""
	index = 0
	for i in range(size):
		for j in range(size):
			if key[i][j] == 1:
				plain += cipher[index]
			index += 1

	return plain

def decrypt(ciphertext, key):

	ciphertext = re.sub("\s+","",ciphertext)

	result = ""
	size = int(math.sqrt(len(ciphertext)))
	key = key.split(",")
	key = gen_key(key, size)

	for i in range(4):
		result += readCipher(ciphertext, key, size)
		key = rot90(key, size)


	return result

def determine_key(size):

	total_square = (size*size)-1
	max_row  = size-1
	key_count = 0
	all_key = []

	count = 0
	val1 = 0
	val3 = total_square
	addition = 2
	while max_row >= 1:
		val2 = max_row + val1
		val4 = val3 - max_row
		for i in range(max_row):
			all_key.append([])
			all_key[count].append(val1)
			all_key[count].append(val2)
			all_key[count].append(val3)
			all_key[count].append(val4)
			count += 1
			val1 += 1
			val2 += size
			val3 -= 1
			val4 -= size
		max_row -= 2
		val1 += addition
		val3 -= addition
		addition += 2

	return all_key

def init_key(size):

	possible_key = determine_key(size)
	key = []

	for i in range(len(possible_key)):
		key.append(str(possible_key[i][random.randrange(0,4)]))

	return ",".join(key)

def change_key(key, all_key):

	new_key = key.split(",")
	randnum1 = random.randrange(0,len(new_key))
	randnum2 = random.randrange(0,len(new_key))
	new_key[randnum1] = str(all_key[randnum1][random.randrange(0,4)])
	new_key[randnum2] = str(all_key[randnum2][random.randrange(0,4)])

	return ",".join(new_key)