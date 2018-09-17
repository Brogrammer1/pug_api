from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView,
                                     UpdateAPIView, RetrieveAPIView)
from rest_framework.response import Response
from . import serializers, models
from django.db.models import Q


class UserRegisterView(CreateAPIView):
    """ api view for creating user account requires username and password"""
    permission_classes = (permissions.AllowAny,)
    model = get_user_model()
    serializer_class = serializers.UserSerializer

    def perform_create(self, serializer):
        """saves user then creates a userdog object and a userpref object
        then sets the settings for the userpref object and saves all changes"""
        print(self.request.data)
        print(self.request.user)
        print(self.request.data['username'])
        serializer.save(user=self.request.user)
        user = get_object_or_404(get_user_model(),
                                 username=self.request.data['username'])
        all_dogs = models.Dog.objects.all()
        for dog in all_dogs:
            user_dog = models.UserDog()
            user_dog.user = user
            user_dog.dog = dog
            user_dog.save()
        pref = models.UserPref()
        pref.user = user
        pref.age = 'b,y,a,s'
        pref.gender = 'm,f'
        pref.size = 'xl,s,m,l'
        pref.save()


class UserPrefView(RetrieveUpdateAPIView):
    """api view for viewing and setting user preferences
    requires age(b,y,a,s) ,gender(m,f),size(xl,s,m,l)"""
    model = models.UserPref
    queryset = models.UserPref.objects.all()
    serializer_class = serializers.UserPrefSerializer

    def get_object(self):
        """gets user preferences base of current user """
        queryset = self.get_queryset()
        print(self.request.user)
        print(self.request.data)
        user_pref = get_object_or_404(queryset, user=self.request.user)
        return user_pref

    def perform_update(self, serializer):
        serializer.save()


class DogLikeView(UpdateAPIView):
    """view for liking or disliking dogs"""
    model = models.UserDog
    serializer_class = serializers.Userdog

    def get_queryset(self):
        return models.UserDog.objects.all()

    def get_object(self):
        """ gets userdog obj or creates one if new dog has been added"""
        dog = get_object_or_404(models.Dog, pk=self.kwargs.get('pk'))
        obj, created = models.UserDog.objects.get_or_create(
            dog=dog,
            user=self.request.user)
        return obj

    def update(self, request, *args, **kwargs):
        """ changes the status of the dog based on kwargs received"""
        print('inside of update', self.kwargs)
        stat = None
        if self.kwargs['status_choice'] == 'liked':

            stat = 'l'
        elif self.kwargs['status_choice'] == 'disliked':
            stat = 'd'

        else:
            stat = 'u'

        instance = self.get_object()
        serializer = self.get_serializer(instance, data={'status': stat},
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        print('end of update ')
        return Response(serializer.data)


class DogUndecidedView(RetrieveAPIView):
    """view for viewing dogs based of being liked or disliked"""
    serializer_class = serializers.DogSerializer

    def get_queryset(self):
        """gets the queryset of dogs based of the user preferences
        and if the dog is liked or not """
        user_preferences = get_object_or_404(models.UserPref,
                                             user=self.request.user)
        age_pref = user_preferences.age.split(',')
        gender_pref = user_preferences.gender.split(',')
        size_pref = user_preferences.size.split(',')
        user_preference_query = models.Dog.objects.filter(
            Q(age__in=list(range(0, 30))
            if 'b' in user_preferences.age
            else [0]) |
            Q(age__in=list(range(30, 60))
            if 'y' in age_pref
            else [0]) |
            Q(age__in=list(range(60, 90))
            if 'a' in age_pref
            else [0]) |
            Q(age__in=list(range(90, 120))
            if 's' in age_pref
            else [0]),
            gender__in=gender_pref
            , size__in=size_pref
        ).order_by('pk')
        if self.kwargs['status'] == 'undecided':
            user_pref_edited = user_preference_query.exclude(
                userdog__status__contains='l')
            return user_pref_edited.exclude(userdog__status__contains='d')
        elif self.kwargs['status'] == 'liked':
            return user_preference_query.filter(userdog__status__contains='l')
        else:
            return user_preference_query.filter(userdog__status__contains='d')

    def get_object(self):
        """returns the next dog with a pk higher then the one received or
        just returns the first dog in the query list"""
        print(self.request.user)
        print(self.request.data)
        print("\n This is the .get() of get object")

        print("\nRequest Data: ", self.request.data)
        print("\nArgs: ", self.args)
        print("\nRequest: ", self.kwargs)
        print("-" * 40)
        pk = self.kwargs['pk']
        dog_on_show = self.get_queryset().filter(id__gt=pk).first()
        if dog_on_show:
            return dog_on_show
        else:
            return self.get_queryset().first()
