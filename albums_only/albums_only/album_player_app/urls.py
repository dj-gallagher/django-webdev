from django.urls import path

from . import views

app_name = 'album_player_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('albums/', views.AlbumsView.as_view(), name='albums'),
]