from django.urls import path
from .views import MovieList, MovieDetail, PostList, PostDetail

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetail.as_view(), name='movie_detail'),
    path('post/', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]

#Hey Saja! if you want to test a user which is not an admin I made one:
# Username: Saja
# Password: GiveMeAFullMark10!
# Just kidding the password is: Saja123@