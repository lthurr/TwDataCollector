import time
from twitter.connection import TwitterClient

def main():
    tw_client = TwitterClient()
    users_to_iterate = tw_client.get_last_200_followers('Citroen_Arg')
    users = [user['screen_name'] for user in users_to_iterate['users']]
    print "Collecting data from Twitter"
    user_id = 0
    for user in users:
        print "Collecting data from %s account" % user
        last_followers = tw_client.get_last_200_followers(user)
        greater_than_200_tw_followers = [follower['screen_name'] for follower in last_followers['users'] if follower['statuses_count']>=200]
        print len(greater_than_200_tw_followers)
        for k, follower in enumerate(greater_than_200_tw_followers):
            result_st = ""
            screen_name = follower
            result_st += "[%s]\n" % screen_name
            print "%d) Collecting data for the user %s" % (k, screen_name)
            last_tweets = tw_client.get_last_200_tweets(screen_name)
            result_st += "count=%d\n" % len(last_tweets)
            i = 0
            if "Rate limit exceeded" in last_tweets.__repr__():
                assert False, "Rate limit exceeded"
            for tweet in last_tweets:
                try:
                    result_st += screen_name + '_tweet_' + str(i) + '="%s"\n' % tweet['text'].replace('\\n', '<br>')
                except Exception as e:
                    print tweet
                i += 1
            with open('DATASET_%d.cfg' % user_id, 'wb') as configfile:
                configfile.write(result_st.encode('utf8'))
            user_id += 1

if __name__ == '__main__':
    main()
