from django.db import models

# Create your models here.

class Home(models.Model):
    image = models.ImageField(upload_to='images/')
    character = models.CharField(max_length=300)