# yt-twitter-bot
[![tweet](https://github.com/epassaro/yt-twitter-bot/actions/workflows/tweet.yml/badge.svg?branch=main)](https://github.com/epassaro/yt-twitter-bot/actions/workflows/tweet.yml)

A Twitter bot that posts random videos from a YouTube channel or playlist


### Usage

Fork the repository and sign up for developer accounts.

- [Twitter Developer Account](https://developer.twitter.com/en/apply-for-access)
- [YouTube API Key](https://www.youtube.com/watch?v=N18czV5tj5o&ab_channel=WebbyFan.com)
> See also: [How to Create Multiple Bots With a Single Twitter Developer Account](https://medium.com/geekculture/how-to-create-multiple-bots-with-a-single-twitter-developer-account-529eaba6a576)

Then, add a secret named `DOTENV` to your repository with the following keys:

```
APP_API_KEY=
APP_API_SECRET_KEY=
BOT_OAUTH_TOKEN=
BOT_OAUTH_TOKEN_SECRET=
YT_API_KEY=
YT_PLAYLIST_ID=
```

The bot is scheduled to run hourly on GitHub Actions, does not require extra deployment. You can change how the bot is triggered from [`.github/workflows/tweet.yml`](.github/workflows/tweet.yml).

### Development

1. Install the dependencies: `python>=3.8` `python-dotenv` `python-youtube` `tweepy`
2. Create a `.env` file at the root of the repository with the same keys described above
3. Run `python bot.py`
