# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import UserSerializer, GroupSerializer, BookSerializer, AuthorSerializer, PhotoSerializer, CustomerSerializer 
from .models import Book, Author, Photo, Customer
from rest_framework.generics import DestroyAPIView

########################### User Requests ##############################################

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class HomeView(APIView):
    permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated, )
    def get(self, request):
       content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
       return Response(content)

class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
        try:
             refresh_token = request.data["refresh_token"]
             token = RefreshToken(refresh_token)
             token.blacklist()
             return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class RegisterCustomerAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        print('-------------------------')
        print(request.data.get('location'))
        print('-------------------------')
        serializerUser = UserSerializer(data=request.data,context={'request': request})
        if serializerUser.is_valid():
            serializerUser.save()
            print('-------------------------')
            print(serializerUser.data)
            print('-------------------------')
            if(serializerUser.is_valid):
                serializer = CustomerSerializer(data={
                    'user': serializerUser.data, 'location': request.data.get('location')},context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else: 
                    print(serializer.errors)
                    return Response(serializerUser.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print(serializerUser.errors)
            return Response(serializerUser.errors, status=status.HTTP_400_BAD_REQUEST)


########################### Book Requests ##############################################

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
   
class CreateBookAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = BookSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateBookAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        instance_id = kwargs.get('pk')
        print(instance_id)
        instance = Book.objects.get(pk=instance_id)
        
        # Assuming you have a serializer for your model
        serializer = BookSerializer(instance, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteBookAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

########################### Author Requests ##############################################

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

########################### Author Requests ##############################################

class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]
    