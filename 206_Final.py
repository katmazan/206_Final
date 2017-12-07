import facebook
import requests
import json
import sqlite3
import itertools
import collections
import datetime
import settings
from datetime import date
import calendar
CACHE_FNAME = "FB_cache.json"
# Put the rest of your caching setup here:

try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}
##get token from https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path=%7Bpost-id%7D&version=v2.11
graph = facebook.GraphAPI(access_token="EAACEdEose0cBAJzMMa3HwgFsEt6EUgkRciAjZBDmiMQt2BGGUrZC8Osy8L6VLUniloXlPczLXwA5ZBfUiwc11YcP7TyZChvWUv88gJ18U6HYsDrdU5r6Ry6G42ZAym2fFcteCVlTXdrZBFTYqGXuZCeRrXmY9xJQGqW7xkWdC7IlP0hAo9l6dflAF7ObdC19T0ZD")

profiles = graph.search(type = 'user',q = 'Katarina Mazanka')

for user in profiles['data']:
    print('%s %s' % (user['id'],user['name'].encode()))
##I am the first user in this print
user = '1547253215290162'
feed = graph.get_object(id = user, fields = 'posts', limit=100)
feed = feed['posts']
post_times = []
allposts = {}
##posts = graph.get_object(id= user, fields ='feed', limit = 100)

while(True):
    try:
        for post in feed['data']:
            
            post_times.append((post['created_time'].encode('utf-8')))
            
            key = post['id']
            CACHE_DICTION[key] = json.dumps(post['created_time'])
            
            if len(post_times) == 100:
                break
        ##print(posts['data'][i]['created_time'])

        # Attempt to make a request to the next page of data, if it exists.
        feed=requests.get(feed['paging']['next']).json()
        if len(post_times) == 100:
                break

    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break
    dumped_json_cache = json.dumps(CACHE_DICTION)
    fw = open(CACHE_FNAME,"w")
    fw.write(dumped_json_cache)
    fw.close()  
##print(allposts)
##print(allposts)
##print(posts)
##make dictionary that is days of the week
##takes in a dictionry and converts the time values to days of the week 
def convert_to_weekday(d):
    weekday_dict = {}
    for item in d:
        my_date = d[item]
        my_date = d[item][1:11]
        year = int(my_date[1:4])
        month = my_date[5:7]
         ##print(month)
        if month[0] == 0:
            month = int(month[1])

        else:
            month = int(month)
        ##print(month)
        day = int(my_date[8:10])
        my_date = date(year, month, day).weekday()
        if my_date == 0:
            my_date = 'Monday'
        if my_date == 1:
            my_date = 'Tuesday'
        if my_date == 2:
            my_date = 'Wednesday'
        if my_date == 3:
            my_date = 'Thursday'
        if my_date == 4:
            my_date = 'Friday'
        if my_date == 5:
            my_date = 'Saturday'
        if my_date == 6:
            my_date = 'Sunday'
         ##print(my_date)
        weekday_dict[item] = my_date
    return(weekday_dict)
##convert a dictionary to day, time format
def convert_to_weekday_and_time(d):
    time_dict = {}
    for item in d:
        my_date = d[item]
        my_date = d[item][1:11]
        year = int(my_date[1:4])
        month = my_date[5:7]
         ##print(month)
        if month[0] == 0:
            month = int(month[1])

        else:
            month = int(month)
        ##print(month)
        day = int(my_date[8:10])
        my_date = date(year, month, day).weekday()
        if my_date == 0:
            my_date = 'Monday'
        if my_date == 1:
            my_date = 'Tuesday'
        if my_date == 2:
            my_date = 'Wednesday'
        if my_date == 3:
            my_date = 'Thursday'
        if my_date == 4:
            my_date = 'Friday'
        if my_date == 5:
            my_date = 'Saturday'
        if my_date == 6:
            my_date = 'Sunday'
         ##print(my_date)
        my_time = int(d[item][12:14])
        print(my_time)
        if my_time in {0, 1, 2, 3, 4, 5}:
            my_time = '12am to 5:59am'
        if my_time in {6,7,8,9,10,11}:
            my_time = '6am to 11:59 am'
        if my_time in {12, 13, 14, 15, 16, 17}:
            my_time = '12pm to 5:59pm'
        if my_time in {18,19,20,21,22,23}:
            my_time = '6pm to 11:59pm'
        time_dict[item] = (my_date + '' + my_time)
    
    return(time_dict)
weekday_dict = convert_to_weekday(CACHE_DICTION)
time_dict = convert_to_weekday_and_time(CACHE_DICTION)
conn = sqlite3.connect('FB_table.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Times')
cur.execute('CREATE TABLE Times (post_id INT PRIMARY KEY,created_time TEXT)')
conn.commit()

for item in CACHE_DICTION:
    cur.execute('INSERT INTO Times (post_id, created_time) VALUES (?,?)',(item, time_dict[item]))
    conn.commit()
cur.execute('DROP TABLE IF EXISTS Weekdays')
cur.execute('CREATE TABLE Weekdays (post_id INT PRIMARY KEY,week_day TEXT)')
conn.commit()
for item in weekday_dict:
    cur.execute('INSERT INTO Weekdays (post_id, week_day) VALUES (?,?)',(item, weekday_dict[item]))
    conn.commit()
