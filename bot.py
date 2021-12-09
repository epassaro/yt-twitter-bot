import os
from random import choice
from textwrap import wrap

import tweepy
from pyyoutube import Api

from credentials import *


def get_random_id(api, playlist_id):
    """Get a random video ID from a YouTube Playlist

    Args:
        api (pyyoutube.api.API):
        playlist_id ([type]): YouTube Playlist ID
    """

    playlist = api.get_playlist_items(playlist_id=playlist_id, count=None)
    video_id_list = [i.snippet.resourceId.videoId for i in playlist.items]

    return choice(video_id_list)


def get_video_info(api, video_id):
    """Get URL, title and description from YouTube video

    Args:
        api (pyyoutube.api.API):
        video_id (str): YouTube video ID

    Returns:
        dict: Dictionary containing video info
    """

    video = api.get_video_by_id(video_id=video_id).to_dict()

    title = video["items"][0]["snippet"]["title"]
    descr = video["items"][0]["snippet"]["description"]
    url = f"https://youtu.be/{video_id}"

    return {"url": url, "title": title, "description": descr}


def tweet(api, info):
    """Tweet title, video URL and description

    Args:
        api (tweepy.api.API):
        info (dict): Dictionary with video info
    """

    url, title, descr = info.values()
    tweet = api.update_status(f"{title} {url}")

    if len(descr) <= 280:
        reply = api.update_status(status=f"{descr}", in_reply_to_status_id=tweet.id)

    else:
        strings = wrap(descr, 270)
        n = len(strings)

        reply = api.update_status(
            status=f"{strings[0]} ({1}/{n})", in_reply_to_status_id=tweet.id
        )

        for i, string in enumerate(strings[1:]):
            reply = api.update_status(
                status=f"{string} ({i+2}/{n})", in_reply_to_status_id=reply.id
            )


def follow_back(api):
    """Follow back bot followers

    Args:
        api (tweepy.api.API):
    """

    followers = api.get_follower_ids()
    following = api.get_friend_ids() + api.outgoing_friendships()

    _ = [
        api.create_friendship(user_id=str(user))
        for user in followers
        if user not in following
    ]


if __name__ == "__main__":

    auth = tweepy.OAuthHandler(TW_API_KEY, TW_API_KEY_SECRET)
    auth.set_access_token(BOT_OAUTH_TOKEN, BOT_OAUTH_TOKEN_SECRET)
    tw_api = tweepy.API(auth)

    try:
        tw_api.verify_credentials()
        print("Authentication OK")

    except:
        print("Error during authentication")

    yt_api = Api(api_key=YT_API_KEY)
    video_id = get_random_id(yt_api, PLAYLIST_ID)
    info = get_video_info(yt_api, video_id)

    tweet(tw_api, info)
    follow_back(tw_api)
