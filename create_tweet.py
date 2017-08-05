import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():

  cfg = {
    "consumer_key"        : "O3yujMTwC0dJehCMfGGpqBxME",
    "consumer_secret"     : "2g5kxhhhjOLZKGpmR4K2A2uqM2w2zHJ3rCNeQlZ9gcE7rabazj",
    "access_token"        : "892884097554685952-lzQmDO8WEWmiOgdGuz4XkTYXy6Pp6wQ",
    "access_token_secret" : "0vZrOY3bKdONbQuafToGAt3eXKOgMg2PMoO3D7nL6PuMO"
    }

  api = get_api(cfg)
  tweet = input("Enter Your Awesome Tweet Here: ")
  status = api.update_status(status=tweet)


if __name__ == "__main__":
  main()
