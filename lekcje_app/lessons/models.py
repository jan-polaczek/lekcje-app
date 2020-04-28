from django.db import models

from accounts.models import Account
from lessons.enums import Subjects


class Lesson(models.Model):
    student = models.ForeignKey(Account, related_name='student', on_delete=models.CASCADE)
    subject = models.CharField(max_length=10, choices=Subjects.choices)
    time = models.DateTimeField()
    duration = models.DurationField()
        
    class Meta:
        order_with_respect_to = 'time'
