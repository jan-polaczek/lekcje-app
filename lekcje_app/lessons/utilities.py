from django.db import models
from datetime import timedelta, time

from .models import Lesson


def get_reserved_times():
    lessons = Lesson.objects.all()
    result = []
    for lesson in lessons:
        lesson_time = lesson.time
        duration = lesson.duration
        result.append(lesson_time)
        result.append(lesson_time - timedelta(minutes=30))
        total_add_time = timedelta(minutes=30)
        while total_add_time < duration:
            result.append(lesson_time + total_add_time)
            total_add_time += timedelta(minutes=30)
    return result
