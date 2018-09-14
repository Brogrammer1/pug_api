from django.contrib.auth import get_user_model

from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        fields=(
            'username',
            'password'
        )
        model = get_user_model()



class DogSerializer(serializers.ModelSerializer):

    class Meta:
        fields =(
            'id',
            'name',
            'image_filename',
            'breed',
            'age',
            'gender',
            'size',

        )
        model = models.Dog



class UserPrefSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.size = validated_data.get('size', instance.size)
        instance.save()
        return instance

    class Meta:
        extra_kwargs = {
            'user' : {'write_only': True}
        }
        fields = (
            'user',
            'age',
            'gender',
            'size',

        )
        model = models.UserPref
