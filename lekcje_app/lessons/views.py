from rest_framework.permissions import AllowAny

from .models import Lesson
from .serializers import LessonSerializer
from rest_framework import generics


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        response = super().get_serializer_context()
        response['request'].data['student'] = self.request.user.id
        return response
