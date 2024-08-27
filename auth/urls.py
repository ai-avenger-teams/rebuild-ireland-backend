"Urls"
from django.urls import path
from . import views


urlpatterns = [
    path('login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('user', views.FetchUser.as_view(), name='user'),
]