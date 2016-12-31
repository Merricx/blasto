#!/usr/bin/env python

import random

def decrypt(ciphertext, key="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):

	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	plain = ""

	for i in ciphertext:
		if i.isalpha():
			if i.isupper():
				charIndex = key.find(i)
				substituted = alpha[charIndex]
			else:
				charIndex = key.lower().find(i)
				substituted = alpha.lower()[charIndex]
			plain += substituted
		else:
			plain += i

	return plain

def init_key():

	key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	key = list(key)
	random.shuffle(key)

	return "".join(key)

def change_key(key):

	new_key = list(key)
	i = random.randrange(0,25)
	j = random.randrange(0,25)
	temp = new_key[i]
	new_key[i] = new_key[j]
	new_key[j] = temp

	return "".join(new_key)