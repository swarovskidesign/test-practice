from django.urls import path
from .views import Main, Feedback

app_name = 'main'

urlpatterns = [
    path('', Main.as_view(), name='home'),
    path('feedback/', Feedback.as_view(), name='feedback'),
]