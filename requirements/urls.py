from django.urls import path, include
from .views import RequirementListView, RequirementDetailView

urlpatterns = [
    path('list/', RequirementListView.as_view()),
    path('detail/<int:pk>/', RequirementDetailView.as_view()),
]