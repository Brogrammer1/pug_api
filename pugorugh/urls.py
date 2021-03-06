from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

from pugorugh.views import UserRegisterView ,UserPrefView,DogUndecidedView,DogLikeView

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^api/user/preferences/$',
        UserPrefView.as_view(),
        name='user_preferences'),
    url(r'^api/user/login/$', obtain_auth_token, name='login-user'),
    url(r'^api/user/$', UserRegisterView.as_view(), name='register-user'),
    url(r'^favicon\.ico$',
        RedirectView.as_view(
            url='/static/icons/favicon.ico',
            permanent=True
        )),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/dog/(?P<pk>\d+)/(?P<status_choice>undecided|liked|disliked)/$',
        DogLikeView.as_view(),
        name='dog_choice'),
    url(r'^api/dog/(?P<pk>-?\d+)/(?P<status>undecided|liked|disliked)/next/$',
        DogUndecidedView.as_view(),
        name='dog_status_view'),
])
