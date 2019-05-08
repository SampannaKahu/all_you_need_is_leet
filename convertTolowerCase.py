originalFile = open('data/mondal_json_v2')
originalTweets = originalFile.read().splitlines()
originalFile.close()
originalTweets = [tweet.lower() for tweet in originalTweets]

with open('data/mondal_json_v2_lowercased', 'w') as f:
    for item in originalTweets:
        f.write("%s\n" % item)
