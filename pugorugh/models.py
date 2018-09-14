from django.contrib.auth.models import User
from django.db import models


class Dog(models.Model):
    GENDER_CHOICES = (
        ('m','male'),
        ('f','female'),
        ('u','unknown'),
    )
    SIZE_CHOICES = (
        ('s','small'),
        ('m','medium'),
        ('l','large'),
        ('xl','extra large'),
    )
    name = models.CharField(max_length=200)
    image_filename = models.CharField(max_length=200)
    breed = models.CharField(max_length=200,blank=True,null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)

class UserDog(models.Model):
    STATUS_CHOICES = (
        ('l','liked'),
        ('d','disliked'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dog = models.ForeignKey('Dog',on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)




class UserPref(models.Model):
    AGE_CHOICES = (
        ('b','baby'),
        ('y','young'),
        ('a','adult'),
        ('s','senior'),

    )
    GENDER_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
        ('u', 'unknown'),
        ('m,f', 'male and female'),
    )
    SIZE_CHOICES = (
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large'),
        ('xl', 'extra large'),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.CharField(max_length=8, choices=AGE_CHOICES,
                           blank=True,null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,
                              blank=True,null=True)
    size = models.CharField(max_length=8, choices=SIZE_CHOICES,
                            blank=True,null=True)


