from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    default_auto_field = 'django.db.models.BigAutoField'
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)  # this field is optional, that is why blank=True
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)


    def __str__(self):

        return self.name

