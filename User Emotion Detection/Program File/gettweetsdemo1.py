import os
import tweepy as tw
import pandas as pd

consumer_key="M9xa6Cy6WQ2vTEkvlNoLTzlSK"
consumer_secret="rAatH0EF6nUJxWgawNXQYFporwVh2Pg5ZTLxghp9UmZDwsN2Of"


access_token="1404919999-wSGaTs7apk2aRPyBV6m90Ma69MeS6R0bmwgDpDq"
access_token_secret="Xl5iTq5hOgcVTtwuBu7ZP7g9kmySSBxaZead7kwmWRZSx"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
api.update_status("tweet216 from kits hanamkonda in DataScience Lab")
search_words = "#narendra modi"
date_since = "2018-11-16"
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(15)
t = []
for tweet in tweets:
    u=tweet.text
    u=u.encode('unicode-escape').decode('utf-8')
    print(tweet.id,tweet.user.screen_name, tweet.user.location)
    t.append((str(tweet.id),tweet.user.screen_name,u))
    print(u)

df = pd.DataFrame(t,columns=['tweetid','username','content'])
df.to_csv('ptweets.csv')
    
    

