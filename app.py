import os
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Set environment variables for your credentials
SPOTIPY_CLIENT_ID = "7163fd8fd8d74a81a0f22bf66492fa1a"
SPOTIPY_CLIENT_SECRET = "d7317584ec3643f9be9586028a7388ac"
SPOTIPY_REDIRECT_URI = "http://localhost:8501/callback/"


# Spotify OAuth setup with token caching
sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                        client_secret=SPOTIPY_CLIENT_SECRET,
                        redirect_uri=SPOTIPY_REDIRECT_URI,
                        scope="user-library-read",
                        cache_path=".cache")  # Token cache path

# Function to get authenticated Spotify instance
def get_spotify_instance():
    token_info = sp_oauth.get_cached_token()
    
    # If no cached token, prompt user to authenticate
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        st.write("Please authenticate: [Authenticate Here]({})".format(auth_url))
        
        code = st.text_input("Enter the authorization code you received after authenticating:")
        
        if code:
            token_info = sp_oauth.get_access_token(code)
            sp = spotipy.Spotify(auth=token_info['access_token'])
            st.success("Authenticated successfully!")
            return sp
        else:
            return None
    else:
        sp = spotipy.Spotify(auth=token_info['access_token'])
        return sp

# Streamlit UI
st.title("Spotify Mood Playlist Curator")

mood = st.text_input("Enter your mood or activity (e.g., chill, workout, study):", "chill")

sp = get_spotify_instance()

if sp:
    # Search for playlists based on mood
    results = sp.search(q=mood, type='playlist', limit=10)
    
    playlist_data = []
    for playlist in results['playlists']['items']:
        playlist_id = playlist['id']
        playlist_name = playlist['name']
        
        # Get tracks from the playlist
        tracks = sp.playlist_tracks(playlist_id)
        for item in tracks['items']:
            track = item['track']
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            
            # Get audio features for the track
            audio_features = sp.audio_features(track['id'])[0]
            danceability = audio_features['danceability']
            energy = audio_features['energy']
            valence = audio_features['valence']
            
            # Store track information
            playlist_data.append({
                'track_name': track_name,
                'artist_name': artist_name,
                'playlist_name': playlist_name,
                'danceability': danceability,
                'energy': energy,
                'valence': valence
            })

    # Save data to CSV
    df = pd.DataFrame(playlist_data)
    file_name = f'spotify_{mood}_data.csv'
    df.to_csv(file_name, index=False)
    st.write(f"Playlist data for '{mood}' saved to {file_name}")
