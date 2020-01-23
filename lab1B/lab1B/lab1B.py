#Zachary Baughan, Lab 1B

#Variable Dictionary
#entering - controls while loop that allows for multiple room inputs
#roomCapacity - capacity of the room currently being checked
#outcome - outcome of people showing up to event
#difference - calculates spots left in event
#validInput - only True if valid input entered when asked to check another room

entering = 'y' #initialize variable for exiting while loop

while entering == 'y' or entering == 'Y': #while loop for multiple room inputs
	roomCapacity = input("What is the capacity of the room? ") #asking for information on events
	outcome = input("How many people want to attend the event? ")
	
	difference = int(roomCapacity) - int(outcome) #calculate spots left

	if int(outcome) < int(roomCapacity): #if spots left
		print("The event can be held.", difference, "people can still join.")
	elif int(outcome) > int(roomCapacity): #if too many people
		print("The event can not be held.", difference, "people must be removed to reach max capacity.")
	else: #if 100% filled, no more, no less
		print("The event can be held. No more people can join, for the room is at max capcity.")
	
	print('') #null string, cosmetic
	
	validInput = False #variable to get out of while loop
	while validInput == False: #check if the input is valid
		entering = input("Check another room? [y/n] ") #ask for another check
		if entering == "y" or entering == "Y" or entering == 'n' or entering == 'N': #valid inputs
			validInput = True #input validated

	print('') #null string, cosmetic