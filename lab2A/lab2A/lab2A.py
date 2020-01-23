#Zachary Baughan Lab 2A

#VARIABLE DICTIONARY
#totalRecords = the total number of records processed
#over = keeps track of how many rooms are 'over' the limit
#csvfile = holds the file used before it's read
#file = holds the file used after it's read
#overflow = holds how many people are over the limit in a rooms deemed 'over'

#this code reads a csv file with room names, maximum room numbers, and number of attendees. it then shows how many rooms are over and by how much.

import csv #STEP 1
totalRecords = 0 #STEP 1.5
over = 0 #initialize variable to keep track of how many rooms are 'over' the limit
print("{0:25}        {1:10}      {2:10}\t{3:10}".format("NAME", "MAXIMUM", "ATTENDING", "OVERFLOW")) #headers
with open("C:/Users/008009114/Documents/CSV Files for Labs/2A/lab2a.csv") as csvfile: #STEP 2
	file = csv.reader(csvfile) #STEP 3
	for rec in file: #STEP 4
		totalRecords += 1 #increment total records processed
		if rec[2] > rec[1]: #check if a room is 'over'
			over += 1 #increment total records showing 'over' rooms
			overflow = int(rec[1]) - int(rec[2])
			overflow = overflow * -1
			print("{0:25}\t{1:10}\t{2:10}\t{3:10}".format(rec[0], rec[1], rec[2], str(overflow))) #print details of 'over' room

print('')

print("Processed", totalRecords, "records") #print total records
print("There are", over, "rooms over the limit") #print number of 'over' rooms