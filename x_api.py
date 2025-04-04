import tweepy
import os
from datetime import datetime


class XAPI:
    def __init__(self):
        self.client = tweepy.Client(
            bearer_token=os.getenv('X_BEARER_TOKEN'),
            consumer_key=os.getenv('X_API_KEY'),
            consumer_secret=os.getenv('X_API_SECRET'),
            access_token=os.getenv('X_ACCESS_TOKEN'),
            access_token_secret=os.getenv('X_ACCESS_TOKEN_SECRET'),
            wait_on_rate_limit=True
        )

        self.legacy_api = tweepy.API(
            tweepy.OAuth1UserHandler(
                os.getenv('X_API_KEY'),
                os.getenv('X_API_SECRET'),
                os.getenv('X_ACCESS_TOKEN'),
                os.getenv('X_ACCESS_TOKEN_SECRET')
            ),
            wait_on_rate_limit=True
        )

    def post_text_tweet(self, text):
        try:
            response = self.client.create_tweet(text=text)
            return response.data
        except tweepy.TweepyException as e:
            return f"Error: {e}"

    def get_user_info(self, username):
        try:
            user = self.client.get_user(
                username=username,
                user_fields=["created_at", "description", "public_metrics"]
            )
            return user.data
        except tweepy.TweepyException as e:
            return f"Error: {e}"

    def search_tweets(self, query, limit=10):
        try:
            tweets = self.client.search_recent_tweets(
                query=query,
                max_results=limit,
                tweet_fields=["created_at", "public_metrics"]
            )
            return tweets.data
        except tweepy.TweepyException as e:
            return f"Error: {e}"

    def post_media_tweet(self, text, image_path):
        try:
            media = self.legacy_api.media_upload(image_path)
            response = self.client.create_tweet(
                text=text,
                media_ids=[media.media_id]
            )
            return response.data
        except tweepy.TweepyException as e:
            return f"Error: {e} (Elevated access required)"

    def get_bookmarks(self):
        try:
            bookmarks = self.client.get_bookmarks(
                tweet_fields=["created_at", "author_id"],
                expansions=["author_id"],
                max_results=20
            )
            return bookmarks.data
        except tweepy.TweepyException as e:
            return f"Error: {e} (Elevated access required)"

    def follow_user(self, username):
        """Follow a user (requires Enterprise tier access)"""
        try:
            # First get the user ID from username
            user = self.client.get_user(username=username)
            if not user or not user.data:
                return f"Error: Could not find user {username}"

            user_id = user.data.id
            response = self.client.follow_user(user_id)

            if response and hasattr(response, 'data') and response.data:
                return f"Successfully followed user {username}"
            else:
                return f"Error following user {username}"
        except tweepy.TweepyException as e:
            error_message = str(e).lower()
            if "forbidden" in error_message or "unauthorized" in error_message:
                return "Error: X now requires Enterprise tier for follow actions"
            return f"Error: {e}"

    def unfollow_user(self, username):
        """Unfollow a user (requires Enterprise tier access)"""
        try:

            user = self.client.get_user(username=username)
            if not user or not user.data:
                return f"Error: Could not find user {username}"

            user_id = user.data.id


            response = self.client.unfollow_user(user_id)

            if response and hasattr(response, 'data') and response.data:
                return f"Successfully unfollowed user {username}"
            else:
                return f"Error unfollowing user {username}"
        except tweepy.TweepyException as e:
            error_message = str(e).lower()
            if "forbidden" in error_message or "unauthorized" in error_message:
                return "Error: X now requires Enterprise tier for unfollow actions"
            return f"Error: {e}"

