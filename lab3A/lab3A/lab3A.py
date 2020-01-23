#Zachary Baughan Lab 3A

#VARIABLE DICTIONARY
#totalRecords = keeps track of total records processed
#csvfile = holds the file before being read
#file = holds the file after being read
#rec = holds the current record
#type = type of computer
#brand = brand of computer
#disk2 = either ram of disk2 or null string
#os = os on computer
#year = year computer was made

#this code takes a pre-made document of records for computers and organizes data on them, such as type, os and ram.

import csv #needed for multiple functions
totalRecords = 0 #initialize variable to keep track of total records processed

typeList = []
brandList = []
cpuList = []
ramList = []
firstDiskList = []
numHDDList = []
secondDiskList = []
osList = []
yearList = []

print("{0:8}\t{1:8}\t{2:8}\t{3:8}\t{4:8}\t{5:8}\t{6:8}\t{7:8}\t{8:8}".format("TYPE", "BRAND", "CPU", "RAM", "1st DISK", "NO HDD", "2nd DISK", "OS", "YEAR")) #print headers
with open("C:/Users/008009114/Documents/CSV Files for Labs/3A/lab3a.csv") as csvfile: #import correct file
	file = csv.reader(csvfile) #read file for interpretting data
	for rec in file: #loop to go throug every record
		totalRecords += 1 #increment total records		

		if rec[0] == "D": #determine type from given data
			type = "Desktop"
		else:
			type = "Laptop"
		
		if rec[1] == "D": #determine brand from given data
			brand = "Dell"
		elif rec[1] == "HP":
			brand = "HP"
		else:
			brand = "Gateway"
		
		if rec[5] == "1": #determine anything that changes depending on number of disks, if 1 disk
			disk2 = ""
			os = rec[6]
			year = rec[7]
		elif rec[5] == "2": #if 2 disks
			disk2 = rec[6]
			os = rec[7]
			year = rec[8]

		typeList.append(type)
		brandList.append(brand)
		cpuList.append(rec[2])
		ramList.append(rec[3])
		firstDiskList.append(rec[4])
		numHDDList.append(
		secondDiskList
		osList
		yearList.append(year)

		print("{0:8}\t{1:8}\t{2:8}\t{3:8}\t{4:8}\t{5:8}\t{6:8}\t{7:8}\t{8:8}".format(type, brand, rec[2], rec[3], rec[4], rec[5], disk2, os, year)) #print record

print("")
print("(Note: to display correctly, please expand the size of the window horizontally until the year column is on the far right.)")