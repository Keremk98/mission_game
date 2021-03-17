Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def walking():
	global conversation
	global response

	
>>> answer = input(print("Press x to talk to the father"))
Press x to talk to the father
None
>>> response = ["Are you okay?"]
>>> conversation = ["Let's go home fast"]
>>> print(conversation, ":] Are you okay ", response, " , Let's go home fast")
["Let's go home fast"] :] Are you okay  ['Are you okay?']  , Let's go home fast
>>> import random
>>> random.shuffle(response)
>>> if answer == "x":
	print(response, ":] ", conversation[0])

	
>>> #Game ends