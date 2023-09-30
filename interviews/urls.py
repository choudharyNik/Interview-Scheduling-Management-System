from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.InterviewScheduleList.as_view()),
    path('schedule/<int:pk>/', views.InterviewScheduleDetail.as_view()),
    path('observation/', views.InterviewObservationList.as_view()),
    path('observation/<int:pk>/', views.InterviewObservationDetail.as_view()),
]