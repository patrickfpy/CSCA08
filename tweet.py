"""Assignment 1.
"""

import math

# Maximum number of characters in a valid tweet.
MAX_TWEET_LENGTH = 50

# The first character in a hashtag.
HASHTAG_SYMBOL = '#'

# The first character in a mention.
MENTION_SYMBOL = '@'

# Underscore is the only non-alphanumeric character that can be part
# of a word (or username) in a tweet.
UNDERSCORE = '_'

SPACE = ' '


def is_valid_tweet(text: str) -> bool:
    """Return True if and only if text contains between 1 and
    MAX_TWEET_LENGTH characters (inclusive).

    >>> is_valid_tweet('Hello Twitter!')
    True
    >>> is_valid_tweet('')
    False
    >>> is_valid_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    False

    """
    
    return 0 < len(text) <= MAX_TWEET_LENGTH


def compare_tweet_lengths(text1: str, text2: str) -> int:
    """Return 1 iff the text1 is longer than the text2. Return -1 iff the 
    text2 is longer than text1. Return 0 otherwise.
    
    Precondition: 0 < len(text1) <= MAX_TWEET_LENGTH
                  0 < len(text2) <= MAX_TWEET_LENGTH
    
    >>> compare_tweet_lengths('lonnnnnnnnnnnnnnnnger', 'shorter')
    1
    >>> compare_tweet_lengths('shorter', 'lonnnnnnnnnnnnnnnnger')
    -1
    >>> compare_tweet_lengths('same', 'same')
    0
    
    """
    
    if len(text1) > len(text2):
        return 1
    elif len(text2) > len(text1):
        return -1
    return 0


def add_hashtag(text: str, word: str) -> str:
    """Return text, SPACE, HASHTAG_SYMBOL and word iff text is valid tweet 
    and word is valid tweet word. Return text otherwise.
    
    Precondtion: 0 < len(text) <= MAX_TWEET_LENGTH
                 valid tweet word
    
    >>> add_hashtag(2 *'more or equal than MAX_TWEET_LENGTH', 'Nohashtag')
    'more or equal than MAX_TWEET_LENGTHmore or equal than MAX_TWEET_LENGTH'
    
    >>> add_hashtag('less than MAX_TWEET_LENGTH', 'Yeshashtag')
    'less than MAX_TWEET_LENGTH #Yeshashtag'
    
    """
    
    if len(text + SPACE + HASHTAG_SYMBOL + word) < MAX_TWEET_LENGTH:
        return text + SPACE + HASHTAG_SYMBOL + word
    return text


def contains_word(text: str, word: str, symbol: str) -> bool:
    """Return True iff text contains the word and corresponding symbol.
    
    Precondtion: 0 < len(text) <= MAX_TWEET_LENGTH
                 valid tweet word
    
    >>> contains_word('I like #cscA08', 'cscA08')
    True
    
    >>> contains_word('I like #cscA08', 'csc')
    False
    
    """
    
    return symbol + word + SPACE in clean(text) + SPACE 
       

def contains_hashtag(text: str, word: str) -> bool:
    """Return True iff text contains HASHTAG_SYMBOL and word.

    Precondition: 0 < len(text) <= MAX_TWEET_LENGTH
                  valid tweet word
    
    >>> contains_hashtag('I like #cscA08', 'cscA08')
    True 
    
    >>> contains_hashtag('I like #cscA08', 'csc')
    False
    
    """
    
    return contains_word(text, word, HASHTAG_SYMBOL) 
    

def is_mentioned(text: str, word: str) -> bool:
    """Return True iff text contains MENTION_SYMBOL and word.
    
    Precondtion: 0 < len(text) <= MAX_TWEET_LENGTH
                 valid tweet word
    
    >>> is_mentioned('Go @Raptors', 'Raptors')
    True
    
    >>> is_mentioned('Go @Raptors', 'Rap')
    False
    
    """
    
    return contains_word(text, word, MENTION_SYMBOL) 


def add_mention_exclusive(text: str, word: str) -> str:
    """ Return text, SPACE, MENTION_SYMBOL iff text contains word. 
    Return text otherwise.
    
    Precondition: 0 < len(text) <= MAX_TWEET_LENGTH
                  valid tweet word
    
    >>> add_mention_exclusive('Go Raptors!', 'Raptors')
    'Go Raptors! @Raptors'
    
    >>> add_mention_exclusive('Go @Raptors!', 'Raptors')
    'Go @Raptors'
    
    """
    if is_mentioned(text, word):
        return text 
    elif len(text + SPACE + MENTION_SYMBOL + word) < MAX_TWEET_LENGTH:
        return text + SPACE + MENTION_SYMBOL + word
    return text
   

def num_tweets_required(message: str) -> int:
    """ Return the ceiling of the number which is message / MAX_TWEET_LENGTH.
    
    >>> num_tweets_required('abcdefghijklmnopqrstuvwxyz')
    1
    
    >>> num_tweets_required(10 * 'abcdefghijklmnopqrstuvwxyz')
    6
    
    """
    return math.ceil(len(message) / MAX_TWEET_LENGTH)


def get_nth_tweet(message: str, number: int) -> str:
    """ Return ( number + 1)th sequence of tweet, and message is split to 
    several sequenve of tweet base on MAX_TWEET_LENGTH
    
    Precondition: number >= 0
    
    >>> get_nth_tweet('u of t is the best', 0)
    
    >>> get_nth_tweet(5 * 'abcdefghijklmnopqrstuvwxyz', 2)
    wxyzabcdefghijklmnopqrstuvwxyz
    
    """
    if len(message) < number * MAX_TWEET_LENGTH:
        return ''
    elif len(message) > (number + 1) * MAX_TWEET_LENGTH:
        return message[number * MAX_TWEET_LENGTH : (number + 1) * \
                       MAX_TWEET_LENGTH]
    return message[number * MAX_TWEET_LENGTH : len(message)]


def clean(text: str) -> str:
    """Return text with every non-alphanumeric character, except for
    HASHTAG_SYMBOL, MENTION_SYMBOL, and UNDERSCORE, replaced with a
    SPACE, and each HASHTAG_SYMBOL replaced with a SPACE followed by
    the HASHTAG_SYMBOL, and each MENTION_SYMBOL replaced with a SPACE
    followed by a MENTION_SYMBOL.

    >>> clean('A! lot,of punctuation?!!')
    'A  lot of punctuation   '
    >>> clean('With#hash#tags? and@mentions?in#twe_et #end')
    'With #hash #tags  and @mentions in #twe_et  #end'
    """

    clean_str = ''
    for char in text:
        if char.isalnum() or char == UNDERSCORE:
            clean_str = clean_str + char
        elif char == HASHTAG_SYMBOL or char == MENTION_SYMBOL:
            clean_str = clean_str + SPACE + char
        else:
            clean_str = clean_str + SPACE
    return clean_str
