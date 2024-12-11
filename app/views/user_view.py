# user_view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from app.models.users import CustomUser
from app.serializers.user_serializer import RegisterSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Handle user registration
class RegisterView(APIView):
    def post(self, request):
        user_data = request.data
        serializer = RegisterSerializer(data=user_data)
        try:
            serializer.is_valid(raise_exception=True)  # Validate the data, raise an exception if invalid
            serializer.save()  # Save the new user to the database
            logger.info(f"User registered successfully with username: {user_data.get('username')}")
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        except Exception as error:
            logger.error(f"Registration failed with errors: {error}")
            return Response({'errors': str(error)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

# Handle user login and token generation
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=email, password=password)  # Authenticate user with email and password
        if user is not None:
            refresh = RefreshToken.for_user(user)  # Generate refresh and access tokens for the authenticated user
            logger.info(f"User authenticated successfully: {email}")
            return Response({
                'access': str(refresh.access_token),  # Access token
                'refresh': str(refresh)  # Refresh token
            }, status=status.HTTP_200_OK)
        else:
            logger.warning(f"Authentication failed for email: {email}")
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# List all users (only accessible by authenticated users)
class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()  # Queryset to get all users from the database
    serializer_class = RegisterSerializer  # Serializer to convert user data to JSON
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get(self, request, *args, **kwargs):
        logger.info(f"User {request.user.email} requested the list of all users")
        return super().get(request, *args, **kwargs)  # Call the parent class's get method to return the list

# Get, update, or delete a specific user's details
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get(self, request, user_id=None):
        # Get user details by user ID or the current logged-in user
        user = get_object_or_404(CustomUser, pk=user_id) if user_id else request.user
        serializer = RegisterSerializer(user)  # Serialize the user data
        logger.info(f"User {request.user.email} requested details for user ID: {user_id if user_id else 'self'}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id=None):
        user = request.user
        serializer = RegisterSerializer(user, data=request.data, partial=True)  # Use partial=True to allow partial updates
        try:
            serializer.is_valid(raise_exception=True)  # Validate the data, raise an exception if invalid
            serializer.save()  # Save the updated user details
            logger.info(f"User {request.user.email} updated details successfully")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            logger.error(f"Update failed for user {request.user.email} with errors: {error}")
            return Response({'errors': str(error)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request, user_id=None):
        user = request.user
        user.delete()  # Delete the user from the database
        logger.info(f"User {request.user.email} deleted their account successfully")
        return Response({'message': 'User deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



