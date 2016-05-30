import spotipy

def mstosec(ms):
    sec=ms/1000
    return sec

trackurn = 'spotify:track:0Svkvt5I79wficMFgaqEQJ'

result = spotipy.Spotify()
track = result.track(trackurn)

for d in track['artists']:
    print(d['name'])

print(track['album']['name'])
print(track['name'])
print(mstosec(track['duration_ms']))
print(track['id'])

