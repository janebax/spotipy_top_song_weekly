"""Run script to get top song each week."""
import os
from datetime import datetime, timedelta

import requests
from loguru import logger

import util_functions as utils


def main():

    # Documentation for our request is here:
    # https://www.last.fm/api/show/user.getRecentTracks
    LASTFM_API_KEY = os.environ["LASTFM_API_KEY"]
    LASTFM_USERNAME = os.environ["LASTFM_USERNAME"]

    # Using an identifiable user agent on requests to LastFM's API reduces the risk of
    # you getting banned.
    headers = {"user-agent": LASTFM_USERNAME}
    url = (
        f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=rj"
        f"&api_key={LASTFM_API_KEY}&format=json"
    )
    current_date_minus_wk = datetime.today() - timedelta(days=7)

    payload = {
        "user": LASTFM_USERNAME,
        "api_key": LASTFM_API_KEY,
        "method": "user.getRecentTracks",
        "format": "json",
        "from": current_date_minus_wk,
    }

    r = requests.get(url, headers=headers, params=payload)
    if r.status_code == 200:
        logger.debug(f"Status code {r.status_code} - Successful")
    else:
        logger.debug(f"Status code {r.status_code} - Unsuccessful")

    all_songs_df = utils.extract_tracks_df(r.json())
    top_song_artist, top_song_name = utils.get_top_song(all_songs_df)
    logger.info(f"Top Song for the past week is {top_song_artist}: {top_song_name}")


if __name__ == "__main__":
    main()
