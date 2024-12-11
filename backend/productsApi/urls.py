from django.urls import path
from .views import AddProductView, ListProductsView, DeleteProductsView, UpdateProductView

urlpatterns = [
    path('add-Products/', AddProductView.as_view()),
    path('Products/', ListProductsView.as_view()),
    path('Products/<int:pk>/', UpdateProductView.as_view()),  # Add pk for update
    path('Products/<int:pk>/delete/', DeleteProductsView.as_view()),  # Add pk for delete
]