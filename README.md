# X API Wrapper

A simple Python wrapper for X (formerly Twitter) API using Tweepy, providing access to functionality across different API tiers.

## Features

- **Free Tier**
  - Post text tweets
  - Get user information
  - Search recent tweets (7-day window)

- **Elevated Tier** ($100/month)
  - Post tweets with media
  - Access bookmarks

- **Enterprise Tier** ($42k+/month)
  - Follow/unfollow users
  - Other restricted actions

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/x-api-wrapper.git
   cd x-api-wrapper
   ```

2. Install required packages:
   ```
   pip install tweepy python-dotenv
   ```

3. Create a `.env` file with your X API credentials (use the template provided in `.env.template`):
   ```
   X_BEARER_TOKEN=your_bearer_token_here
   X_API_KEY=your_api_key_here
   X_API_SECRET=your_api_secret_here
   X_ACCESS_TOKEN=your_access_token_here
   X_ACCESS_TOKEN_SECRET=your_access_token_secret_here
   ```

## Usage

### Basic Usage

```python
from x_api import XAPI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize API wrapper
x = XAPI()

# Post a tweet
response = x.post_text_tweet("Hello from X API Wrapper!")
print(response)

# Get user information
user = x.get_user_info("twitter")
print(user)

# Search tweets
tweets = x.search_tweets("Python", 5)
for tweet in tweets:
    print(f"{tweet.id}: {tweet.text}")
```

### Enterprise Tier Functionality

If you have Enterprise tier access, you can use the following functions:

```python
# Follow a user
result = x.follow_user("username")
print(result)  # Should show "Successfully followed user username"

# Unfollow a user
result = x.unfollow_user("username")
print(result)  # Should show "Successfully unfollowed user username"
```

Without Enterprise access, these methods will return informative error messages.

## Full Example

Run the included `example.py` file to see all features in action:

```
python example.py
```

## API Tier Limitations(source - X API developer platform

This wrapper is designed to work with all API tiers, but certain functionality requires specific access levels:

1. **Free Tier**: Basic read and write operations
2. **Elevated Tier** ($100/month): Media uploads, bookmarks, and higher rate limits
3. **Enterprise Tier** ($42k+/month): Follow/unfollow functionality and other restricted actions

The wrapper will provide clear error messages when attempting to use features not available in your current tier.
