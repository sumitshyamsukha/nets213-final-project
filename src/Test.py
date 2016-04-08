import Aggregator
import Comment

a = Aggregator.Aggregator()
c = Comment.Comment("Hello World", "Sumit")
a.add_comment(c)
a.get_comments()