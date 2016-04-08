from math import sqrt
import heapq

class Aggregator(object):

  def __init__(self):
    self.comments = []

  def add_comment(self, comment):
    if comment is not None:
      pair = (comment.score, comment)
      heapq.heappush(self.comments, pair)

  def get_comments(self):
    for c in self.comments:
      print "%f %s" % (c[0], c[1].text)