import random

GREETING = ["hello", "hi", "hey", "yo", "sup"]
GREETING_RESPONSE = ["Alright dude?", "Hey, how you doin'?", "Alright bro?", "Alright mate?"]

SWEAR = ["shit", "fuck", "cunt", "twat", "arse", "bitch", "ass", "damn"]
SWEAR_RESPONSE = ["Don't swear you little shit", "Watch your profanity", "Excuse me?!"]

FOOD = ["chocolate", "pizza", "chicken", "curry", "pasta", "soup"]
FOOD_RESPONSE = ["Yum", "Stop making me hungry", "Mmm tasty"]

LOVE = ["love", "<3"]
LOVE_RESPONSE = ["Oh, thanks I guess...", "I don't even like you", "I love you more"]

WEATHER = ["weather", "sunny", "cloudy"]
WEATHER_RESPONSE = ["It's dark here...", "Look out the window", "It's cold here..."]

BYE = ["bye", "night", "seeya", "adios", "later"]
BYE_RESPONSE = ["Bye", "Come back soon", "Please don't leave me", "Is it your bed time?"]

HELP = ["help"]
HELP_RESPONSE = ["I don't want to help you", "I don't know how to help", "No, you help me"]


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
	
	if any(x in answer for x in LOVE):
		print (random.choice(LOVE_RESPONSE))
		answer = raw_input().lower()
		chatbot()
		
	if any(x in answer for x in WEATHER):
		print (random.choice(WEATHER_RESPONSE))
		answer = raw_input().lower()
		chatbot()
		
	if any(x in answer for x in BYE):
		print (random.choice(BYE_RESPONSE))
		answer = raw_input().lower()
		chatbot()

	if any(x in answer for x in HELP):
		print (random.choice(HELP_RESPONSE))
		
	newQ()
	
chatbotIntro()

