import pandas as pd
import pytest


@pytest.fixture()
def example_json():
    example_json = {
        "recenttracks": {
            "track": [
                {
                    "artist": {
                        "mbid": "bdc343bd-1c45-4a5d-b956-c4429f3dbba5",
                        "#text": "Blossoms",
                    },
                    "streamable": "0",
                    "image": [
                        {
                            "size": "small",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/34s/1976e6c8659480153ec82086a3a02b3c.jpg",
                        },
                        {
                            "size": "medium",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/64s/1976e6c8659480153ec82086a3a02b3c.jpg",
                        },
                        {
                            "size": "large",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/174s/1976e6c8659480153ec82086a3a02b3c.jpg",
                        },
                        {
                            "size": "extralarge",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/1976e6c8659480153ec82086a3a02b3c.jpg",
                        },
                    ],
                    "mbid": "31cb91f9-3734-48e3-b7b0-051ff1fd843f",
                    "album": {
                        "mbid": "571ab3dd-8037-4667-b58a-21bd6976af14",
                        "#text": "Foolish Loving Spaces (Deluxe Edition)",
                    },
                    "name": "Your Girlfriend",
                    "url": "https://www.last.fm/music/Blossoms/_/Your+Girlfriend",
                    "date": {"uts": "1662621238", "#text": "08 Sep 2022, 07:13"},
                },
                {
                    "artist": {
                        "mbid": "90744b3e-363a-458e-8da1-e3e392a489c4",
                        "#text": "Wet Leg",
                    },
                    "streamable": "0",
                    "image": [
                        {
                            "size": "small",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/34s/14e7090ffabb2ecd5e9bf8c8f5a108b9.jpg",
                        },
                        {
                            "size": "medium",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/64s/14e7090ffabb2ecd5e9bf8c8f5a108b9.jpg",
                        },
                        {
                            "size": "large",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/174s/14e7090ffabb2ecd5e9bf8c8f5a108b9.jpg",
                        },
                        {
                            "size": "extralarge",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/14e7090ffabb2ecd5e9bf8c8f5a108b9.jpg",
                        },
                    ],
                    "mbid": "1a5fa5c9-3db5-40ed-ad5d-b3a56d551c87",
                    "album": {
                        "mbid": "949c1b3a-db54-4302-90b3-ec8d0f70a45b",
                        "#text": "Wet Leg",
                    },
                    "name": "Wet Dream",
                    "url": "https://www.last.fm/music/Wet+Leg/_/Wet+Dream",
                    "date": {"uts": "1662620462", "#text": "08 Sep 2022, 07:01"},
                },
                {
                    "artist": {"mbid": "", "#text": "Sam Fender"},
                    "streamable": "0",
                    "image": [
                        {
                            "size": "small",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/34s/a6e7c9f329c60f85427dac2fa1be897e.png",
                        },
                        {
                            "size": "medium",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/64s/a6e7c9f329c60f85427dac2fa1be897e.png",
                        },
                        {
                            "size": "large",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/174s/a6e7c9f329c60f85427dac2fa1be897e.png",
                        },
                        {
                            "size": "extralarge",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/a6e7c9f329c60f85427dac2fa1be897e.png",
                        },
                    ],
                    "mbid": "",
                    "album": {
                        "mbid": "0c856099-033b-4bee-8ac3-83a197807a37",
                        "#text": "Seventeen Going Under",
                    },
                    "name": "Seventeen Going Under - Edit",
                    "url": "https://www.last.fm/music/Sam+Fender/_/Seventeen+Going+Under+-+Edit",
                    "date": {"uts": "1662620321", "#text": "08 Sep 2022, 06:58"},
                },
                {
                    "artist": {"mbid": "", "#text": "Sam Fender"},
                    "streamable": "0",
                    "image": [
                        {
                            "size": "small",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/34s/2dd4ca82b5b07a0ac1817c6a06c891c9.jpg",
                        },
                        {
                            "size": "medium",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/64s/2dd4ca82b5b07a0ac1817c6a06c891c9.jpg",
                        },
                        {
                            "size": "large",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/174s/2dd4ca82b5b07a0ac1817c6a06c891c9.jpg",
                        },
                        {
                            "size": "extralarge",
                            "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/2dd4ca82b5b07a0ac1817c6a06c891c9.jpg",
                        },
                    ],
                    "mbid": "",
                    "album": {
                        "mbid": "",
                        "#text": "Getting Started (Live From Finsbury Park)",
                    },
                    "name": "Getting Started - Live From Finsbury Park",
                    "url": "https://www.last.fm/music/Sam+Fender/_/Getting+Started+-+Live+From+Finsbury+Park",
                    "date": {"uts": "1662620083", "#text": "08 Sep 2022, 06:54"},
                },
            ]
        }
    }
    return example_json


@pytest.fixture()
def example_track():
    example_track = {
        "artist": {
            "mbid": "bdc343bd-1c45-4a5d-b956-c4429f3dbba5",
            "#text": "Blossoms",
        },
        "streamable": "0",
        "image": [
            {
                "size": "small",
                "#text": "https://lastfm.freetls.fastly.net/i/u/34s/1976e6c8659480153ec82086a3a02b3c.jpg",
            },
            {
                "size": "medium",
                "#text": "https://lastfm.freetls.fastly.net/i/u/64s/1976e6c8659480153ec82086a3a02b3c.jpg",
            },
            {
                "size": "large",
                "#text": "https://lastfm.freetls.fastly.net/i/u/174s/1976e6c8659480153ec82086a3a02b3c.jpg",
            },
            {
                "size": "extralarge",
                "#text": "https://lastfm.freetls.fastly.net/i/u/300x300/1976e6c8659480153ec82086a3a02b3c.jpg",
            },
        ],
        "mbid": "31cb91f9-3734-48e3-b7b0-051ff1fd843f",
        "album": {
            "mbid": "571ab3dd-8037-4667-b58a-21bd6976af14",
            "#text": "Foolish Loving Spaces (Deluxe Edition)",
        },
        "name": "Your Girlfriend",
        "url": "https://www.last.fm/music/Blossoms/_/Your+Girlfriend",
        "date": {"uts": "1662621238", "#text": "08 Sep 2022, 07:13"},
    }
    return example_track


@pytest.fixture()
def example_all_songs_df():
    all_songs_df = pd.DataFrame(
        {
            "artist": ["Blossoms", "Sam Fender", "Sam Fender", "Sam Fender"],
            "song_title": [
                "Your Girlfriend",
                "Seventeen Going Under - Edit",
                "Seventeen Going Under - Edit",
                "Getting Started - Live From Finsbury Park",
            ],
            "listen_date": [
                "2022-09-08 07:13:58",
                "2022-09-08 07:01:02",
                "2022-09-08 06:58:41",
                "2022-09-08 06:54:43",
            ],
        },
        index=[0, 1, 2, 3],
    )
    return all_songs_df
