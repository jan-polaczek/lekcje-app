from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import datetime

from .models import Lesson
from .serializers import LessonSerializer
from rest_framework import generics, views, status
from .utilities import get_reserved_times


class LessonListCreate(generics.ListCreateAPIView):
    queryset = Lesson.objects.all().order_by('time')
    serializer_class = LessonSerializer

    def get_serializer_context(self):
        response = super().get_serializer_context()
        response['request'].data['student'] = self.request.user.id
        return response


class ReservedTimesView(views.APIView):

    def get(self, request):
        return Response({'reserved_times': get_reserved_times()}, status=status.HTTP_200_OK)


class DeleteLessonView(views.APIView):

    def delete(self, request, lesson_id):
        for lesson in Lesson.objects.all():
            print(lesson.pk)
        try:
            lesson = Lesson.objects.get(pk=lesson_id)
        except Lesson.DoesNotExist:
            return Response('Nie ma takiej lekcji!', status=status.HTTP_404_NOT_FOUND)
        if lesson.time < datetime.datetime.now(datetime.timezone.utc):
            lesson.delete()
            lesson.save()
            return Response('Lekcja usunięta pomyślnie!', status=status.HTTP_200_OK)
        else:
            return Response('Za późno, by odwołać lekcję!', status=status.HTTP_400_BAD_REQUEST)