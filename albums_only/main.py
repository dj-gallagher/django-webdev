import requests

def main():
    
    BASE_URL = "https://api.spotify.com/v1/me/"
        
    access_token = "BQAAmJ2oxYXOxsv1iVaV1SUSW_WMp_3AGz86dc1zb7Ogpy-EuBpXDxKejbRPEXUMIMn_PB89Z0VopRlNa-XnJjvWErJDNY4HKGsTjr-pBK_fwEAIwzxoUlm3I-dpS9huMOCFfMRyEHpy1lUp-wOgELIhdLbV_PXg1os7DWIVztgfsyDJ9g8iHeENeHf9S66AOqzJEsGvK1Gxua1QINe-YQJ1xWM"
    
    user_headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    user_params = {
        "limit": 5
    }

    API_ENDPOINT = "player/devices/"
    
    # response is a json object with ["items"] being all the albums returned (list of dicts)
    api_response = requests.get(BASE_URL + API_ENDPOINT, headers=user_headers).json()
    
    print(api_response)


def start_resume_playback():
    
    BASE_URL = "https://api.spotify.com/v1/me/"
        
    access_token = "BQAAmJ2oxYXOxsv1iVaV1SUSW_WMp_3AGz86dc1zb7Ogpy-EuBpXDxKejbRPEXUMIMn_PB89Z0VopRlNa-XnJjvWErJDNY4HKGsTjr-pBK_fwEAIwzxoUlm3I-dpS9huMOCFfMRyEHpy1lUp-wOgELIhdLbV_PXg1os7DWIVztgfsyDJ9g8iHeENeHf9S66AOqzJEsGvK1Gxua1QINe-YQJ1xWM"
    
    request_headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    request_params = {
        "device_id": "6ed68f20762563311aec3c9f37700345bd7418f2"
    }

    API_ENDPOINT = "player/play/"
    
    # response is a json object with ["items"] being all the albums returned (list of dicts)
    api_response = requests.put(BASE_URL + API_ENDPOINT, params=request_params, headers=request_headers)
    
    
def stop_playback():
    
    BASE_URL = "https://api.spotify.com/v1/me/"
        
    access_token = "BQAAmJ2oxYXOxsv1iVaV1SUSW_WMp_3AGz86dc1zb7Ogpy-EuBpXDxKejbRPEXUMIMn_PB89Z0VopRlNa-XnJjvWErJDNY4HKGsTjr-pBK_fwEAIwzxoUlm3I-dpS9huMOCFfMRyEHpy1lUp-wOgELIhdLbV_PXg1os7DWIVztgfsyDJ9g8iHeENeHf9S66AOqzJEsGvK1Gxua1QINe-YQJ1xWM"
    
    request_headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    request_params = {
        "device_id": "6ed68f20762563311aec3c9f37700345bd7418f2"
    }

    API_ENDPOINT = "player/pause/"
    
    # response is a json object with ["items"] being all the albums returned (list of dicts)
    api_response = requests.put(BASE_URL + API_ENDPOINT, params=request_params, headers=request_headers)
    
    
def get_user_album_names_and_start_playback_urls():
    
    BASE_URL = "https://api.spotify.com/v1/me/"
        
    access_token = "BQDqBitIOiOw5d5n4jD4PxWq2aG4TYnKudhcLetYqmsoxmn839EznM-6Pg0aawWdI0KqPNOwjqgD0tWJUCPulYmx-woDtmnm6CMzXryF4VBEK1EMmb89j1s7ZJrvacDVFJZRUXrdL86GwCPpqkb2e30_9_OacV1Z6By3klFw8ryduaLrYXMOOC75mjj8_A9AHaYRP7vWtvhYWmbnoWtuFcxIGzE"
    
    request_headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    request_params = {
        "limit": 3
    }

    API_ENDPOINT = "albums/"
    
    # response is a json object with ["items"] being all the albums returned (list of dicts)
    json_response = requests.get(BASE_URL + API_ENDPOINT, params=request_params, headers=request_headers).json()
    
    user_albums = []
    
    for item in json_response["items"]:
        
        album_name = item["album"]["name"]
        album_uri = item["album"]["uri"]
        
        user_albums.append({
            "name" : album_name,
            "uri" : album_uri
        })
        
    print(user_albums)
    
    
        
        
    
    



if __name__ == "__main__":
    
    get_user_album_names_and_start_playback_urls()
            
    
            
    