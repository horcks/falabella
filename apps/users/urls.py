from django.conf.urls import  include
from apps.users.views import *
from django.urls import path
from django.contrib.auth.decorators import login_required
urlpatterns = [
	path(r'index',login_required(Extended_UserListView.as_view()), name='index'),
	path(r'registration',registration, name='registration'),
	path(r'downloadUsers',downloadUsers, name='downloadUsers'),
]