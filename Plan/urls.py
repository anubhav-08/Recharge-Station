from django.urls import path

from .views import PlanListView, PlanAPIView

urlpatterns = [
    path('select/', PlanAPIView.as_view()),
    path('', PlanListView.as_view()),
]