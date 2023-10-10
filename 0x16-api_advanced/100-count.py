#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript, but java should
not)
"""
import requests
import sys


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the title of hot articles, and
    counts the occurrences of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): Parameter used for pagination.
        counts (dict): Dictionary to store word counts.

    Returns:
        dict: Dictionary containing the word counts.
    """
    if counts is None:
        counts = {}
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) "
            "Gecko/20100101 Firefox/92.0"
            )
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        after = data.get("data", {}).get("after", None)
        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                if f" {word.lower()} " in f" {title} ":
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1
        if after is not None:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))
            return counts
    else:
        return None


if __name__ == '__main__':
    count = __import__('100-count').count_words

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(
            sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
