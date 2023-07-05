from rest_framework import generics
from .models import Movie, Post
from .serializers import MovieSerializers, PostSerializers
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    permission_classes= [IsOwnerOrReadOnly]

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    permission_classes= [IsOwnerOrReadOnly]


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes= [IsAuthenticatedOrReadOnly]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes= [IsAuthenticatedOrReadOnly]
