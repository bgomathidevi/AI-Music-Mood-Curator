
Spotify Mood Playlist Curator
Overview
The Spotify Mood Playlist Curator is a simple web application built using Streamlit and Spotipy (Spotify Web API wrapper) that helps users find playlists based on their mood or activity. Users can input a mood (e.g., "chill", "workout", "study") and the app will return playlists along with detailed track information such as danceability, energy, and valence. It also saves the retrieved data into a CSV file for further analysis.

Key Features
Mood-Based Playlist Search: Enter a mood (e.g., "chill", "workout") and discover Spotify playlists that match your input.
Track Audio Features: Provides audio metrics like danceability, energy, and valence for each track.
CSV Export: Automatically saves playlist data for future reference or analysis.
Prerequisites
Spotify Developer Account to obtain API credentials (Client ID, Client Secret).
Basic knowledge of using Python and Streamlit for running the application.


Setup Instructions
Spotify Developer App: Create an app on the Spotify Developer Dashboard to get your Client ID, Client Secret, and set the redirect URI.
Environment Setup: Ensure your environment is set up with the required dependencies.
Running the Application: Launch the app locally, and you'll be prompted to authenticate your Spotify account. After logging in, the app will curate playlists based on your mood input.


Authentication: You will need to authenticate with Spotify to allow the app to access playlists.
Mood Input: Enter your mood or activity (e.g., "focus", "relax") into the app interface.
Playlist Data: The app will fetch playlists related to the mood and display key information about each track.
Export: Playlist details, including track names, artists, and audio features, will be saved in a CSV file for easy reference.


Features in Progress
Adding more filters for better playlist recommendations.
Integration with custom playlist creation options for users.
License
This project is licensed under the MIT License.

Contact
For any inquiries or feedback, please reach out to:

Gomathidevi: LinkedIn
GitHub: bgomathidevi
