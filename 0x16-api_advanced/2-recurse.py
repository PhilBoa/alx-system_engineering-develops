#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles of hot articles.
        after (str): Parameter used for pagination.

    Returns:
        list: List containing the titles of all hot articles for the subreddit,
              or None if no results are found.
    """
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
            hot_list.append(post["data"]["title"])
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None


if __name__ == '__main__':
    top_ten = __import__('2-recurse').recurse

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        titles = recurse(sys.argv[1])
        if titles is not None:
            print(len(titles))
        else:
            print(None)
