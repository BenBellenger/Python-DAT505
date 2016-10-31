import twitter, datetime, sqlite3

user = 	3131378668

file = open("C:\Users\Ben\Desktop\Python-DAT505\Twitter/TwitterCredentials.txt")
creds = file.read().split('\n')

api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

timestamp = datetime.datetime.utcnow()

def getTweet():
	statuses = api.GetUserTimeline(user)
	print (statuses[0].text)

def newTweet():
	response = api.PostUpdate("Tweeted at " + str(timestamp))
	print("Status updated to: " + response.text)

getTweet()
newTweet()

#C:\Users\Ben\AppData\Local\Google\Chrome\User Data\Default\Current Session