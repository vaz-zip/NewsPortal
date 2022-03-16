from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.SmallIntegerField(default=0)

    def update_rating(self):
        post_rat = self.post_set.aggregate(postRating=Sum('rating'))
        p_rat = 0
        p_rat += post_rat.get('postRating')

        comment_rat = self.author_user.comment_set.aggregate(commentRating=Sum('rating'))
        c_rat = 0
        c_rat += comment_rat.get('commentRating')

        self.author_rating = p_rat * 3 + c_rat
        self.save()


class Category(models.Model):
    category_theme = models.CharField(max_length=64, unique=True)


article = 'СТА'
news = 'НОВ'

POSITIONS = [
    (article, 'Статья'),
    (news, 'Новость')
]


class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    position = models.CharField(max_length=3, choices=POSITIONS, default=news)
    time_public = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=255)
    news_text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def prewiev(self):
        return self.news_text[0:123] + '...'


class PostCategory(models.Model):
    post_category_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_category_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_us = models.TextField()
    time_comment = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
