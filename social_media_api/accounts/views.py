from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate
from .serializers import RegistrationSerializer, UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import CustomUser 


class RegisterView(APIView):
    def post(self, request):
        # Deserialize the data using RegistrationSerializer
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            # Save the new user
            user = serializer.save()

            # Create the token for the new user
            token, created = Token.objects.get_or_create(user=user)

            # Return the user data along with the token
            return Response({
                "user": UserSerializer(user).data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key})
#         return Response({'error': 'Invalid credentials'}, status=HTTP_400_BAD_REQUEST)


# Follow User View
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user = request.user
        user_to_follow = get_object_or_404(CustomUser, id=user_id)

        # Explicitly using CustomUser.objects.all() here
        all_users = CustomUser.objects.all()

        if user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Add user_to_follow to the current user's following list
        user.following.add(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)


# Unfollow User View
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user = request.user
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

        # Explicitly using CustomUser.objects.all() here
        all_users = CustomUser.objects.all()

        if user == user_to_unfollow:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        # Remove user_to_unfollow from the current user's following list
        user.following.remove(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
