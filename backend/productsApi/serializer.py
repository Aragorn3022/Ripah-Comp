from django.template.context_processors import request
from rest_framework import serializers
from .models import ProductModel

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'price','description','itemPictureLocation']


    def create(self, validated_data, *args, **kwargs):
        request1 = self.context.get('request')
        isAdmin = request1.user.is_superuser or request1.user.is_staff
        if isAdmin:
            product = ProductModel(
                name=validated_data['name'],
                price=validated_data['price']
            )
            product.save()
            return product
        else:
            raise serializers.ValidationError("Only staff users can create products.")