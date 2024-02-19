from django.urls import path
from .views import NewsView, UsersView, FeedbackView

urlpatterns = [
    path('news/', NewsView().get, name='news'),
    path('users/', UsersView().get, name='users'),
    path('feedback/', FeedbackView().get, name='feedback'),
]
