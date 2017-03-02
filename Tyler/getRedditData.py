from __future__ import print_function
import praw
import json
from praw.models import MoreComments


#FILL OUT THIS FIRST
subreddit = 'AskHistorians'
limit = 10  #how many questions
category = 'history' #DONT FORGET TO CHANGE THIS
retrieveFile = 'redditRetrieve' + subreddit + '.json'
NLCfile = 'redditNLC.csv'
RankerFile = 'redditRanker' + subreddit + '.csv'
commentThresh = 10



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
    topScore = 0
    topComments = []  # each comment should be comment, score, id
    numComments = len(comments)
    if numComments > 0:

        if numComments > commentThresh:
            numComments = commentThresh

        for k in range(numComments):
            topComments.append([comments[k].body, comments[k].score, comments[k]])


    #comments[2] = answerID
    #comments[1] = answerScore

    #store data to write to NLC
    if len(title) + len(category) <= 1024:
        nlcData.append(title + ' , ' + category)

    answerSequence = '' #answerid, answerscore
    for commentEntry in topComments:
        # store data to write to the retriever
        retrieveData['documents'].append({'id': str(commentEntry[2]),'body': {'question': title,'answer': commentEntry[0]}})

        # store data to write to the ranker
        answerSequence = answerSequence + ',' + '\"' + str(commentEntry[2]) + '\"' + ',' + '\"' + str(commentEntry[1]) + '\"'

    rankerData.append('\"' + title + '\"' + answerSequence)

#write to NLCDataFile
f= open(NLCfile, 'a')
for line in nlcData:
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
