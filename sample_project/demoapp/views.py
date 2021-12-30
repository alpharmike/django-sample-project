from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status

from .models import Movie


class MovieListView(ListAPIView):
    allowed_methods = ["GET"]
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class MovieCreateView(CreateAPIView):
    allowed_methods = ["POST"]
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        the_serializer = self.serializer_class(data=request.data)

        if not the_serializer.is_valid():
            return Response({'errors': the_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        title = request.data.get("title", "")
        genre = request.data.get("genre", "")
        year = request.data.get("year", "")

        movie = Movie.objects.create(title=title, genre=genre, year=year)
        movie.save()
        serializer = self.get_serializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MovieDetailView(RetrieveAPIView):
    allowed_methods = ["GET"]
    serializer_class = MovieSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk', '')
        movie = Movie.objects.filter(id=pk)
        if movie.exists():
            return movie


class MovieDeleteView(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', '')
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_200_OK)
