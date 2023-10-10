#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers (not active users,
total subscribers) for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for
    a subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers of the subreddit, or 0 if invalid subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) "
            "Gecko/20100101 Firefox/92.0"
            )
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0


if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
