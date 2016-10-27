import random

GREETING_RESPONSE = ["Alright dude?", "Hey, how you doin'?", "Alright bro?", "Alright mate?"]
GREETING = ["hello", "hi", "hey", "yo", "sup"]

SWEAR = ["shit", "fuck", "cunt", "twat", "asshole", "arsehole", "bitch"]
SWEAR_RESPONSE = ["Don't swear you little shit", "Watch your profanity", "Excuse me?!"]



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

	if answer in GREETING:
		print (random.choice(GREETING_RESPONSE))
		answer = raw_input().lower()
		chatbot()
		
	if answer in SWEAR:
		print (random.choice(SWEAR_RESPONSE))
		answer = raw_input().lower()
		chatbot()
	
	newQ()
	
chatbotIntro()

