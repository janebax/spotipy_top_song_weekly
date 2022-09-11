An app to get most frequently played song on my Spotify account in a given week and add it to a playlist

## TODOs
- Add in Spotify code to Search for the song and add to playlist

## LastFM Setup

You will first need to set up an account with LastFM in order to get the listening date associated with your songs (it's not available on the Spotify API). When set up with LastFM, connect it to your Spotify account.

## Set environment variables

This allows the the app to get information from the LastFM api
```
export LASTFM_USERNAME='your-lastfm-username'
export LASTFM_API_KEY='your-lastfmgi-api-key'
```

## Running the script
To run the script, locate to the root (where this README.md is located) and the run the following in the terminal:
```
poetry install
poetry run python src/run.py
```

## Tests
To run the tests run the following command from root:
```
poetry run pytest tests/
```
