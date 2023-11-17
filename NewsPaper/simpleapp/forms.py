from django.core.exceptions import ValidationError
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    text = forms.Charfield(min_length=50)
    class Meta:
        model = Post
        fields = '__all__'
    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
     
        return cleaned_data