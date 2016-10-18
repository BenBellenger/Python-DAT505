GREETING = ("hello", "hi", "hey", "yo", "sup",)

GREETING_RESPONSE = ["Alright dude?", "Hey, how you doin'?"]


def chatbotIntro():
    print "I am Dave."
    answer = raw_input("What do you want?: ").lower()
    helloCheck()
    
def helloCheck(sentance):
    for word in answer.words:
        if word.lower() in GREETING:
            return random.choice(GREETING_RESPONSE)
        
chatbotIntro()