from rest_framework import serializers
from .models import CartItem
from productsApi.serializer  import ProductSerializer
from productsApi.models import ProductModel

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'added_at']

    def create(self, validated_data):
        user = self.context['request'].user
        product_id = validated_data.pop('product_id')
        product = ProductModel.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(
            user=user, product=product, defaults={'quantity': validated_data.get('quantity', 1)}
        )
        if not created:
            cart_item.quantity += validated_data.get('quantity', 1)
            cart_item.save()
        return cart_item

