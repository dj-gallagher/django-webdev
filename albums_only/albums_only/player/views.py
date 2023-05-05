from django.shortcuts import render

import requests

# Create your views here.

from django.views import View

class IndexView(View):

    def get(self, request):
        
        template_name = 'player/index.html'
        
        return render(request,
                      template_name)
        
        
class UserView(View):

    def get(self, request):
        
        template_name = 'player/user.html'
        
        return render(request,
                      template_name)

from urllib.parse import urlencode

def redirect_to_auth_code_flow():  
    
    CLIENT_ID='01df235638fc4c4a95c5a12486500ac4'
    CLIENT_SECRET='4712f7eef67e4c0794c4fd5589f4087d'
    
    auth_headers = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": "http://127.0.0.1:8000/player/callback",
        "scope": "user-library-read"
    }     
    
    r = requests.get("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))
        
class AuthorizeView(View):

    def get(self, request):
        
        
        
        template_name = 'player/authorize.html'
        
        return render(request,
                      template_name)
        
class CallbackView(View):
    
    def get(request):
        
        pass