# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import UserSerializer, GroupSerializer, BookSerializer, AuthorSerializer, PhotoSerializer, CustomerSerializer 
from .models import Book, Author, Photo, Customer
from rest_framework.generics import DestroyAPIView, RetrieveAPIView, CreateAPIView
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
########################### User Requests ##############################################

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
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
            refresh_token = request.body["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserCreateAPIView(CreateAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        # print(queryset)

class CustomerCreateAPIView(CreateAPIView):
        queryset = Customer.objects.all()
        serializer_class = CustomerSerializer
        
        def perform_create(self, serializer):
            # Extract user data from the request
            user_data = self.request.data.get('user', {})
            
            # Create a User instance
            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid():
                user_instance = user_serializer.save()
                
                # Create YourModel instance with the ForeignKey to the created User
                serializer.save(user=user_instance)
            else:
                # Handle invalid user data
                self.response.status_code = status.HTTP_400_BAD_REQUEST
                self.response.data = user_serializer.errors
 
class CustomerRetrieveAPIView(RetrieveAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get the username and password from the request
        username = kwargs.get('username')
        password = kwargs.get('password')
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            # User is authenticated, get the YourModel instance associated with the user
            customer_instance = Customer.objects.filter(user=user).first()
            print(customer_instance)
            if customer_instance is not None:
                serializer = self.get_serializer(customer_instance)
                print(serializer.data)
                return Response(serializer.data)
            else:
                return Response({'detail': 'YourModel instance not found for this user.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'detail': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
     
########################### Book Requests ##############################################

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
   
class BookDetail(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   
class CreateBookAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def perform_create(self, serializer):
        # Extract user data from the request
        customer_id = self.request.data.get('customer_id', {})
        author_id = self.request.data.get('author_id', {})
        customer_instance = Customer.objects.filter(id=customer_id).first()
        author_instance = Author.objects.filter(id=author_id).first()
        serializer.save(customer=customer_instance, author = author_instance)

class UpdateBookAPIView(APIView):
    def post(self, request, *args, **kwargs):
        instance_id = kwargs.get('pk')
        instance = Book.objects.get(pk=instance_id)
        
        author_id = self.request.data.get('author_id', {})
        author_instance = Author.objects.filter(id=author_id).first()
        
        # Assuming you have a serializer for your model
        serializer = BookSerializer(instance, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            Book.objects.filter(pk=instance_id).update(author=author_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
        
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
    