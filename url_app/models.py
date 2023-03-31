from django.db import models
from django.contrib.auth.models import User

class shorterURL (models.Model):
    original_url = models.TextField()
    shorter_url = models.CharField(max_length=100)
    visit_count = models.IntegerField(default=0)
    private = models.BooleanField(default=False)
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.original_url

