import spotipy
from spotipy.oauth2 import SpotifyOAuth
from loguru import logger


def main():
    scope = "user-top-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    # Limitations of the Spotify API mean that we can only access listening history for '4 weeks' rather than suggesting a date range.
    range = "short_term"
    results = sp.current_user_top_tracks(time_range=range, limit=10)
    for i, item in enumerate(results["items"], start=1):
        logger.info(f'Track {i} | {item["name"]} || {item["artists"][0]["name"]}')

    logger.info("Finished script")


if __name__ == "__main__":
    main()
