from django.db import models
#we imported the models from DB library 
# Create your models here.

#It tells us that new class Post  inharits some of the properties from models.Model.
#model has title, body, publish date
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    
class User(models.Model):
    post = models.ForeignKey(Post)
    post_text = models.CharField(max_length=200)
    
    