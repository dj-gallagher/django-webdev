from django.urls import path

from . import views

app_name = 'player'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('user/', views.UserView.as_view(), name='user'),
    path('authorize/', views.AuthorizeView.as_view(), name='authorize'),
    path('callback/', views.CallbackView.as_view(), name='callback'),
]