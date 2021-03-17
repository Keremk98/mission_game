#Kerem Kok
#Chapter1
prompt = "Please enter user name. Enter X to start"
userInput = ""
while userInput != "X":
        userInput = str(input(prompt))
        print(userInput)
if userInput == "Student":
        prompt = "Welcome Student"
NAME=str(input("enter the name: "))#game asks user for name

print("hello",NAME) #Game welcomes the user

userInput = input("Enter 'S' to start or 'X' to exit").capitalize() #starting or exiting the game

#starts action module
def bus():
	global busNumber
	global response

	
responses = ["Can I get on this bus", "I am looking to find my father"]
busNumberChoice = ["1", "2", "3"]
import random
random.shuffle(busNumberChoice)
busNumber = busNumberChoice[2]
print(busNumber, ":] Can I get on ", busNumber, " , I need to go")

random.shuffle(responses)
answer = input(print("Press x to get on the bus"))


#Chapter 2 starts



