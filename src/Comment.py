class Comment(object):

  def __init__(self, text, poster):
      self.text = text
      self.upvotes = 1
      self.downvotes = 0
      self.score = 1
      self.isSpam = False
      self.poster = poster