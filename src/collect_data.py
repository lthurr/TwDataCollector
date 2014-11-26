from twitter.connection import TwitterClient

def main():
    tw_client = TwitterClient()
    users = ['aprendengrande']
    print "Collecting data from Twitter"
    user_id = 133
    for user in users:
        last_followers = tw_client.get_last_200_followers(user)
        greater_than_200_tw_followers = [follower['screen_name'] for follower in last_followers['users'] if follower['statuses_count']>=200]
        print len(greater_than_200_tw_followers)
        for follower in greater_than_200_tw_followers:
            result_st = ""
            screen_name = follower
            result_st += "[%s]\n" % screen_name
            print "Collecting data for the user %s" % screen_name
            last_tweets = tw_client.get_last_200_tweets(screen_name)
            result_st += "count=%d\n" % len(last_tweets)
            i = 0
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