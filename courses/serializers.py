from rest_framework import serializers

from . import models

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'created_at',
            'description',
            'published',
            'title',
            'teacher',
            'subject',

        ]
        model= models.Course

class StepSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'title',
            'order',
            'description',
            'course',
        ]
        model= models.Step

class TextSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = [
            'content',
        ]
        model= models.Text

class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = [
            'totalquestions',
        ]
        model= models.Quiz