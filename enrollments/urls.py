from django.urls import path
from . views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()


router.register('courses', CourseViewSet, basename='courses'),
router.register('enrollments', EnrollmentViewSet, basename='enrollments'),
router.register('reviews', ReviewViewSet, basename='reviews')



urlpatterns  =  router.urls
