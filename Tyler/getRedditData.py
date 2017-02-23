import praw
from praw.models import MoreComments

#PRAW method
reddit = praw.Reddit(client_id='XarwttTqbYFghg',
                     client_secret='OzsZALZ9430Avf_jV83uq3Mxn10',
                     user_agent='my user agent')
#print(reddit.read_only)

for submission in reddit.subreddit('ama').hot(limit=100):
    title = submission.title

    comments = []
    for comment in submission.comments:
        if isinstance(comment, MoreComments):
            continue
        comments.append(comment)

    comments.sort(key=lambda comment: comment.score, reverse=True)

    if len(comments):
        ans = comments[0].body.replace("\n", " ")

    #write to NLC
    if len(title) + len(ans) <= 1024:
        print (title + ' , ' + 'python')

    #write to retrieve by generating JSON

