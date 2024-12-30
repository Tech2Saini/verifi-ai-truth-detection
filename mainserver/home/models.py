from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from datetime import datetime
from django.conf import settings
import os


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

# Create your models here.
class Profile(AbstractUser):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True,default='./profile_images/user.png')
    city = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.username
    

# Feedback Model
class Feedback(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='feedbacks')
    content = models.TextField(default="", help_text="Specify the associated content (e.g., product or post).",blank=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=3)
    fid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    real = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Rating: {self.rating} by {self.user.username} for {self.content}"


class ContactServices(models.Model):
    name= models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=30, choices=(('General Customer Service','General Customer'),('Suggestions','Suggestions'),('Product Suppport','Product Support')))
    message = models.TextField(default="", help_text="Mention your resion to contact us",blank=True,null=False)
    created_date = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return f"{self.name} : {self.email}"