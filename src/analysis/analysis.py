import csv
from math import sqrt
import operator

def ratings(ratings):
    confidence = []
    for i in ratings:
        u = 0
        d = 0
        for j in ratings[i]:
            if 'up' in j.lower():
                u = u + 1
            if 'down' in j.lower():
                d = d + 1
        confidence.append((i, _confidence(u, d)))
    sorted_ratings = sorted(confidence, key=operator.itemgetter(1), reverse=True)
    return sorted_ratings

# Source: http://www.evanmiller.org/how-not-to-sort-by-average-rating.html
def _confidence(ups, downs):
    n = ups + downs

    if n == 0:
        return 0

    z = 1.96 #1.44 = 85%, 1.96 = 95%
    phat = float(ups) / n
    return ((phat + z*z/(2*n) - z * sqrt((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n))

with open('f901679.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	users = {}
	for row in reader:
		if row[17] not in users:
			users[row[17]] = [row[15]]
		else:
			users[row[17]].append(row[15])
	
	ratings = ratings(users)
	for rating in ratings:
		print rating[0].strip() + " " + str(rating[1])
