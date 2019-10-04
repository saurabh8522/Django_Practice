from django.conf.urls import include
from django.urls import path
from apptwo import views

urlpatterns=[
	path('',views.index,name='index'),
    path('help',views.help,name='help'),
	path('user',views.user,name='user')
]
