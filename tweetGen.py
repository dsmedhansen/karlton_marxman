# Generate tweets from texts

import markovify
from random import randrange

# Get raw as string
path = "/Users/Daniel/Google Drive/karlton_marxman/lit/"
friedman = path +"friedman_clean.txt"
marx = path +"marx_clean.txt"

with open(marx) as f:
	text = f.read()

# Build model
marx_model = markovify.Text(text, state_size=2)

with open(friedman) as f:
	text = f.read()

friedman_model = markovify.Text(text, state_size=2)

model_combo = markovify.combine([marx_model, friedman_model],[1,1])

f = open("tweets.txt", "w+")

for i in range(100000):

	tweet= model_combo.make_short_sentence(280)

	f.write(tweet + "\n")

f.close()


# import re

# text_file = open(path +"sample.txt", "w")

# with open(marx) as f:
# 	text = f.read()
# 	text = re.sub('[0-9]', ' ', text)
# 	text = re.sub('\n', ' ', text)
# 	text = re.sub(' +', ' ', text)
# 	text = re.sub('\t', ' ', text)
# 	text_file.write(text)
# 	print(text)

# text_file.close()