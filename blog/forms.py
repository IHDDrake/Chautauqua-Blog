from django import forms
from .models import Post, Comment


#Form for adding Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols': 130}),
        }
