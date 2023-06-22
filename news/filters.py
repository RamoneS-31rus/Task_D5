from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFilter
from django import forms

from .models import Post, Category


class PostFilter(FilterSet):
    title = CharFilter(
        lookup_expr="icontains",
        label="Заголовок",
        widget=forms.TextInput(attrs={"class": "form-control shadow-none"}),
    )
    category = ModelChoiceFilter(
        queryset=Category.objects.all(),
        empty_label="Все категории",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    date_create = DateFilter(
        label="Дата публикации с",
        lookup_expr="gte",
        widget=forms.DateTimeInput(
            attrs={"type": "date", "class": "form-control shadow-none"},
        ),
    )

    class Meta:
        model = Post
        fields = ["title", "category", "date_create"]
