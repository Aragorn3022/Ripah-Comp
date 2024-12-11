from django.urls import path
from .views import AddUserView, ListUsersView, DeleteUserView, UpdateUserView

urlpatterns = [
    path('add-user/', AddUserView.as_view()),
    path('users/', ListUsersView.as_view()),
    path('users/<int:pk>/', UpdateUserView.as_view()),  # Add pk for update
    path('users/<int:pk>/delete/', DeleteUserView.as_view()),  # Add pk for delete

]