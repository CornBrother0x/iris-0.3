
import tweepy

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(f'Tweet text: {tweet["data"]["text"]}')

printer = MyStream("AAAAAAAAAAAAAAAAAAAAAEZBoAEAAAAA4%2BvGqNDLRDbHJcsDTx7zCCg5Wig%3Da60dRxX6LaQ8q4LVR0fHtJx1NThmYRLhzvTNSy8L4351X77YYD")

# Fetch existing rules
existing_rules = printer.get_rules()

# Extract rule IDs
rule_ids = [rule['id'] for rule in existing_rules['data']]

# Delete existing rules
printer.delete_rules(ids=rule_ids)

# Set a new rule
new_rule = tweepy.StreamRule(value="from:kittysquiddy", tag="tweets from Twitter Dev")
printer.add_rules([new_rule])

# Start streaming
printer.sample()
