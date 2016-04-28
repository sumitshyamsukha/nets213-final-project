import sys
import urllib2
import json
import csv
import re

api_key = '6879-6446b8b4f00a2ecb7744e4c4fa211ff8'
corpus = {}
users = []

def construct_api_call(user):
  return 'https://hypothes.is/api/search?limit=1000&user=' + str(user)

def get_comments(user) :
  try:
    request = urllib2.Request(construct_api_call(user), headers={
      'Authorization': 'Bearer ' + api_key
      })
    text = urllib2.urlopen(request)
  except urllib2.HTTPError:
    sys.stderr.write('BAD REQUEST\n')
    return None
  try:
    response = json.loads(text.read())
  except ValueError:
    sys.stderr.write('JSON ERROR\n')
    return None
  comments = []
  for row in response['rows']:
    text = row['text'].strip()
    target = row['target']
    exact = 'null'
    for item in target:
    	if 'selector' in item:
    		for selector in item['selector']:
    			if 'exact' in selector:
    				exact = selector['exact']
    				break
    if text != None and text != '':
      comments.append((exact.strip().encode('utf-8'), text))
  return comments

def get_all_comments():
  for user in users:
    if user not in corpus:
      corpus[user] = get_comments(user)

def get_all_users(): 
  with open('users.txt', 'r') as f:
    while True:
      user = f.readline()
      if user == '':
        break
      if user not in users:
        users.append(user)
  get_all_comments()

def construct_csv():
  get_all_users()
  with open('data.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['User', 'Annotation', 'Comment'])
    for user in corpus:
      if corpus[user] is not None:
        for comment in corpus[user]:
          writer.writerow([user, comment[0], comment[1]])
    csvfile.close()

def construct_user_csv():
	get_all_users()
	with open('users.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Username'])
		for user in users:
			writer.writerow([user])
		csvfile.close()

#construct_csv()
construct_user_csv()