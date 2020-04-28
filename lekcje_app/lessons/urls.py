from django.urls import path
from . import views

urlpatterns = [
    path('', views.LessonListCreate.as_view()),
    path('reserved', views.ReservedTimesView.as_view()),
    path('<int:lesson_id>/', views.DeleteLessonView.as_view()),
]
