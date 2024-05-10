from django import forms 
from .models import Post

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['author']