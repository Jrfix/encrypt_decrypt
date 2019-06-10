#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from os import system
import random as r
import re

def main():
	os.system("clear")
	choice = raw_input("1) select file \n2) write text \n>> ")

	if choice == "1":
		path_f = raw_input("file path to read: ")
		dosya_ac(path_f)
	elif choice == "2":
		raw_text = raw_input("raw_text: ")
		file_path = raw_input("ex: /root/Desktop/tosavehere.txt ---> ")
		tanimlama(raw_text,file_path)
	else:
		print("wrong choice!!")
		raw_input("press any key to continue")
		main()
	



split_space = ["!","#","&"]
split_chars = ["%","?","*"]

raw_chars = []

rich_chars = []



shit = ["H,.,,","He,.,","Li.,,","Be...","B.,..","C.,.,","N.,.,","O,.,,","F..,.","K...,","Cr.,,","Hf,..","Cs,.,","Ra.,.","Fr,,,","Ce...","Np..,","Gd,,.","Pu,.,"]


apx = []
	



def algoritma(file_pathh):
	dosya = open(file_pathh,"a")
	result = ""
	
	#chr(100) -> reverse
	for i in range(0,len(raw_chars)):
		c = ord(raw_chars[i])
		a = int(c) + 373
		b = str(r.randint(1000,9999))+ r.choice(shit)+ str(r.randint(1000,9999))+ str(a) + str(r.randint(1000,9999))+ r.choice(shit)+ str(r.randint(1000000000,1999999999)) + r.choice(shit)
		#rich_chars.append(ord(raw_chars[i]))
		rich_chars.append(b)
		#print(rich_chars[i])
	for j in range(0,len(rich_chars)):
		
		apx.append(rich_chars[j] [13:16])
		print(apx[j])
		
		if apx[j] == str((32+373)):  ## ascii 32 = space character
			print("DONE")

			result += split_space[r.randint(0,len(split_space)-1)]
			
			
		else:
			result += split_chars[r.randint(0,len(split_chars)-1)]
			result += str(rich_chars[j])
	print(apx)
	print("\n")
	print(result)
	

	
	dosya.write(result)
	dosya.close()
		
		



def tanimlama(r_text,file_pat_to_r):
	for i in range(0,len(r_text)):
		raw_chars.append(r_text[i])
	algoritma(file_pat_to_r)













def dosya_ac(file_p):
	os.system("clear")
	print("beta..\n\n\n")
	raw_input("Press any key to continue")
	main()

	




	
	
main()

