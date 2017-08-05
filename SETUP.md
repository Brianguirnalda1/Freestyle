# Setup Guide

Create a Twitter Account. Add your phone number to your Twitter Account, or else you won't be allowed to create a Twitter Application.

Then while logged in to Twitter, visit the Twitter Application Management Console (https://apps.twitter.com/) and click "Create New App" to create a new Twitter Application.

### Computing Environment Setup

After creating a new application, click on the "Keys and Access Tokens" tab, and note the application's "Consumer Key" and "Consumer Secret". Scroll down and generate a new Access Token and note its "Access Token" and "Access Token Secret" values. Store these four values in environment variables like the following commands and inputing your api/ access information after the equal sign(mac):

```shell
echo export "TWITTER_API_KEY=xxxx_api_key_xxxx" >> ~/.bash_profile
echo export "TWITTER_API_SECRET=xxxx_api_secret_xxxx" >> ~/.bash_profile
echo export "TWITTER_ACCESS_TOKEN=xxxx_access_token_xxxx" >> ~/.bash_profile
echo export "TWITTER_ACCESS_TOKEN_SECRET=xxxx_access_token_secret_xxxx" >> ~/.bash_profile
```

Remember to restart your Terminal after installing the environmental variables.
