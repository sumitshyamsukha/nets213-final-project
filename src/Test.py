import Aggregator
import Comment

a = Aggregator.Aggregator()
c = Comment.Comment("Hello World", "Sumit")
d = Comment.Comment("Hello", "Sumit")
a.add_comment(c)
d.mark_spam()
a.add_comment(d)
a.get_comments()