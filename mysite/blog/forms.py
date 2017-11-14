from django import forms

from .models import Post


class PostForm(
    forms.ModelForm):  # PostForm, as you probably suspect, is the name of our form. We need to tell Django that this form is a ModelForm (so Django will do some magic for us) – forms.ModelForm is responsible for that.
    class Meta:  # Next, we have class Meta, where we tell Django which model should be used to create this form (model = Post).
        model = Post
        fields = ('title', 'text',)
