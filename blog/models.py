from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    img = models.ImageField(upload_to='Product/img')
    price = models.IntegerField()
    def get_absolute_url(self):
        return reverse("productDetail", args=[self.slug])

    def __str__(self):
        return self.name



class Team(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Team/img')
    job = models.CharField(max_length=200)

class Blog(models.Model):
    bio = models.TextField()
    img = models.ImageField(upload_to='Blog/img')
    date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class News(models.Model):
    email = models.EmailField(max_length=200)







