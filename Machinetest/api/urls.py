from django.urls import path
from .views import SignInView
from .views import UserListView

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('users/', UserListView.as_view(), name='user-list'),
]
