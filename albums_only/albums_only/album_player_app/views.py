from django.http import HttpResponseRedirect, HttpResponse, request
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic


from django.utils import timezone

# Create your views here.

#class IndexView(generic.DetailView):
#    template_name = 'album_player_app/index.html'

from django.views import View

class IndexView(View):

    def get(self, request):
        
        template_name = 'album_player_app/index.html'
        
        return render(request,
                      template_name)
    
from spotipy.oauth2 import SpotifyClientCredentials

import requests

def get_token():
    
    CLIENT_ID='01df235638fc4c4a95c5a12486500ac4'
    CLIENT_SECRET='4712f7eef67e4c0794c4fd5589f4087d'
    
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    # POST
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']
    
    #print(access_token)
    
    return access_token

#access_token = get_token()

def track_audio_features(access_token):
    
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'

    # Track ID from the URI
    track_id = '6y0igZArWVi6Iz0rj35c1Y'

    # actual GET request with proper header
    r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
    
    r = r.json()
    
    print(r)

def user_top_tracks(access_token):
    
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'

    # Track ID from the URI
    user_id = 'djohngallagher1'

    # actual GET request with proper header
    r = requests.get(BASE_URL + f'users/{user_id}/playlists?limit=2', headers=headers)
    
    r = r.json()
    
    playlists=[]
    
    for pl in r["items"]:
        playlists.append(pl["name"])
        
    return playlists
        

    
   
class AlbumsView(View):
    
    def get(self, request):
        
        SPOTIPY_CLIENT_ID='01df235638fc4c4a95c5a12486500ac4'
        SPOTIPY_CLIENT_SECRET='4712f7eef67e4c0794c4fd5589f4087d'
        REDIRECT_URI='http://127.0.0.1:8000/album_player_app/albums/'
        
        template_name = 'album_player_app/albums.html'
        
        access_token = get_token()
        
        playlists = user_top_tracks(access_token)
        
        return render(request,
                      template_name,
                      context={"playlist_list" : playlists})
