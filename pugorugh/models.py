from django.contrib.auth.models import User
from django.db import models

DOG_AGE_YEARS = {
    'baby': list(range(0, 30)),
    'young': list(range(30, 60)),
    'adult': list(range(60, 90)),
    'senior': list(range(90, 200)),

}


class Dog(models.Model):
    """ Dog model
    GENDER_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
        ('u', 'unknown'),
    )
    SIZE_CHOICES = (
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large'),
        ('xl', 'extra large'),
    )
    """
    name = models.CharField(max_length=200)
    image_filename = models.CharField(max_length=200)
    breed = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, )
    size = models.CharField(max_length=1, )


class UserDog(models.Model):
    """User dog model
    STATUS_CHOICES = (
        ('l', 'liked'),
        ('d', 'disliked'),
        ('u', 'undecided'),
    )"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dog = models.ForeignKey('Dog', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, default='u')

    class Meta:
        unique_together = ['user', 'dog']


class UserPref(models.Model):
    """
    User preference model feilds accept letters separated with comma
    AGE_CHOICES = (
        ('b', 'baby'),
        ('y', 'young'),
        ('a', 'adult'),
        ('s', 'senior'),

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
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=8,
                           blank=True, null=True)
    gender = models.CharField(max_length=6,
                              blank=True, null=True)
    size = models.CharField(max_length=8,
                            blank=True, null=True)
