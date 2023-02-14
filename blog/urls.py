from django.urls import path
from . import views
from .views import Home, Detail, addPost,HomeRev, upVote, downVote
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', Home.as_view(), name="homepage"),
    path('rev/', HomeRev.as_view(), name="homepageRev"),
    path('posts/<int:pk>', Detail.as_view(), name="detailed_post"),
    path('add_post/', addPost.as_view(), name ='add_post'),
    path('upVote/<int:pk>', upVote, name = 'upvote'),
    path('downVote/<int:pk>', downVote, name = 'downvote')

]
urlpatterns += staticfiles_urlpatterns()

