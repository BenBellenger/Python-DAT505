import random

GREETING = ["hello", "hi", "hey", "yo", "sup"]
GREETING_RESPONSE = ["Alright dude?", "Hey, how you doin'?", "Alright bro?", "Alright mate?"]

SWEAR = ["shit", "fuck", "cunt", "twat", "asshole", "arsehole", "bitch", "ass"]
SWEAR_RESPONSE = ["Don't swear you little shit", "Watch your profanity", "Excuse me?!"]

FOOD = ["chocolate", "pizza", "chicken", "curry", "pasta", "soup"]
FOOD_RESPONSE = ["Yum", "Stop making me hungry", "Mmm tasty"]


def chatbotIntro():
	global answer
	print "Alright? I'm Dave."
	answer = raw_input("What do you want?: ").lower()
	chatbot()
	
def newQ():
	global answer
	answer = raw_input("You what?: ").lower()
	chatbot()
	
def chatbot():
	global answer 

	if any(x in answer for x in GREETING):
		print (random.choice(GREETING_RESPONSE))
		answer = raw_input().lower()
		chatbot()
		
	if any(x in answer for x in SWEAR):
		print (random.choice(SWEAR_RESPONSE))
		answer = raw_input().lower()
		chatbot()
        
	if any(x in answer for x in FOOD):
		print (random.choice(FOOD_RESPONSE))
		answer = raw_input().lower()
		chatbot()
		
	newQ()
	
chatbotIntro()

