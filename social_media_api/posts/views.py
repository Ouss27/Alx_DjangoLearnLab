from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters import rest_framework as filters

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


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


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the list of users that the current user follows
        following = self.request.user.following.all()
        # Get posts from the users the current user follows
        return Post.objects.filter(author__in=following).order_by('-created_at')
