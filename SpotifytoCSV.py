import sys
import os
import spotipy
import spotipy.util as util
from collections import Counter

#global variables
q=0
bands = []
details = []

def mstosec(ms):
    sec=ms/1000
    return sec

def show_tracks(results):
    global q
    global bands

    length=0
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("%d,%s,%s,%d" % (q, track['artists'][0]['name'], track['name'] ,mstosec(track['duration_ms'])))
        bands.append((track['artists'][0]['name']))
        q= q + 1;


username="eternal_atom"
token = util.prompt_for_user_token(username)

if token:
    sp = spotipy.Spotify(auth=token)
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['id']=="6GXK27XsRSngHWROTtOsst":
            print()
            print(playlist['name'])
            print('  total tracks', playlist['tracks']['total'])
            results = sp.user_playlist(username, playlist['id'], fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)

    #FIND MOST POPULAR ARTIST
    counts = Counter(bands)
    print(" ")
    print(counts)


else:
     print("Can't get token for", username)
