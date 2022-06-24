from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20, blank=True)
    picture = CloudinaryField('image', blank=True)

    def __str__(self):
        return self.user.username

    # user profile creation
    def create_profile(sender, **kwargs):
        user = kwargs['instance']
        if kwargs['created']:
            user_profile = UserProfile(user=user)
            user_profile.save()
    post_save.connect(create_profile, sender=User)

    
LUGGAGE_CHOICES = [
    (1,'Bedsitter'),
    (2,'1 Bedroom'),
    (3,'2 Bedroom'),
    (4,'3 Bedroom'),
    (5,'Small Office'),
    (6,'Medium Office'),
    (8,'Large Office'),
]

# create moving details model
class MovingDetails(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='moving_details', null=True)
    address = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=100, blank=True)
    luggage_size = models.IntegerField(choices=LUGGAGE_CHOICES, default=0)
    relocating_on = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return str(f'{self.address} :: {self.destination}' )


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def create_post(self):
        self.save()

    def __str__(self):
        return self.title


class RateUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviews = models.CharField(max_length=100, null=True)
    ratings = GenericRelation(Rating, related_query_name='ratings')

    def __str__(self):
        return str(self.reviews)