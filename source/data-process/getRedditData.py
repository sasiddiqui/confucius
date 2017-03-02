from __future__ import print_function
import praw
import json
from praw.models import MoreComments


#FILL OUT THIS FIRST
subreddit = 'AskScience'
limit = 10  #how many questions
category = 'science' #DONT FORGET TO CHANGE THIS
retrieveFile = 'redditRetrieve' + subreddit + '.json'
NLCfile = 'redditNLC.csv'


#PRAW credentials
reddit = praw.Reddit(client_id='XarwttTqbYFghg',
                     client_secret='OzsZALZ9430Avf_jV83uq3Mxn10',
                     user_agent='my user agent')
titles = []
nlcData = []
retrieveData = {}
retrieveData['documents'] = []

idcount = 0
for submission in reddit.subreddit(subreddit).top(limit=limit):

    title = submission.title
    titles.append(title)

    comments = []
    for comment in submission.comments:
        if isinstance(comment, MoreComments):
            continue
        comments.append(comment)

    comments.sort(key=lambda comment: comment.score, reverse=True)

    if len(comments):
        ans = comments[0].body

    #store data to write to NLC
    if len(title) + len(ans) <= 1024:
        nlcData.append(title + ' , ' + category)

    #store data to write to the retriever
    retrieveData['documents'].append({'id': idcount,'body': {'question': submission.title,'answer': ans}})

    #increment id
    idcount += 1

#write to NLCData
f= open(NLCfile, 'a')
for line in nlcData:
    print(line.encode('utf8'), file=f)
f.close()

#write to retrieveData
retriever = open(retrieveFile, 'w+')
json.dump(retrieveData, retriever, indent=4)

