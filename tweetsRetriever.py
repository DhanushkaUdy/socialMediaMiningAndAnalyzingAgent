import os
import tweepy
import csv

# Twitter API credentials
consumer_key = "Qkpqtt1DyoZHqthLHq1VyZRx4"
consumer_secret = "6x2DBCDMlNPmyPVv7qbXfzKRrqqhTSIPZuF2OmDPlsQUezXi3h"
access_key = "2571998706-J0d3Lbc9CjKSTfVtSpgEn54usbxsFoBbtDfchar"
access_secret = "Wh4Nk27sMNh0XueeihJdpiPAJwSqOtS8y7599P4aKehzn"

class getTweets(object):
    def get_all_tweets(self,screen_name):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        alltweets = []
        api = tweepy.API(auth)
        new_tweets = api.user_timeline(screen_name,language ="en", count=6)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1

        while len(new_tweets) > 0:
            # print "getting tweets before %s" % (oldest)
            new_tweets = api.user_timeline(screen_name,language="en", count=6, max_id=oldest)
            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1
            outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]
        return outtweets

# retreive = getTweets()
#
# path = "E:\\SocialMediaMinner\\RetrievedTweets" #File Patha to save Retrieved Tweets
# fpath = 'E:\\SocialMediaMinner\\log.csv' # Log File Path from Buddhika
#
# newDict=[]
# with open(fpath, "r") as logfile:
#     for line in logfile:
#         newDict.append(line)
#
#     i = 1
#     while (i< len(newDict)):
#         id = (newDict[i]).split()[:1]
#         tid = (newDict[i]).split()[1:]
#
#
#         if (os.path.isfile("E:\\SocialMediaMinner\\RetrievedTweets"+ str(id) + ".txt")):
#
#
#             # file = open(os.path.join(path, '%s.txt' % id), "ab")
#             # writer = csv.writer(file)
#             # writer.writerows(outtweet)
#
#         else:
#         #     outtweet = retreive.get_all_tweets(tid)
#         #     print(outtweet)
#             # outtweet = retreive.get_all_tweets(tid)
#             # file = open(os.path.join(path, '%s.txt' % id), "ab")
#             # writer = csv.writer(file)
#             # writer.writerows(outtweet)
#          i = i + 1
#
#

