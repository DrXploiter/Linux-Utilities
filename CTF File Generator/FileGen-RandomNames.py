#!/usr/bin/python3
import sys
import os
from lorem_text import lorem
from RandomWordGenerator import*

numOfFiles = int(input('How many files do you wish to generate?: '))

paragraphLength = int(input('How many paragraphs do you wish to have for each file?: '))

filenameLength = int(input('How long should the filenames be?: '))

paragraphLength = paragraphLength*25 
print(paragraphLength)

rw = RandomWord(max_word_size=filenameLength)

for i in range (numOfFiles):
    #generate random name
	newFile = rw.generate()
	#using touch create file based on the randomly generated string
	createFiles = r"touch " + r"/home/$USER/Desktop/lorem/bulk/"+ newFile
	#execute above string argument 
	os.system(createFiles)
	
	#redirect text to the file
	writeTOfile = r"lorem_text --words="+str(paragraphLength)+r" > /home/$USER/Desktop/lorem/bulk/"+ newFile
	#execute above string argument 
	os.system(writeTOfile) 
	
	
