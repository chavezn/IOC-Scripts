#!/usr/bin/python
import filecmp
import wget
import os
import os.path
from os import path 
import time


#API Key goes here!
API_Key = 'YOURAPIKEY'

#Pick you database type.  Just delete the "#."
#DB_type = 'xml'
#DB_type = 'json'
DB_type = 'csv'

#Where would you like to save the database file?  Default is /Users/current user or ./
dblocation = './'
url = 'http://data.phishtank.com/data/%s/online-valid.%s' % (API_Key, DB_type)


def PhishTankDBUpdate():
#Checks to see if database files already exist.
	if path.exists('%sPhishTankDatabase.%s' % (dblocation, DB_type)) and path.exists('%sPhishTankDatabase_old.%s' % (dblocation, DB_type)):

	#Compares old and new database files.  If they match, nothing gets downloaded.  This probably occured because of a timing issue.
	#Database files are update every hour on the hour.  If downloads occur within the same hour, the files will match.
		if filecmp.cmp('%sPhishTankDatabase.%s' % (dblocation, DB_type), '%sPhishTankDatabase_old.%s' % (dblocation, DB_type)):
			print ("Old and new database match.  Database was not updated.")

	#This runs when the database files don't match; this indicates a previously successful database update.
		else:
			os.remove('%sPhishTankDatabase_old.%s' % (dblocation, DB_type))
			os.rename('%sPhishTankDatabase.%s' % (dblocation, DB_type), '%sPhishTankDatabase_old.%s' % (dblocation, DB_type))
			print ("Downloading database. ")
			wget.download(url, '%sPhishTankDatabase.%s' % (dblocation, DB_type))


#This runs when there is no successful update AND download.  In otherwords, there's only one database file.			
	elif path.exists('%sPhishTankDatabase.%s' % (dblocation, DB_type)):
		os.rename('%sPhishTankDatabase.%s' % (dblocation, DB_type), '%sPhishTankDatabase_old.%s' % (dblocation, DB_type))
		wget.download(url, '%sPhishTankDatabase.%s' % (dblocation, DB_type))		
		print ("Updated database.")


#This runs if there is no database file at all.
	else:
		wget.download(url, '%sPhishTankDatabase.%s' % (dblocation, DB_type))
		print ("Downloaded database.")

#This script will continue running.  Change the sleep (in seconds) to download and update the database file in whatever
#interval works for you.
while True:
	PhishTankDBUpdate()
	time.sleep(3600)





