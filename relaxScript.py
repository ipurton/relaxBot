import tweepy, time, sys, random, os
# Import libraries

__author__ = 'ipurton'

# This is a Twitter bot which tweets a random quote selected from a local txt file
# At present, scheduling is done using Windows Task Scheduler
# Based on the guide found at http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/

# Revision Log:
# 9/28/2015	    IP		Switched to absolute paths instead of relative paths for the two text files, added rstrip to
#                       programatically remove newlines and trailing spaces from api_items
# 9/24/2015     IP      Created script, GitHub repo. Scheduling set up using Windows Task Scheduler

# The following fines are called with absolute paths so that this script can be run from any directory.
# This makes it so that a Scheduled Task for this script does not need to have a defined "Start In" directory.

# Define quotes_file, file from which quotes are selected
quotes_file = "C:/Users/Isaac/Documents/Python/relaxBot/relaxQuotes.txt"

# Define api_file, file from which private Twitter API items are read
api_file = "C:/Users/Isaac/Documents/Python/relaxBot/twitterAccess.txt"

# Read in lines from api_file into a list
with open(api_file) as f:
    api_items = list(f)

# api_items contains: CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

# Above method maintains the /n character, which needs to be removed for later calls
for i in range(3):
    api_items[i] = api_items[i].rstrip()

# Enter application authentication information
CONSUMER_KEY = api_items[0]
CONSUMER_SECRET = api_items[1]
ACCESS_KEY = api_items[2]
ACCESS_SECRET = api_items[3]
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Read in lines from quotes_file into a list
with open(quotes_file) as f:
    quotes = list(f)

# Find number of lines in quote_items
quote_n = len(quotes)

# Generate a random integer from the range 0 to quote_n
quote_ln = random.randrange(0, quote_n, 1)

# Update status using the quote located on the line of quotes_file indicated by quote_ln
# Last character (/n) is omitted using rstrip
api.update_status(status=quotes[quote_ln].rstrip("/n"))
