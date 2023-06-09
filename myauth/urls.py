from django.urls import path
from .views import (
    UserView,
    UserDetailView,
    UserRegistrationView,
    UserLogoutView,
    UserRoleView,
    UserRoleDetailView
)

urlpatterns = [
    path('regis/', UserRegistrationView.as_view(), name='user-regis'),
    path('users/', UserView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(),
         name='user-retrieve-update-destroy'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('role/', UserRoleView.as_view(), name='user-role'),
    path('role/<int:pk>/', UserRoleDetailView.as_view(), name='user-role-detail'),

]
