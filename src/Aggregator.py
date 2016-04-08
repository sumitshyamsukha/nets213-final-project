from math import sqrt
import heapq

class Aggregator(object):

  def __init__(self):
    self.comments = []

  def add_comment(self, comment):
    if comment is not None:
      pair = (self._confidence(comment.upvotes, comment.downvotes), comment)
      heapq.heappush(self.comments, pair)

  def get_comments(self):
    for c in self.comments:
      print "%f %s" % (c[0], c[1].text)

  def _confidence(self, ups, downs):
    n = ups + downs

    if n == 0:
        return 0

    z = 1.96 #1.44 = 85%, 1.96 = 95%
    phat = float(ups) / n
    return ((phat + z*z/(2*n) - z * sqrt((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n))