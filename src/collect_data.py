from twitter.connection import TwitterClient
import ConfigParser

def main():
    config = ConfigParser.RawConfigParser()
    tw_client = TwitterClient()
    n_followers = 0
    n_tweets = 0
    users = ['AgenciaTelam', 'LAVOZcomar', 'clarincom', 'C5N']
    print "Collecting data from Twitter"
    for user in users:
        last_followers = tw_client.get_last_200_followers(user)
        n_followers += len(last_followers['users'])
        for follower in last_followers['users']:
            screen_name = follower['screen_name']
            try:
                config.add_section(screen_name)
            except Exception:
                break
            print "Collecting data for the user %s" % screen_name
            last_tweets = tw_client.get_last_200_tweets(screen_name)
            n_tweets += len(last_tweets)
            config.set(screen_name, 'count', len(last_tweets))
            i = 0
            for tweet in last_tweets:
                try:
                    config.set(screen_name, screen_name + '_tweet_' + str(i), tweet['text'])
                    i += 1
                except Exception:
                    print tweet
    print "Data collection for %d users, and %d tweets" % (n_followers, n_tweets)
    with open('results.cfg', 'wb') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    main()