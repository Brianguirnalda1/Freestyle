# Write Tweets and List Recent Tweets - Python3

## Prerequisites

Follow the [Setup Guide](SETUP.md) to obtain and configure credentials for using the Tweepy service for twitter REST API And for configuring a machine to run this application.

## Installation

Install Python 3.x.

Install source code:

```shell
git clone https://github.com/Brianguirnalda1/Freestyle
cd Freestyle/
```

Install package dependencies:

```shell
# For Homebrew-installed Python 3.x on Mac OS:
pip3 install -r requirements.txt
# All others:
pip install tweepy
```

## Usage

Create a new tweet using your twitter handle and list your most recent tweets:

CD into the /Freestyle and open in Atom .
In the file titled create_tweet.py change the below config to your key variables:

```shell
cfg = {
  "consumer_key"        : "KEY_VARIABLE",
  "consumer_secret"     : "SECRET_VARIABLE",
  "access_token"        : "ACCESS_TOKEN_VARIABLE",
  "access_token_secret" : "ACCESS_TOKEN_SECRET_VARIABLE"
}
```
Save the script and run the app using your CLI to run the twitter_app.py:

```shell
python3 twitter_app.py
```
