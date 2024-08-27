from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('ask-gpt', views.AskGptView.as_view()),
    path('ask-gpt-stream', views.AskGptStreamView.as_view()),
]