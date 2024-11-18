from os.path import basename

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

r = DefaultRouter()
r.register('categories', views.CategoryViewSet, basename='cate')
r.register('course', views.CourseViewSet, basename='course')


urlpatterns = [
    path('', include(r.urls))
]
