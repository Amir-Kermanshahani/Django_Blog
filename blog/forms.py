import email
from django import forms
from blog.models import Comment

class CForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.Textarea()

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['post', 'name', 'subject', 'email', 'message']
