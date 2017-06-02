TWEET_LENGTH = 140


def total_tweets(text: str) -> int:
    len_txt = len(text)
    num_tweets = 0
    sum_prefix = 0
    sum_sufix = 0

    while num_tweets * TWEET_LENGTH - sum_prefix < len_txt:
        num_tweets += 1

        len_num_tweets = len(str(num_tweets))
        len_num_tweets_ant = len(str(num_tweets - 1))

        prefix_len = 2 * (len_num_tweets + 1)
        sufix_len = TWEET_LENGTH - prefix_len
        diff = (num_tweets - 1) * (len_num_tweets - len_num_tweets_ant)

        # CALCULATION
        sum_prefix += (prefix_len + diff)
        sum_sufix += (sufix_len - diff)

    return num_tweets


def colored_index(i: int, total: int) -> str:
    ''' Fancy color output '''
    blue = '\033[94m'
    bold = '\033[1m'
    end = '\033[0m'

    return '{:s}{:s}{:d}/{:d}{:s}{:s}'.format(blue, bold, i, total, end, end)


def get_tweets(text: str=None, color: bool=True) -> list:
    total = total_tweets(text)
    pos = 0
    tweets = []

    for i in range(1, total + 1):
        prefix = len(str(i)) + len(str(total)) + 2
        pos_ant = pos
        pos = pos + TWEET_LENGTH - prefix

        if color:
            tweets.append('{:s} {:s}'.format(colored_index(i, total), text[pos_ant:pos]))
        else:
            tweets.append('{:d}/{:d} {:s}'.format(i, total, text[pos_ant:pos]))

    return tweets
