from django.urls import path
from . import views


urlpatterns = [
    path('movies/create', views.MovieCreateView.as_view(), name='create_movies'),
    path('movies/list', views.MovieListView.as_view(), name='get_movies'),
    path('movies/detail/<int:pk>', views.MovieDetailView.as_view(), name='get_movie_details'),
    path('movies/delete/<int:pk>', views.MovieDeleteView.as_view(), name='delete_movie'),
]