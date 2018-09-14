from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.generics import (CreateAPIView , ListCreateAPIView,RetrieveUpdateAPIView,
                                     UpdateAPIView, ListAPIView, RetrieveAPIView)

from . import serializers,models


class UserRegisterView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    model = get_user_model()
    serializer_class = serializers.UserSerializer

    def perform_create(self, serializer):
        print(self.request.data)
        print(self.request.user)
        print(self.request.data['username'])
        serializer.save(user=self.request.user)
        user = get_object_or_404(get_user_model(),
                                 username=self.request.data['username'])
        print(user.username)
        pref = models.UserPref()
        pref.user = user
        pref.save()





class UserPrefView(RetrieveUpdateAPIView):
    model = models.UserPref
    queryset = models.UserPref.objects.all()
    serializer_class = serializers.UserPrefSerializer
    def get_object(self):
        queryset = self.get_queryset()
        user_pref = get_object_or_404(queryset,user=self.request.user)
        return user_pref

    def perform_update(self, serializer):
        serializer.save()
        print(self.request.data)
        print(self.request.user)
        print(serializer.data)









class DogUndecidedView(RetrieveAPIView):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer






