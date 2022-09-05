
import pyodbc
from textwrap3 import wrap
import tweepy as tp

file_tw = r"C:\Users\tugno\OneDrive\Projects\Twitter\Set-up\keys.txt"

with open(file_tw, 'r') as file_tw:
    all_keys = file_tw.read().splitlines()
    api_key = all_keys[1]
    api_key_secret = all_keys[3]
    access_token = all_keys[7]
    access_token_secret = all_keys[9]

authenticator = tp.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tp.API(authenticator, wait_on_rate_limit=True)


file_db = r"C:\Users\tugno\OneDrive\Projects\Twitter\Set-up\log-db.txt"

with open(file_db, 'r') as file_db:
    all_logs = file_db.read().splitlines()
    server_name = all_logs[1]
    database_name = all_logs[3]
    user = all_logs[5]
    passw = all_logs[7]

server = server_name 
database = database_name 
username = user 
password = passw
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

query = 'select first_tweet, long_tweet from twe.single_json where publication_date = convert(date, getdate())'
cursor.execute(query)
tweet_day_list = cursor.fetchall()
first_tweet = tweet_day_list[0][0]
text = tweet_day_list[0][1]

def exec_tweet():

    try:
        # list wehre there are the parts of the text -> (every single reply to the previous tweet)
        reply = wrap(text, width=280, fix_sentence_endings=True)

        # empty list for store the code for each reply of the thread
        reply_codes = []
        # parts of the text
        n = len(reply)

        for t in range(0, n+1):
            reply_codes.append(f'tweet{t+1} = api.update_status(status={reply}[{t}], in_reply_to_status_id=tweet{t}.id, auto_populate_reply_metadata=True)')
        # variable string where all the replays are on a single line
        all_replyies = '\n'.join(reply_codes)

        # first tweet of the thread
        tweet0 = api.update_status(first_tweet)
        # execute thoses lines as code, not as strings
        exec(all_replyies)
    except:
        pass


exec_tweet()  
cnxn.close()
