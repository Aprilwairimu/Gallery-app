from django.urls import path,re_path
from . import views



urlpatterns=[
    path('',views.home, name='home',),
    path('gallery',views.gallery, name='gallery',),
    path('photo/<pk>/',views.ViewPhoto, name='photo',),
    path('add/',views.addPhoto, name='add',)
]