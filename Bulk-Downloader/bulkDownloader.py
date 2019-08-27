#!/usr/bin/python3
#------------------------------------------------------------
# Bulk Downloader: Coded by DrXploiter 
#------------------------------------------------------------
import subprocess
import fileinput
#------------------------------------------------------------
print("--------------------------------------")
print("Simple Bulk downloader. by DrXploiter ")
print("--------------------------------------")
print("Menu")
print("1. Use a single link-list")
print("2. Use multiple link-lists\n")
print("--------------------------------------")
choice = int(input("> "))
#------------------------------------------------------ 
if (choice == 1):
	print("link-list path?: ")
	listLocation = input("> ")
	txt = open(listLocation, 'r', encoding='utf-8-sig')
	downloadLISTtxt = txt.readlines()
	#strip spaces and \n from list 
	downloadLISTtxt = list(map(str.strip, downloadLISTtxt))
	downloadLIST = []
	for everyitem in downloadLISTtxt:
		downloadLIST.append(everyitem)	
		subprocess.run(['bash', '-c', 'wget $0', everyitem])
	
#---------------------------------------------------------	
if (choice == 2):
	lst = []
	multiplepaths = []
	print("How many download link-lists do you want to download from?: ")
	numlist = int(input('> '))
	for x in range(numlist):
		print("link-list path?: ")
		listLocation = input("> ")
		multiplepaths.append(listLocation)
		allfiles = fileinput.input(multiplepaths)
	for lines in allfiles:
		lst.append(str(lines))
		#strip spaces and \n from list 
		lst = list(map(str.strip, lst))
	for everyLink in lst:
		subprocess.run(['bash', '-c', 'wget $0', everyLink])
