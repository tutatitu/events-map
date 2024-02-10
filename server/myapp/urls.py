from django.urls import path
from .views import NewsViewSet, UsersViewSet, FeedbackViewSet

urlpatterns = [
    path('news/', NewsViewSet.as_view, name='news'),
    path('users/', UsersViewSet.as_view, name='users'),
    path('feedback/', FeedbackViewSet.as_view, name='feedback'),
]
