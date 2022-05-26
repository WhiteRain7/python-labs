import datetime
from distutils.command.upload import upload
from operator import mod
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Blog (models.Model):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    create_date = models.DateTimeField(auto_now = True)

    def __str__ (self): return self.name

    def __repr__ (self):
        return '<{} of {}>'.format(self.name, self.author)


class Article (models.Model):
    heading = models.CharField(max_length = 200)
    text = models.CharField(max_length = 2000)
    img = models.ImageField(upload_to = 'media/', blank = True)
    pub_date = models.DateTimeField(auto_now = True)
    
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)

    def __str__ (self): return self.heading

    def __repr__ (self): 
        return '<Article: {} from {}{}>'.format(
            self.heading[:10], 
            self.pub_date.year + '-' + self.pub_date.month + '-' + self.pub_date.date,
            '' if self.img.null else ' with image')

    def was_published_recently (self, days_ago = 7):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = days_ago)

    def splitted (self):
        return self.text.split('\n')

datetime.timedelta(days=1)