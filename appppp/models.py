from django.db import models

# Create your models here.
class Song(models.Model):
    name=models.CharField(max_length=200)
    language=models.CharField(max_length=33)
    singer=models.CharField(max_length=23)
    
    def __str__(self):
        return self.name
