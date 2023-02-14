from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    heroHeader = models.ImageField(upload_to ='uploads/', default=None, blank=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    viewCount = models.IntegerField(default=0)
    pubStatus = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('detailed_post', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name= "comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upVote = models.IntegerField(default=0)
    downVote = models.IntegerField(default=0)


    def __str__(self):
        return self.post.title + ' - ' + str(self.name)



