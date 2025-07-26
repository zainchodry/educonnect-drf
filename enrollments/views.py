from django.shortcuts import render
from rest_framework import viewsets, permissions
from . models import *
from . serializer import *
from rest_framework.response import Response
from rest_framework.decorators import action
from . permissions import *



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


    def perform_create(self, serializer):
        return serializer.save(instructor = self.request.user)
    



    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsInstructor()]
        return [permissions.AllowAny()]
    


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(student=self.request.user)

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)