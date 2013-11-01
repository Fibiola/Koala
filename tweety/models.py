from django.db import models
import datetime
from django.utils import timezone

# We imported the models from DB library 
# Create your models here.

# It tells us that new class Post  inharits some of the properties from models.Model.
#model has title, body, publish date

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    
    def __unicode__(self): 
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
class User(models.Model):
    post = models.ForeignKey(Post)
    user_description = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.user_description
