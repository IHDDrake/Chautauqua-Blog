from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


#This is the class-based view for a very simple homepage.
#It is ordered by negative creation time. This results in the object_list being
#ordered with the most recent posts at the top
class Home(ListView):
    model = Post
    template_name = 'homepage.html'
    ordering = ['-created_at']


#This is the class-based view for the Detailed Post page.
#Included are a function that update the viewCount every time the page is visited,
#a function to correctly point the url to the right post,
#and a function to ensure that forms are submitted correctly
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



#This class-based view goes unused in the final product. It remains for the purpose of remimplementation upon request
class addPost(CreateView):
    model = Post
    template_name = 'addPost.html'
    fields = '__all__'



# These are the two function based views. They have no associated template and allow for the functionality
#of the comment liking and disliking buttons. Upon modify the specific comments value in the database.
#After their task is completed they redirect back to the detailed post page the comment is on.
#An improvement that can be made for these functions is the inclusion of handling a failed search.
#i.e. if get_object_or_404 doesn't retrieve whats it is asked to.
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
