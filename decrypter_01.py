#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from os import system
import re


split_space = ["!","#","&"]
split_chars = ["%","?","*"]

char_words = []
space_words = []

file_path = raw_input("ex: /root/Desktop/tosavehere.txt ---> ")


all_data = []


def algoritma(data):

	result = re.split("\%|\?|\*|",data) # for chars
	#result = re.split("\!|\#|\&|",data)  # for spaces
	
	
	for i in result:
		
		char_words.append(i)
		
			
	char_words.pop(0)
	print(char_words)
	print("\n\n\n")
	
	
	b = 0
	for j in char_words:
		result2 = re.split("\!|\#|\&|",char_words[b])  # for spaces
		b += 1
		for a in result2:
			if a == '':
				
				
				space_words.append(a + " ")
			else:
				#chr(100) -> reverse
				c = int(a[13:16])
				c = c - 373
				c = chr(c)
				space_words.append(c)

	#print(space_words)
	export(space_words)


def export(data):
	export_file = raw_input("export file path: ")
	ex_string = ""
	print(data)
	for i in range(0,len(data)):
		ex_string += data[i]
	print("\n\n--->   " + ex_string)
	exf = open(export_file,"w")
	exf.write(ex_string)	
	
	
	
	
	

	







def dosya_oku():
	dosya = open(file_path,"r+")
	string_data = dosya.read()
	dosya.close()
	algoritma(string_data)
	
dosya_oku()
