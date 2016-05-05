penn = {}
cf = {}

with open('penn_ratings.txt') as f:
	while True:
		line = f.readline().split(' ')
		if len(line) < 2:
			break
		penn[line[0]] = line[1].strip()

with open('cfratings.txt') as f:
	while True:
		line = f.readline().split(' ')
		if len(line) < 2:
			break
		cf[line[0]] = line[1].strip()

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
users = []

for user in cf:
	if user in penn:
		users.append(user)
		y.append(cf[user])
		x.append(penn[user])


fig, ax = plt.subplots()
ax.scatter(x, y)
for i, txt in enumerate(users):
    ax.annotate(txt, (x[i],y[i]), rotation='45')

ax.set_xlabel(' Penn Student Ratings of Penn Students')
ax.set_ylabel(' CrowdFlower Worker Ratings of Penn Students')
plt.show()