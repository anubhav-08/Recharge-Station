from django.urls import path

from .views import PlanListView, PlanAPIView

urlpatterns = [
    path('', PlanListView.as_view()),
    path('select/', PlanAPIView.as_view()),
]