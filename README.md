# CSCA08A1 **Tweet Analyser**

This assignment is based on the social network company Twitter. Twitter allows users to read and post tweets that are between 1 and 280 characters long, inclusive. In this assignment, you will be writing functions that (we imagine) are part of the programs that manage Twitter feeds.

**Some terminology**

We will use the following terms in this assignment.

**tweet**: A message posted on Twitter. For our assignment, a valid tweet is between 1 and MAX_TWEET_LENGTH characters long (inclusive). MAX_TWEET_LENGTH is a constant.

**tweet word**: A word in a tweet. For our assignment, a valid tweet word contains only alphanumeric characters and underscores. For example, pink_elephant is a valid tweet word, while bits&pieces is not (In fact, bits&pieces has two valid tweet words, bits and pieces, with an ampersand (&) between them.)

**hashtag**: A word in a tweet that begins with the hash symbol. Twitter uses the number sign (#) as the hash symbol. For our assignment, we'll use the constant HASHTAG_SYMBOL to represent the hash symbol. Hashtags are used to label important words or terms in a tweet. A valid hashtag has the hash symbol as its first character and the rest of the characters form a valid tweet word. In other words, a hashtag begins with the hash symbol, and contains all alphanumeric characters and underscores up to (but not including) the first non-alphanumeric character (such as space, punctuation, etc.) or the end of the tweet. A hashtag either begins a tweet or is preceded by a character that is not alphanumeric and is not an underscore. A hashtag must contain at least one alphanumeric character.

Note that a hashtag is not a valid tweet word, because it has the hash symbol as its first character.

**mention**: A word in a tweet that begins with the mention symbol. Twitter uses the at-sign (@) as the mention symbol. For our assignment, we'll use the constant MENTION_SYMBOL to represent the mention symbol. Mentions are used to direct a message at or about a particular Twitter user, so the word should be a Twitter username (but for the purposes of this assignment, we will not check if the word that follows the MENTION_SYMBOL is a real username — we'll just assume it). For our purposes, the definition of a mention is very similar to that of a hashtag. A valid mention has the mention symbol as its first character and the rest of the characters form a valid tweet word. In other words, a mention begins with the at-sign, and contains all alphanumeric characters and underscores up to (but not including) the first non-alphanumeric character (such as space, punctuation, etc.) or the end of the tweet. A mention either begins a tweet or is preceded by a character that is not alphanumeric and is not an underscore. A mention must contain at least one alphanumeric character.

Note that a mention is not a valid tweet word, because it has the mention symbol as its first character. Here are some more interesting examples of how we will treat valid tweet words, hashtags, and mentions in this
assignment.
