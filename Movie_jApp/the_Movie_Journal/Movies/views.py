from django.shortcuts import render
import requests
from .models import Movie
from django.conf import settings
from django.http import JsonResponse
# Create your views here.

OMDB_API_KEY = settings.OMDB_API_KEY


def fetch_movie_data(request):
    title = request.GET.get('title')
    
    if not title:
        return JsonResponse({'error': 'No title provided'}, status=400)
    
    
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}"
    print(f"Fetching data for title: {title}")
    
    response = requests.get(url)
    print(f"Response status: {response.status_code}, Response data: {response.text}")


    if response.status_code == 200:
        movie_data = response.json()
        if movie_data.get('Response') == 'False':
            return JsonResponse({'error': 'Movie not found in OMDB'}, status=404)
        
        movie, created = Movie.objects.get_or_create(
            imdb_id=movie_data['imdbID'],
            defaults={
                'title': movie_data['Title'],
                'plot': movie_data['Plot'],
                'year': movie_data['Year'],
                'imdb_rating': movie_data['imdbRating']
            }
        )
        print(f"Movie saved: {movie.title}")
        return JsonResponse(movie_data)
    else:
        return JsonResponse({'error': 'Failed to fetch movie data'}, status=404)
        