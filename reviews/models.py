from django.conf import settings
from django.db import models

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    movie = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to='')

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews_comment')
    content = models.CharField(max_length=200)