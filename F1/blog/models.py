from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.

class Author(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    pseudonym = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254)

    def full_name(self):
        return f'{self.f_name} {self.l_name}'

    def __str__(self):
        if self.pseudonym:
            return self.pseudonym
        else:
            return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    image = models.ImageField(upload_to='posts', null=True)
    date = models.DateField(auto_now=True)
    txt = models.TextField(
        validators=[MinLengthValidator(200), MaxLengthValidator(3000)])
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(
        Author, null=True, on_delete=models.SET_NULL, related_name='posts')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.slug


class Comment(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField()
    txt = models.TextField(max_length=500)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
