from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    story = models.TextField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Photographer(models.Model):
    name = models.CharField(max_length=100)
    business = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Florist(models.Model):
    name = models.CharField(max_length=100)
    business = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Planner(models.Model):
    name = models.CharField(max_length=100)
    business = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Music(models.Model):
    name = models.CharField(max_length=100)
    business = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Catering(models.Model):
    name = models.CharField(max_length=100)
    business = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Bakery(models.Model):
    name = models.CharField(max_length=100)
    business = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name