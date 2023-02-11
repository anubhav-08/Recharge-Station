from django.urls import path

from .views import PlanListView, PlanAPIView

urlpatterns = [
    path('select/<int:_id>', PlanAPIView.as_view()),
    path('<slug:company>', PlanListView.as_view()),
]