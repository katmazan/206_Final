import praw
import settings
import json
import sqlite3

reddit = praw.Reddit(client_id=settings.red_client,
                     client_secret= settings.red_secret,
                     user_agent='User Agent:script:python.my.data.collection:v1.2.3 (by /u/katarain)')
CACHE_FNAME = "red_cacnhe.json"
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}
def get_hot(sub):
    d_list = []
    if sub + '0' in CACHE_DICTION:
        print("Data was in the cache")
        print(CACHE_DICTION[sub + '0'])
        return CACHE_DICTION[sub + '0']
    else:
        print("Making a request")
        print("Retrieving" + "\n")
        i = 0
        for submission in reddit.subreddit(sub).hot(limit=100):
            
        
        
            CACHE_DICTION[sub + str(i)] = submission.title
            i = i +1
    ##print(CACHE_DICTION[key])
    dumped_json_cache = json.dumps(CACHE_DICTION)
    fw = open(CACHE_FNAME,"w")
    fw.write(dumped_json_cache)
    fw.close() # Close the open file
            
get_hot('Overwatch')
def count_words(d):
    word_d = {}
    for item in d:
        string = str(d[item])
        string = string.split()

        for i in range(len(string)):
            ##print(string[i])
            word = string[i]
            if word not in word_d:
                word_d[word] = 1
            else:
                word_d[word] = word_d[word] + 1
    return(word_d)
ow_words = count_words(CACHE_DICTION)
conn = sqlite3.connect('Red_table.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Hot')
cur.execute('CREATE TABLE Hot (word TEXT PRIMARY KEY,count INT)')
conn.commit()

for item in ow_words:
    cur.execute('INSERT INTO Hot (word, count) VALUES (?,?)',(item, ow_words[item]))
    conn.commit()