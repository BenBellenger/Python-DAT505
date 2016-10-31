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
	
def tweetHistory():
	response = api.PostUpdate("I like " + str(f))
	print("Status updated to: " + response.text)

	
f = open('C:\Users\Ben\AppData\Local\Google\Chrome\User Data\Default\History', 'rb')
data = f.read()
f.close()
f = open('C:\Users\Ben\Desktop\Python-DAT505\Twitter\History.txt', 'w')
f.write(repr(data))
f.close()

getTweet()
newTweet()
tweetHistory()