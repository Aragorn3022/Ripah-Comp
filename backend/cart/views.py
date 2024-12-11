from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import  CartItem
from .serializer import  CartItemSerializer
from rest_framework import viewsets, status


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['GET'])
    def total(self):
        cart_items = self.get_queryset()
        total = sum(item.product.price * item.quantity for item in cart_items)
        return Response({'total': total})

    @action(detail=False, methods=['POST'])
    def clear(self):
        self.get_queryset().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

