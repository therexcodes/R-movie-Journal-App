from django.urls import path
from . import views


urlpatterns = [
    path('api/fetch_movie_data/', views.fetch_movie_data, name='fetch_movie_data'),
]
