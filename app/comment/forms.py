from django import forms
from comment.models import Comment
from parler.forms import TranslatableModelForm

class CommentForm(TranslatableModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widget = {
            'name': forms.TextInput(attrs={'class' : 'form-group'}),
            'email': forms.TextInput(attrs={'class' : 'form-group'}),
            'body': forms.Textarea(attrs={'class' : 'form-group'}),
        }
        