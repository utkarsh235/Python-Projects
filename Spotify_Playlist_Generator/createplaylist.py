import os
import spotify_client
import pprint
from spotify_client import SpotifyClient


def main():
    SPOTIFY_AUTHORIZATION_TOKEN = # Mention your Spotify Authorization Token here
    SPOTIFY_USER_ID = # Mention your Spotify User ID here
    spotify_client = SpotifyClient(SPOTIFY_AUTHORIZATION_TOKEN, SPOTIFY_USER_ID)

    # get last played tracks
    num_tracks_to_visualise = int(input("How many tracks would you like to visualise? "))
    last_played_tracks = spotify_client.get_recently_played_tracks_for_user(SPOTIFY_AUTHORIZATION_TOKEN
                                                                            , num_tracks_to_visualise)
    #print(last_played_tracks['items'][0]['track']['album']['name'])
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(last_played_tracks)
    #last_played_tracks['items'][0]['track']['album']['name']
    print(f"\nHere are the last {num_tracks_to_visualise} tracks you listened to on Spotify:")
    for idx in range(num_tracks_to_visualise):
        print(f"{idx} - {last_played_tracks['items'][idx]['track']['album']['name']}")
        # for track in last_played_tracks['items'][idx]['track']['album']['name']:
            # print(track)

    # choose which tracks to use as a seed to generate a playlist
    indexes = input("\nEnter a list of up to 5 tracks you'd like to use as seeds. Use indexes separated by a space: ")
    indexes = indexes.split()
    seed_tracks = [last_played_tracks['items'][int(index)]['track']['album']['name'] for index in indexes]

    # get recommended tracks based off seed tracks
    recommended_tracks = spotify_client.get_recommendations('Energy', 1, 8, seed_tracks, limit=3)
    print("\nHere are the recommended tracks which will be included in your new playlist:")
    for index, track in enumerate(recommended_tracks):
        print(f"{index+1}- {track}")

    # get playlist name from user and create playlist
    playlist_name = input("\nWhat's the playlist name? ")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"\nPlaylist '{playlist_name}' was created successfully.")

    # populate playlist with recommended tracks
    spotify_client.add_songs_to_playlist(SPOTIFY_AUTHORIZATION_TOKEN, playlist, recommended_tracks)
    print(f"\nRecommended tracks successfully uploaded to playlist '{playlist_name}'.")


if __name__ == "__main__":
    main()