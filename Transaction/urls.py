from django.urls import path

from .views import TransactionView

urlpatterns = [
    path('checkout/', TransactionView.as_view()),
]