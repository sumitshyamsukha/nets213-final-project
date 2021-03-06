from math import sqrt

class Comment(object):

  def __init__(self, text, poster):
      self.text = text
      self.poster = poster
      self.upvotes = 1
      self.downvotes = 0
      self.score = self._confidence(1, 0)
      self.spam = False

  def upvote(self):
      self.upvotes = self.upvotes + 1
      self.score = self._confidence(self.upvotes, self.downvotes)

  def downvote(self):
      self.downvotes = self.downvotes + 1
      self.score = self._confidence(self.upvotes, self.downvotes)

  # Source: http://www.evanmiller.org/how-not-to-sort-by-average-rating.html
  def _confidence(self, ups, downs):
    n = ups + downs

    if n == 0:
        return 0

    z = 1.96 #1.44 = 85%, 1.96 = 95%
    phat = float(ups) / n
    return ((phat + z*z/(2*n) - z * sqrt((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n))

  def mark_spam(self):
    self.spam = True