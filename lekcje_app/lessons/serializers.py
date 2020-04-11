from rest_framework import serializers
from lessons.models import *


class LessonSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(source='student.user.id', read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'student', 'student_id', 'subject', 'time', 'duration']
        extra_kwargs = {
            'student': {'required': False, 'write_only': True}
        }
