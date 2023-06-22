from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        rat_post_all = 0
        rat_com_author = 0
        rat_com_all = 0
        for i in Post.objects.filter(author__name__username=self.name):
            rat_post_all += i.rating

        for i in Comment.objects.filter(user__username=self.name):
            rat_com_author += i.rating

        for post in Post.objects.filter(author__name__username=self.name):
            for i in Comment.objects.filter(post=post):
                rat_com_all += i.rating

        self.rating = rat_post_all * 3 + rat_com_author + rat_com_all
        self.save()

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    news = "Новость"
    article = "Статья"
    type = [(news, "Новость"), (article, "Статья")]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=type, default=news)
    date_create = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(
        "Category", through="PostCategory", verbose_name="Категории"
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def get_absolute_url(self):
        if self.type == "Новость":
            return reverse("news_detail", args=[str(self.id)])
        elif self.type == "Статья":
            return reverse("article_detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.title}"

    def preview(self):
        return self.text[:124] + "..."

    def like(self):
        self.likes += 1
        self.rating = self.likes - self.dislikes
        self.save()

    def dislike(self):
        self.dislikes += 1
        self.rating = self.likes - self.dislikes
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.text}"

    def like(self):
        self.likes += 1
        self.rating = self.likes - self.dislikes
        self.save()

    def dislike(self):
        self.dislikes += 1
        self.rating = self.likes - self.dislikes
        self.save()
