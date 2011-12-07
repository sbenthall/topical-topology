
## GET SNOWBALL PARAMETERS

# User ID of the 'ego' of the snowball
EGO = 14437549

#Number of hops for snowball collection
HOPS = 4


CONNECTION_NO = 10


METADATA_PATH = "accounts/metadata/"
FRIENDS_PATH = "accounts/friends/"
FOLLOWERS_PATH = "accounts/followers/"

#when filter followers, true: pick randomly,
 #false: pick from beginning
FILTER_RANDOM = False 


## GET LOG PARAMETERS

SLEEP = 5
LOG_PATH = "log/"

SNOWBALL_PATH = "snowball-%d-%d.json" % (EGO, HOPS)


## EXTRACT PARAMETERS

AGGREGATE_TWEETS = True

DUMP_PATH = "sample-data/"
DUMP_FILE = "sample-data/tweets.txt"

CUTOFF = 200


## INFER TOPICS PARAMETERS

MALLET_INPUT_FILE = "input.mallet"
INFERENCER_FILE = "inferencer.mallet"
OUTPUT_STATE = "topic-state.gz"
INFERRED_FILE = "inferred-topics.txt"
TOPIC_KEYS_FILE = "topic-keys.txt"
NUM_TOP_WORDS = 30


NUM_TOPICS = 10
OPTIMIZE_INTERVAL = 200


## CORRELATE PARAMETERS


