Scripts to get most frequently played song on my Spotify account and add it to a playlist

## TODOs
- Currently the script can only get top songs from the past 4 weeks however we want to look at the last week. Next steps will be to update the song query to LastFM's API where I can get this information

## Spotify Setup

You will first need to set up a Developer account on your Spotify account here and create an app. Use this to get your SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET. Your username will be on a seperate account page for your Spotify account. You will need to specify the redirect URI to a location of your choice - to run this locally I have used 'http://localhost:8888/callback'

## Set environment variables

This allows the SpotifyOAuth object to get user information
```
export SPOTIPY_USERNAME='your-spotify-username'
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

## Running the script
To run the script, locate to the root (where this README.md is located) and the run the following in the terminal:
```
poetry install
poetry run python src/run.py
```