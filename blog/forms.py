from django import forms
from blog.models import Blog,Comment


class CreateBlogForm(forms.ModelForm):

    class Meta:

        model = Blog
        fields = ('title','image','content')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
