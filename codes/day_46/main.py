# Importing libraries
import requests
from bs4 import BeautifulSoup
from billboard_data import get_top_artists, get_top_tracks
from spotipy import SpotifyOAuth, Spotify
import time

# URL endpoint
BILLBOARD_END = "https://www.billboard.com/charts/hot-100/"

# In order to do the request in the URL we need to append the date selection to the URL END
date_selection = input("Which year do you want to travel to? Type this date in this format YYYY-MM-DD: ")
request_url = f'{BILLBOARD_END}{date_selection}/'
request = requests.get(request_url)
# To text
billboard_site = request.text

# Creating a soup object and retrieving data
billboard_soup = BeautifulSoup(billboard_site, "html.parser")
top_tracks = get_top_tracks(billboard_soup)
top_artists = get_top_artists(billboard_soup)

# ---- Spotipy ---- #
CLIENT_ID = "57ee1f7104214898819ab0eb22123656"
CLIENT_SECRET = "785c019d87e848698c46d2fa6c36f130"

# Autentication
oauth_spotify = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"

)
oauth_spotify.get_access_token()
sp = Spotify(oauth_manager=oauth_spotify)
user_id = sp.current_user()["id"]
print("Autentication was a success in Spotify for your user!",user_id)

# --- Main Program -- #
# Retrieving URIs and appending in a list
uri_list = []
for song_name, artist_name in zip(top_tracks, top_artists):
    time.sleep(1)
    search_uri = sp.search(q=f"track:{song_name} artist:{artist_name}", type="track")
    try:
        uri = search_uri["tracks"]["items"][0]["uri"]
        uri_list.append(uri)

    except:
        print(f"{song_name} by {artist_name} not found, skipping")

# Creating the Playlist
playlist_id = sp.user_playlist_create(user=user_id, name=f"{date_selection} TOP 100 BILLBOARD", public=False)['id']

# Adding the uri_list to the playlist
add_tracks = sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)
