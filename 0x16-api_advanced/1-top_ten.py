#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
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
        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)


if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
