from __future__ import print_function
import praw
import json
from praw.models import MoreComments

#FILL OUT THIS FIRST
subreddit = 'AskHistorians'
category = 'history' #DONT FORGET TO CHANGE THIS

limit = 150  #how many questions
retrieveFile = 'redditRetrieve' + subreddit + '.json'
NLCfile = 'redditNLC.csv'
RankerFile = 'redditRanker' + subreddit + '.csv'
commentThresh = 4

#PRAW credentials
reddit = praw.Reddit(client_id='XarwttTqbYFghg',
                     client_secret='OzsZALZ9430Avf_jV83uq3Mxn10',
                     user_agent='my user agent')
nlcData = []
rankerData = []
retrieveData = {}
retrieveData['documents'] = []

for submission in reddit.subreddit(subreddit).top(limit=limit):


    title = submission.title

    #get all the top level comments in that submission
    comments = []
    for comment in submission.comments:
        if isinstance(comment, MoreComments):
            continue
        comments.append(comment)

    #sort the comments by upvotes
    comments.sort(key=lambda comment: comment.score, reverse=True)

    #store the top n comments
    topComments = []  # each comment should be comment, score, id
    numComments = len(comments)
    if numComments > 0:

        if numComments > commentThresh:
            numComments = commentThresh

        for k in range(numComments):
            topComments.append([comments[k].body, comments[k].score, comments[k]])

    #comments[2] = answerID
    #comments[1] = answerScore
    #comments[0] = commentbody

    #store data to write to NLC
    if len(title) + len(category) <= 1024:
        title = title.replace(',', '')
        nlcData.append(title + ' , ' + category)

    answerSequence = '' #answerid, answerscore
    if len(topComments) > 0:

        for commentEntry in topComments:
            #filter characters
            title = title.replace(':', '<colon>').replace('%','<percent>').replace('\"','<dq>').replace('\n', '<br>').replace('\'','<sq>')
            answer = commentEntry[0].replace(':', '<colon>').replace('%','<percent>').replace('\"','<dq>').replace('\n', '<br>').replace('\'','<sq>')

            # store data to write to the retriever
            retrieveData['documents'].append({'id': str(commentEntry[2]),'body': {'question': title,'answer': '<p>' + commentEntry[0] + '</p>'}})

            # store data to write to the ranker
            answerSequence = answerSequence + ',' + '\"' + str(commentEntry[2]) + '\"' + ',' + '\"' + str(commentEntry[1]) + '\"'

        rankerData.append('\"' + '<p>' + title + '</p>' + '\"' + answerSequence)

#write to NLCDataFile
f= open(NLCfile, 'a')
for line in nlcData:
    line = line.replace('\n', ' ')
    line = line.replace('"', '&quote')
    print(line.encode('utf8'), file=f)
f.close()

#write to retrieveDataFile
retriever = open(retrieveFile, 'w+')
json.dump(retrieveData, retriever, indent=4)

#write to rankerDataFile
f2 = open(RankerFile, 'w+')
for line in rankerData:
    print(line.encode('utf8'), file=f2)
f2.close()
