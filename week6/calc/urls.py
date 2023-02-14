from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('cards/',views.cards,name='cards'),
    path('posts/',posts,name='posts'),
    path('logout/',logout,name='logout'),
    path('signup/<int:verify>',signup,name='signup'),
    path('adminchoice/',adminchoice,name='adminchoice'),
    path('adminnew/',adminnew,name='adminnew'),
    path('deleteuser/<int:userid>',deleterecord,name='deleterecord'),
    path('updaterecord/<int:userid>', updaterecord, name='updaterecord'),
]


    

