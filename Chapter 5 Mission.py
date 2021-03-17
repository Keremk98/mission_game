#Chapter 5
def walking():
	global conversation
	global response

	
answer = input(print("Press x to talk to the father"))


response = ["Are you okay?"]
conversation = ["Let's go home fast"]
print(conversation, ":] Are you okay ", response, " , Let's go home fast")
import random
random.shuffle(response)
if answer == "x":
        print(response, ":] ", conversation[0])

	
#Game ends
