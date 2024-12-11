from django.contrib.auth.models import User
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status, permissions, viewsets
from .serializers import UserSerializer





class AddUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListUsersView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    isAdmin = IsAdminUser and IsAuthenticated
    if isAdmin:
        def get(self, request):
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    else:
        AddUserView.as_view()

class UserViewSet(viewsets.ModelViewSet):
    ListUsersView.as_view()

class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only Staff can delete users

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)  # Successful deletion, no content


class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only Staff can update users

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)