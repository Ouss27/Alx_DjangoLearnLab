from rest_framework import viewsets, permissions, generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters import rest_framework as filters

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import status
from django.shortcuts import get_object_or_404
from accounts.models import CustomUser


class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search by title
    content = filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search by content

    class Meta:
        model = Post
        fields = ['title', 'content']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter

    def perform_create(self, serializer):
        # Automatically set the author to the current user when creating a post
        serializer.save(author=self.request.user)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set the author to the current user when creating a comment
        serializer.save(author=self.request.user)


class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get the current user
        user = request.user

        # Get the list of users the current user follows
        following_users = user.following.all()

        # Get posts from the users that the current user follows
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)