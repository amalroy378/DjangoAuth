from django.db import models

# Create your models here.
class Actor(models.Model):
    actor_name =models.CharField(max_length=200)
    actor_industry=models.CharField(max_length=200)
    actor_img=models.ImageField(upload_to='actors')

    def __str__(self):
        return self.actor_name


class LatestUpdates(models.Model):
    title=models.CharField(max_length=200) 
    n_movies=models.CharField(max_length=200)  
    description=models.TextField(max_length=225) 

    def __str__(self):
        return self.title
