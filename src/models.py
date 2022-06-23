from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save


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
    
class QuoteForm(models.Model):
    size=(('1 Room or small studio','1 Room or small studio'),('1 Bedroom apartment','1 Bedroom apartment'), ('2 Bedroom apartment','2 Bedroom apartment'),('3 Bedroom apartment','3 Bedroom apartment'),('4 Bedroom apartment','4 Bedroom apartment'))
    when =(('Unknown','Unknown'),('Within a week','Within a week'), ('1-2 months','1-2 months'),('2-4 months','2-4 months'))
    MovingFrom = models.CharField(max_length=200, null=True)
    MovingTo = models.CharField(max_length=200,)
    size = models.CharField(max_length=300, choices=size)
    When  = models.CharField(max_length=300,choices=when)