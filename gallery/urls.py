from django.urls import path,re_path
from . import views



urlpatterns=[
    path('',views.gallery, name='gallery',),
    path('photo/<str:pk>/',views.ViewPhoto, name='photo',),
    path('add/',views.addPhoto, name='add',)
]