#!/usr/bin/env python
#contact: norberto.chavez.nc@gmail.com
import csv
# Note:  The source you want to search must be in the same folder as this script.


#The csv you want to search will be named here.
src_file = open('yourmispindicators.csv','r')
reader = csv.reader(src_file)
indicator = []

for row in reader:
	try:
#Pay attention to col#.  Python starts counting at 0.  Here, python is searching in column "D".
		col3 = str(row[3])
#The string you are searching for comes after the ==.
		if col3 == 'email-src':
#Change row[#] to whatever you wish to write to a txt.
			indicator.append(row[4])
#Keep this in here for emtpy lines.  
	except:
		pass

# Change the " **.txt" to the file name you wish to save to. 
dest_file = open("newfile.txt", "w+")
for item in indicator:
	dest_file.write(item + '\n')