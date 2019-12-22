import csv
import utils
from twython import Twython
import random
import json

API_KEYS_FILE = 'APIkeys.txt'

def findClass(tweet, classWord):
    if classWord in tweet:
        return True

#Twitter api key stuff
api_keys = []
with open(API_KEYS_FILE) as api:
    for line in api:
        api_keys.append([str(l) for l in line.strip().split('\n')])

#Get Twitter credentials
APP_KEY = api_keys[0]
APP_SECRET = api_keys[1]
OAUTH_TOKEN = api_keys[2]
OAUTH_SECRET_TOKEN = api_keys[3]
#Create Twython object with creds
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_SECRET_TOKEN)
#Create query with search term, result_type, count, & lang
qu = input("What term are you searching? ")
rt = input("Would you like popular, recent, or mixed tweets? ")
c = input("How many tweets would you like right now? ")
l = input("What language do you want? (Example: english = en) ")
Q = {'q': qu, 'result_type': rt, 'count': int(c), 'lang': l}
# Create dictionary with desired data
i = 0
D = {'dataterm1': [], 'dataterm2': [], 'dataterm3': [], 'dataterm4': [], 'dataterm5': []}
# For each status in searching tweets
present = False

f = open('tweetData1.txt', 'w', encoding="utf-8")
for status in twitter.search(**Q)['statuses']:
    s = status['text'].replace(',', '')
    s = status['text'].replace('.', '')
    s = status['text'].replace('#', '')
    s = status['text'].replace('?', '')
    s = status['text'].replace(':', '')
    s = status['text'].replace('!', '')
    s = status['text'].replace('rt' , '')
    s = status['text'].replace('/', '')
    s = status['text'].lower()
    print(s)
    f.write(s + '\n')
f.close()
t = open('tweetBin.txt', 'r', encoding="utf-8")
for line in t:
    D['dataterm1'].append(i)
    i += 1
    st = line.replace('.', '')
    st = line.replace(':', '')
    st = line.replace('rt' , '')
    st = line.replace('/', '')
    st = line.lower()
    present = findClass(st, 'dataterm2')
    D['dataterm2'].append(1) if present == True else D['dataterm2'].append(0)
    present = False
    present = findClass(st, 'dataterm3')
    D['dataterm3'].append(1) if present == True else D['dataterm3'].append(0)
    present = False
    present = findClass(st, 'dataterm4')
    D['dataterm4'].append(1) if present == True else D['dataterm4'].append(0)
    present = False
    present = findClass(st, 'dataterm5')
    D['dataterm5'].append(1) if present == True else D['dataterm5'].append(0)
t.close()
with open('dict_file.csv', 'w', encoding="utf-8") as f:
    for key, value in D.items():
        f.write('%s:%s\n' % (key, value))
