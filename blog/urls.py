from django.urls import path
from .views import Home, Detail, addPost, upVote, downVote
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', Home.as_view(), name="homepage"),
    path('posts/<int:pk>', Detail.as_view(), name="detailed_post"),
    path('add_post/', addPost.as_view(), name ='add_post'),
    path('upVote/<int:pk>', upVote, name = 'upvote'),
    path('downVote/<int:pk>', downVote, name = 'downvote')

]
urlpatterns += staticfiles_urlpatterns()

