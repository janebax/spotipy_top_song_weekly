import os
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
from loguru import logger


def main():

    PLAYLIST_NAME = "top_songs_weekly"

    scope = "user-top-read playlist-modify-public playlist-modify-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    # Limitations of the Spotify API mean that we can only access listening history for '4 weeks' rather than suggesting a date range.
    range = "short_term"
    results = sp.current_user_top_tracks(time_range=range, limit=1)

    song_name = results["items"][0]["name"]
    artist_name = results["items"][0]["artists"][0]["name"]
    song_uri = results["items"][0]["uri"]

    logger.info(f"Top song is {song_name} by {artist_name}. Song URI: {song_uri}")

    logger.info(f"Checking if playlist {PLAYLIST_NAME} already exists...")
    playlists = sp.current_user_playlists(limit=50)  # Assumes no more than 50 playlists

    # Convert this to a while for efficiency and into a dict comprehension
    playlist_exists_flag = False
    for playlist in playlists["items"]:
        print(playlist["name"])
        if playlist["name"] == PLAYLIST_NAME:
            playlist_exists_flag = True
            logger.info(f"Playlist {PLAYLIST_NAME} already exists")

    if playlist_exists_flag == False:
        logger.info(f"Playlist {PLAYLIST_NAME} does not exist!")
        sp.user_playlist_create(
            os.environ["SPOTIPY_USERNAME"], PLAYLIST_NAME, public=True, description=""
        )
        logger.info(f"Created playlist {PLAYLIST_NAME}")

    playlists = sp.current_user_playlists(limit=50)  # Assumes no more than 50 playlists
    for playlist in playlists["items"]:
        if playlist["name"] == PLAYLIST_NAME:
            playlist_id = playlist["id"]

    sp.playlist_add_items(playlist_id, [song_uri], position=1)
    logger.info(f"Added song {song_name} by {artist_name} to {PLAYLIST_NAME}")

    logger.info("Finished script")


if __name__ == "__main__":
    main()
