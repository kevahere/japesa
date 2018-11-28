from django.db import models

# Create your models here.
class Lender(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    reviews = models.PositiveIntegerField(default=0)

class Review(models.Model):
    reviewer = models.CharField(max_length=250)
    rating = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=300)
    likes = models.IntegerField(default=0)
    pub_time = models.DateTimeField(auto_now_add=True)
