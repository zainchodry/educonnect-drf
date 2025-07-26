from rest_framework import serializers
from .models import User, Course, Enrollment, Review
from accounts.serializer import RegisterSerializer




class CourseSerializer(serializers.ModelSerializer):
    instructor = RegisterSerializer(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
        read_only_fields = ['student']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['student']


