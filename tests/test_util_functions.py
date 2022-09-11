import pandas as pd
from pandas.testing import assert_frame_equal

import src.util_functions as utils


def test_extract_tracks_df(example_json):
    test_songs_df = utils.extract_tracks_df(example_json)
    expected_songs_df = pd.DataFrame(
        {
            "artist": ["Blossoms", "Wet Leg", "Sam Fender", "Sam Fender"],
            "song_title": [
                "Your Girlfriend",
                "Wet Dream",
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
    assert_frame_equal(test_songs_df, expected_songs_df)


def test_extract_single_track(example_track):
    test_songs_dict = utils.extract_single_track(example_track)
    expected_songs_dict = {
        "artist": "Blossoms",
        "song_title": "Your Girlfriend",
        "listen_date": "2022-09-08 07:13:58",
    }
    assert expected_songs_dict == test_songs_dict


def test_convert_unix_timestamp_to_aws_format():
    test_output = utils.convert_unix_timestamp_to_aws_format("1662621238")
    expected_output = "2022-09-08 07:13:58"
    assert test_output == expected_output


def test_get_top_song(example_all_songs_df):
    test_output = utils.get_top_song(example_all_songs_df)
    expected_output = ("Sam Fender", "Seventeen Going Under - Edit")
    assert test_output[0] == expected_output[0]
    assert test_output[1] == expected_output[1]
