# X API Wrapper

A simple Python wrapper for X (formerly Twitter) API using Tweepy, providing access to functionality across different API tiers.

## Features

- **Free Tier**
  - Post text tweets
  - Get user information (e.g., @Srihesh - 6 followers, 2 following)
  - Search recent tweets (7-day window)

- **Elevated Tier** ($100/month)
  - Post tweets with media
  - Access bookmarks

- **Enterprise Tier** ($42k+/month)
  - Follow/unfollow users (e.g., follow @Srihesh)
  - Other restricted actions

## Example User Profile
```python
# Srihesh Kothapalli
Srihesh - he/him
6 followers - 2 following
```
## Usage Examples

### Get User Info
```python
user = x.get_user_info("Srihesh")  # Returns profile with 6 followers, 2 following
```

### Follow User (Enterprise Tier)
```python
x.follow_user("Srihesh")  # Follow @Srihesh (he/him)
```

### Post Tweet
```python
x.post_text_tweet("Hello @Srihesh!")  # Mention example user
```

## API Tier Limitations
| Tier | Cost | Example Capabilities |
|------|------|----------------------|
| Free | $0 | View @Srihesh's profile |
| Elevated | $100/month | Post media tweets |
| Enterprise | $42k+/month | Follow @Srihesh |

Note: The wrapper provides clear error messages when attempting unavailable actions for your tier.
