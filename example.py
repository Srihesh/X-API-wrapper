from x_api import XAPI
from dotenv import load_dotenv
import os


def main():
    load_dotenv()

    x = XAPI()

    print("=== Free Tier Functions ===")
    print("Posting text tweet:")
    print(x.post_text_tweet("<your text to post>"))

    print("\nGetting user info:")
    print(x.get_user_info("<user name>"))

    print("\nSearching tweets:")
    tweets = x.search_tweets("<name>", 2)
    if isinstance(tweets, list):
        for tweet in tweets:
            print(f"{tweet.id}: {tweet.text[:50]}...")

    print("\n Elevated Tier Functions ")
    print("tweet with media(requires elevated access):")
    print(x.post_media_tweet("<your text with media>", "<image link>"))

    print("\nviewing bookmakrs (requires elevated access):")
    print(x.get_bookmarks())

    print("\n=== Enterprise Tier Functions ===")
    print("follow user(requires enterprise access):")
    print(x.follow_user("<username>"))

    print("\nUnfollow user (requires enterprise access):")
    print(x.unfollow_user("<user name>"))


if __name__ == "__main__":
    main()