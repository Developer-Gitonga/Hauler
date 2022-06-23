from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django_google_maps import fields as map_fields


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20, blank=True)
    picture = CloudinaryField('image', blank=True)
    
    
    def __str__(self):
        return self.user.username
    
    # user profile creation
    def create_profile( sender, **kwargs):
        user = kwargs['instance']
        if kwargs['created']:
            user_profile = UserProfile(user=user)
            user_profile.save()
    post_save.connect(create_profile, sender=User)   
    
    
# create moving details model
class MovingDetails(models.Model):
    depart_location = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    
    
