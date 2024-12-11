from rest_framework import serializers
from .models import OrderItem,Order
from productsApi.serializer import ProductSerializer
from productsApi.models import ProductModel as Product


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_id', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'updated_at', 'total_amount', 'status', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        total_amount = 0
        for item_data in items_data:
            product_id = item_data.pop('product_id')
            product = Product.objects.get(id=product_id)
            item_data['price'] = product.price
            OrderItem.objects.create(order=order, product=product, **item_data)
            total_amount += item_data['price'] * item_data['quantity']
        order.total_amount = total_amount
        order.save()
        return order

