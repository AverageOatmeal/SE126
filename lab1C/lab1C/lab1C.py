#Zachary Baughan, Lab 1C

#Variable Dictionary
#entering - controls while loop that allows for multiple room inputs
#maxCapacity - capacity of the room currently being checked
#outcome - outcome of people showing up to event
#difference - calculates spots left in event
#validInput - only True if valid input entered when asked to check another room
#attending - variable for attendees()
#roomCapacity - variable for capacity()
#attendence - parameter for register(), represents current attendence
#max - parameter for register(), represents maximum room capacity
#checkAnother - variable in checkMoreRooms, stores user's response when asked if they want to check another room

def capacity():
	roomCapacity = input("What is the capacity of the room? ") #asking for maximum room capacity
	return roomCapacity #returnning max room capacity


def attendees():
	attending = input("How many people want to attend the event? ") #asking for outcome
	return attending #returning outcome


def register(attendence, max):
	spots = int(max) - int(attendence) #calculate spots left
	return spots #returning spots left, if any


def checkMoreRooms():
	validInput = False #variable to get out of while loop
	while validInput == False: #check if the input is valid
		checkAnother = input("Check another room? [y/n] ") #ask for another check
		if checkAnother == "y" or checkAnother == "Y" or checkAnother == 'n' or checkAnother == 'N': #valid inputs
			validInput = True #input validated
	
	return checkAnother #returning response


entering = 'y' #initialize variable for exiting while loop

while entering == 'y' or entering == 'Y': #while loop for multiple room inputs
	
	maxCapacity = capacity() #function for maximum room capacity
	outcome = attendees() #function for outcome
	difference = register(outcome, maxCapacity) #function for difference of attendees against max room capacity

	if int(outcome) < int(maxCapacity): #if spots left
		print("The event can be held.", difference, "people can still join.")
	elif int(outcome) > int(maxCapacity): #if too many people
		print("The event can not be held due to fire regulations.", str(int(difference) * -1), "people must be removed due to fire regulations.")
	else: #if 100% filled, no more, no less
		print("The event can be held. No more people can join, for the room is at max capcity.")
	
	print('') #null string, cosmetic
	
	entering = checkMoreRooms() #check if user wants to enter more rooms

	print('') #null string, cosmetic