
# from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.allblogs, name='allbogs'),
    path('<int:blog_id >/', views.detail, name='detail'),
]