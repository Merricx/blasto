#!/usr/bin/env python
#-*-coding: utf-8-*-

import random, time, math, re, os
import cipher

result = {'key':'','plain':'','score':''}

def hill_climbing(cipher_text, cipher_type, count, sleep, lang):

	if cipher_type == "subs":
		method = cipher.substitution
		parent_key = cipher.substitution.init_key()
	elif cipher_type == "grille":
		method = cipher.grille
		size = int(math.sqrt(len(cipher_text)))
		all_key = method.determine_key(size)
		parent_key = cipher.grille.init_key(size)

	child_key = ""
	parent_score = score_text(method.decrypt(cipher_text, parent_key), lang)

	for i in range(0, count):
		if cipher_type == "grille":
			child_key = method.change_key(parent_key, all_key)
		else:
			child_key = method.change_key(parent_key)
		child_score = score_text(method.decrypt(cipher_text, child_key), lang)

		if (child_score > parent_score):
			parent_score = child_score
			parent_key = child_key

		time.sleep(sleep)

	result['key'] = parent_key
	result['plain'] = method.decrypt(cipher_text, parent_key)
	result['score'] = parent_score

	return result


def common_dict(cipher_text, lang):

	keylist = open(os.path.join(os.path.dirname(__file__),'keylist'))
	best_key = ""
	best_score = -99e99

	for i in range(349):
		key = keylist.next()
		score = score_text(cipher.substitution.decrypt(cipher_text, key), lang)

		if score > best_score:
			best_score = score
			best_key = key

	result['key'] = best_key
	result['plain'] = cipher.substitution.decrypt(cipher_text, best_key)
	result['score'] = best_score

	return result


def score_text(text, lang='en'):

	if lang == 'en':
		from qgr import en
		text = re.sub("[^A-Z]","",text.upper())
		alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		method = en
	elif lang == 'de':
		from qgr import de
		text = re.sub("[^A-ZÄÖÜß]","",text.upper())
		alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß"
		method = de
	elif lang == 'es':
		from qgr import es
		text = re.sub("[^A-ZÑ]","",text.upper())
		alpha = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
		method = es

	temp = [0,0,0,0]
	score = 0
	l = len(alpha)

	for i in range(0,len(text)-3):
		temp[0] = alpha.find(text[i])
		temp[1] = alpha.find(text[i+1])
		temp[2] = alpha.find(text[i+2])
		temp[3] = alpha.find(text[i+3])
		score += method.qgram[(l**3)*temp[0] + (l**2)*temp[1] + l*temp[2] + temp[3]]

	return score