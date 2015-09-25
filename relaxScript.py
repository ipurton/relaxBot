import tweepy, time, sys, random
# Import libraries

__author__ = 'ipurton'

# This is a Twitter bot which tweets a random quote selected from a local txt file
# At present, scheduling is done using Windows Task Scheduler
# Based on the guide found at http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/

# Revision Log:
# 9/24/2015     IP      Created script, GitHub repo. Scheduling set up using Windows Task Scheduler

# Define quotes_file, file from which quotes are selected
quotes_file = "relaxQuotes.txt"

# Define api_file, file from which private Twitter API items are read
api_file = "twitterAccess.txt"

# Both of the above files should be in the same folder as this script

# Read in lines from api_file into a list
with open(api_file) as f:
    api_items = list(f)

# api_items contains: CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

# Above method maintains the /n character, which needs to be removed from later calls
# Enter application authentication information
# If a 401 error occurs when the script is run, the formatting of these items is likely to blame.
# Check for trailing spaces and the like.
CONSUMER_KEY = api_items[0][:-1]
CONSUMER_SECRET = api_items[1][:-1]
ACCESS_KEY = api_items[2][:-1]
ACCESS_SECRET = api_items[3]
# As the above is the final line of the text file, there is no /n character to remove
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
# Last character (/n) is omitted
api.update_status(status=quotes[quote_ln][:-1])