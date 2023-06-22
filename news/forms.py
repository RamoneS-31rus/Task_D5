from django import forms

from .models import Author, Category, Post


class PostForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        label="Автор",
        queryset=Author.objects.all(),
        widget=forms.Select(attrs={"class": "form-select shadow-none"}),
    )
    title = forms.CharField(
        label="Заголовок",
        widget=forms.TextInput(attrs={"class": "form-control shadow-none"}),
    )
    text = forms.CharField(
        label="Текст",
        widget=forms.Textarea(attrs={"class": "form-control shadow-none"}),
    )

    class Meta:
        model = Post
        fields = ["author", "category", "title", "text"]

        widgets = {
            "category": forms.CheckboxSelectMultiple(),
        }
