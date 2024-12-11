from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status, viewsets
from .serializer import ProductSerializer
from .models import ProductModel
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer



class AddProductView(APIView):
    isAdmin = IsAdminUser and IsAuthenticated
    if isAdmin:
        def post(self, request, format=None):
            serializer = ProductSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():

                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ListProductsView(APIView):
    def get(self, request):
        Product = ProductModel.objects.all()
        serializer = ProductSerializer(Product, many=True)
        return Response(serializer.data)



class DeleteProductsView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only Staff can delete users

    def delete(self, request, pk):
        try:
            Product = ProductModel.objects.get(pk=pk)
        except ProductModel.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        Product.delete()
        return Response({"Deleted Successfully"},status=HTTP_201_CREATED,)  # Successful deletion, no content


class UpdateProductView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only Staff can update users

    def put(self, request, pk):
        try:
            user = ProductModel.objects.get(pk=pk)
        except ProductModel.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)