from django.urls import path
from .views import Home, Detail, addPost, upVote, downVote
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', Home.as_view(), name="homepage"),
    path('posts/<int:pk>', Detail.as_view(), name="detailed_post"),
    #This url goes unused in this program
    path('add_post/', addPost.as_view(), name ='add_post'),

    #The upvote and downvote are passed the primary key of the post so
    #they know where to return to after completing their tasks.
    path('upVote/<int:pk>', upVote, name = 'upvote'),
    path('downVote/<int:pk>', downVote, name = 'downvote')

]

#adding Static Files
urlpatterns += staticfiles_urlpatterns()
