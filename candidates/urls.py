from django.urls import path, include
from .views import CandidateCreateAPIView, CandidateDetailView

urlpatterns = [
    path('create/', CandidateCreateAPIView.as_view()),
    path('detail/<int:pk>/', CandidateDetailView.as_view()),
]