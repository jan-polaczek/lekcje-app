from rest_framework import serializers
from lessons.models import *


class LessonSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(source='student.user.id', read_only=True)
    student_first_name = serializers.CharField(source='student.user.first_name', read_only=True)
    student_last_name = serializers.CharField(source='student.user.last_name', read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'student', 'student_id', 'subject', 'time',
                  'duration', 'student_first_name', 'student_last_name']
        extra_kwargs = {
            'student': {'required': False, 'write_only': True}
        }
