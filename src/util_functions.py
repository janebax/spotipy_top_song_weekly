"""Util functions used by run.py ."""
from datetime import datetime

import pandas as pd


def extract_tracks_df(json_output: dict):
    """Convert json output from LastFM API to a pd.DataFrame.

    Returns a pd.Dataframe with a single row for a track played.
    """
    track_list = json_output["recenttracks"]["track"]
    track_dict = {}
    for index, track in enumerate(track_list):
        track_dict[index] = extract_single_track(track)

    track_df = pd.DataFrame.from_dict(track_dict, orient="index")
    return track_df


def extract_single_track(track_dict: dict):
    """Extract the artist, song_title and listen_date for a single track."""
    artist = track_dict["artist"]["#text"]
    song_title = track_dict["name"]
    listen_date_uts = track_dict["date"]["uts"]
    listen_date = convert_unix_timestamp_to_aws_format(listen_date_uts)
    return {"artist": artist, "song_title": song_title, "listen_date": listen_date}


def convert_unix_timestamp_to_aws_format(uts: str):
    """Convert UTS time stamp to format for AWS Athena: yyyy-MM-dd HH:mm:ss ."""
    ts = int(uts)
    converted_time = datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    return converted_time


def get_top_song(all_songs_df: pd.DataFrame):
    """Return the most popular song as a tuple (artist, song_title)."""
    counts = (
        all_songs_df.groupby(["artist", "song_title"])
        .count()
        .sort_values(["listen_date", "artist"], ascending=False)
    ).reset_index()
    top_song = counts.head(1)
    return (top_song["artist"][0], top_song["song_title"][0])
