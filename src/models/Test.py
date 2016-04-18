import Aggregator
import Comment
import json
import os

os.chdir('../data')
file = open(os.getcwd()+"/dummy_data.json")
data = json.load(file)

a = Aggregator.Aggregator()

for comment in data:
  c = Comment.Comment(comment['text'], comment['poster'])
  c.upvotes = comment['upvotes']
  c.downvotes = comment['downvotes']
  c.spam = comment['isSpam']
  c.score = c._confidence(c.upvotes, c.downvotes)
  a.add_comment(c)

a.get_comments()