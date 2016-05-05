import csv
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from numpy import corrcoef, sum, log, arange
from numpy.random import rand
from pylab import pcolor, show, colorbar, xticks, yticks

# Source: http://www.evanmiller.org/how-not-to-sort-by-average-rating.html
def _confidence(ups, downs):
    n = ups + downs

    if n == 0:
        return 0

    z = 1.96 #1.44 = 85%, 1.96 = 95%
    phat = float(ups) / n
    return ((phat + z*z/(2*n) - z * sqrt((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n))


with open('f901672.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	comments = {}
	confidence = {}
	length = {}
	for row in reader:
		comment = row[16].strip().encode('utf-8')
		vote = row[14].strip().encode('utf-8')
		if comment not in comments:
			comments[comment] = {}
			if 'Downvote comment' in vote:
				comments[comment]['down'] = 1
			if 'Upvote comment' in vote:
				comments[comment]['up'] = 1
		else:
			if 'Downvote comment' in vote and 'down' in comments[comment]:
				comments[comment]['down'] = comments[comment]['down'] + 1
			else:
				comments[comment]['down'] = 1
			if 'Upvote comment' in vote and 'up' in comments[comment]:
				comments[comment]['up'] = comments[comment]['up'] + 1
			else:
				comments[comment]['up'] = 1

	for comment in comments:
		if 'up' in comments[comment]:
			up = comments[comment]['up']
		else:
			up = 0
		if 'down' in comments[comment]:
			down = comments[comment]['down']
		else:
			down = 0
		confidence_rating = _confidence(up, down)
		confidence[comment] = confidence_rating
		length[comment] = len(comment)
	

	x = []
	y = []

	for comment in confidence:
		x.append(confidence[comment])
		y.append(length[comment])

	fig, ax = plt.subplots()
	ax.scatter(x, y)
	ax.set_xlabel(' Quality of Comment (in confidence rating) ')
	ax.set_ylabel(' Length of Comment (in number of characters) ')
	plt.show()