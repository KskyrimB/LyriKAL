import requests

def lyrics(song_name, artist_name):
    # song_name = "Shape of you"
    # artist_name = "Ed Sheeran"
    title = song_name
    artist = artist_name
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.request("GET",url)
    data = response.json()
    return data['lyrics']