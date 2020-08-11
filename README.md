# CSCA08A1

Tweet Analyser

This assignment is based on the social network company Twitter. Twitter allows users to read and post tweets that are between 1 and 280 characters long, inclusive. In this assignment, you will be writing functions that (we imagine) are part of the programs that manage Twitter feeds.

Some terminology

We will use the following terms in this assignment.
tweet: A message posted on Twitter. For our assignment, a valid tweet is between 1 and MAX_TWEET_LENGTH characters long (inclusive). MAX_TWEET_LENGTH is a constant.

tweet word: A word in a tweet. For our assignment, a valid tweet word contains only alphanumeric characters and underscores. For example, pink_elephant is a valid tweet word, while bits&pieces is not (In fact, bits&pieces has two valid tweet words, bits and pieces, with an ampersand (&) between them.)

hashtag: A word in a tweet that begins with the hash symbol. Twitter uses the number sign (#) as the hash symbol. For our assignment, we'll use the constant HASHTAG_SYMBOL to represent the hash symbol. Hashtags are used to label important words or terms in a tweet. A valid hashtag has the hash symbol as its first character and the rest of the characters form a valid tweet word. In other words, a hashtag begins with the hash symbol, and contains all alphanumeric characters and underscores up to (but not including) the first non-alphanumeric character (such as space, punctuation, etc.) or the end of the tweet. A hashtag either begins a tweet or is preceded by a character that is not alphanumeric and is not an underscore. A hashtag must contain at least one alphanumeric character.
#UofT, #cscA08, and #Go_Raptors are three examples of hashtags on Twitter.
Note that a hashtag is not a valid tweet word, because it has the hash symbol as its first character.

mention: A word in a tweet that begins with the mention symbol. Twitter uses the at-sign (@) as the mention symbol. For our assignment, we'll use the constant MENTION_SYMBOL to represent the mention symbol. Mentions are used to direct a message at or about a particular Twitter user, so the word should be a Twitter username (but for the purposes of this assignment, we will not check if the word that follows the MENTION_SYMBOL is a real username — we'll just assume it). For our purposes, the definition of a mention is very similar to that of a hashtag. A valid mention has the mention symbol as its first character and the rest of the characters form a valid tweet word. In other words, a mention begins with the at-sign, and contains all alphanumeric characters and underscores up to (but not including) the first non-alphanumeric character (such as space, punctuation, etc.) or the end of the tweet. A mention either begins a tweet or is preceded by a character that is not alphanumeric and is not an underscore. A mention must contain at least one alphanumeric character.
@redcrosscanada, @UN_Women, and @UofTGrad2019 are three examples of Twitter mentions.
Note that a mention is not a valid tweet word, because it has the mention symbol as its first character. Here are some more interesting examples of how we will treat valid tweet words, hashtags, and mentions in this
assignment.

In the tweet
     Raptors win championship,#NBAFINALS, Go @Raptors!!!     #WeTheNorth
we have four valid tweet words (Raptors, win, championship, and Go), two hashtags (#NBAFINALS and #WeTheNorth), and one mention (@Raptors). It is important to note that in this example there is no space between the first comma and the hashtag #NBAFINALS, there is a comma immediately following the hashtag #NBAFINALS, there are three exclamation marks immediately following the mention @Raptors, and there are more than one space after the exclamation marks. All these are valid in a tweet. Also note that the first occurrence of the word Raptors is not considered to be a mention, because it does not have the mention symbol.


Function name:
(Parameter types) -> Full Description (paraphrase to get a proper docstring description)
Return type
    is_valid_tweet: (str) -> bool
add_hashtag: (str, str) -> str
is_mentioned: (str, str) -> bool
num_tweets_required: (str) -> int
Using Constants
The parameter represents a potential tweet. The function should return True if and only if the tweet contains between 1 and MAX_TWEET_LENGTH characters, inclusive.
The first parameter represents a valid tweet. The second parameter represents a valid tweet word.
Appending a space, a hash symbol, and the tweet word to the end of the original tweet will result in a potential tweet. If the potential tweet is a valid tweet, the function should return the potential tweet. If the potential tweet is not a valid tweet, the function should return the original tweet.
For example (assuming the hash symbol is '#'), if the first argument is 'I like' and the second argument is 'cscA08', then the function should return 'I like #cscA08', if MAX_TWEET_LENGTH is at least 14. Otherwise, it should return 'I like'.
The first parameter represents a valid tweet, and the second parameter represents a valid tweet word. This function should return True if and only if the tweet contains a mention made up of the mention symbol and the tweet word. For example (assuming the mention symbol is '@'), if the first argument is 'Go @Raptors!', and the second argument is 'Raptors', then the function should return True.
Hint: This function is very similar to the function contains_hashtag. What can you do to avoid writing the same code twice?
The parameter represents a message. This function should return the minimum number of tweets that would be required to communicate the entire message. Recall the maximum length of a tweet is MAX_TWEET_LENGTH.
Hint: The ceil function in the math module is useful here.
Functions to write for A1
     compare_tweet_lengths: (str, str) -> int
The two parameters represent valid tweets. This function must return one of three integers: 1 (if the first tweet is longer than the second), -1 (if the second tweet is longer than the first), or 0 (if the tweets have the same length).
         contains_hashtag: (str, str) -> bool
The first parameter represents a valid tweet, and the second parameter represents a valid tweet word. This function should return True if and only if the tweet contains a hashtag made up of the hash symbol and the tweet word. For example (assuming the hash symbol is '#'), if the first argument is 'I like #cscA08', and the second argument is 'cscA08', then the function should return True.
Notes: If the first argument is 'I like #cscA08', and the second argument is 'csc', then the function should return False. Also, if the first argument is 'I like #cscA08, #mat137, and #phl101', and the second argument is cscA08, the function should return True.
Hint: Use the helper function clean that is provided in the starter code.
    
add_mention_exclusive: (str, str) -> str
The first parameter represents a valid tweet and the second parameter represents a valid tweet word. Appending a space, a mention symbol, and the tweet word to the end of the original tweet will result in a potential tweet. If the potential tweet is valid and the original tweet contains the given tweet word, the function should return the potential tweet. In all other cases, the function should return the original tweet. Note that if the tweet word is mentioned in the original tweet (i.e., it appears with a MENTION_SYMBOL as a first character), then the function should return the original tweet.
For example (assuming the mention symbol is '@'), if the first argument is 'Go Raptors!' and the second argument is 'Raptors', then the function should return 'Go Raptors! @Raptors'. If, on the other hand, the first argument is 'Go @Raptors!' and the second argument is 'Raptors', then the function should return the original tweet 'Go @Raptors!'.
Hint: Can you use one of your other functions as a helper function?
     
