from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.template import RequestContext


class Home(ListView):
    model = Post
    template_name = 'homepage.html'
    ordering = ['-created_at']





class HomeRev(ListView):
    model = Post
    template_name = 'homepageRev.html'
    ordering = ['created_at']


class Detail(DetailView, CreateView):

    model = Post
    form_class = CommentForm
    template_name = 'postDetails.html'
    def get_object(self):
        obj = super().get_object()
        obj.viewCount += 1
        obj.save()
        return obj

    def get_success_url(self):
        return reverse_lazy('detailed_post', kwargs={'pk': self.kwargs['pk']})
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class addPost(CreateView):
    model = Post
    template_name = 'addPost.html'
    fields = '__all__'


def upVote(request, pk):

    comment = get_object_or_404(Comment, id=request.POST.get('upvoteID'))
    comment.upVote += 1
    comment.save()
    return HttpResponseRedirect(reverse('detailed_post', args=[str(pk)]))

def downVote(request, pk):

    comment = get_object_or_404(Comment, id=request.POST.get('downvoteID'))
    comment.downVote -= 1
    comment.save()

    return HttpResponseRedirect(reverse('detailed_post', args=[str(pk)]))
