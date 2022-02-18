from django.core.validators import FileExtensionValidator
from tkinter import CASCADE
from django.db import models



class Author(models.Model):
    name = models.CharField(verbose_name='Name', unique=True, max_length=128)
    login = models.CharField(verbose_name='login', max_length=128)
    password = models.CharField(verbose_name='password', max_length=128)
    avatar = models.ImageField(upload_to='avatar/', max_length = 100, blank=True)#, upload_to=upload_path)
    email = models.EmailField(verbose_name='email', max_length=254, unique=True)

    def __str__(self):
        return self.name



class Video(models.Model):
    title = models.CharField(verbose_name='Name', unique=True, max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    file = models.FileField(
        upload_to='video/',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )

    image = models.ImageField(upload_to='preview/', blank=True)
    rating = models.IntegerField(default = 0)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='+')
    text = models.TextField()
    rating = models.IntegerField(default = 0)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
