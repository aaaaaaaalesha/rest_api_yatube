from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.filters import SearchFilter

from .serializers import (
    GroupSerializer,
    CommentSerializer,
    PostSerializer,
    FollowSerializer,
)
from .permissions import IsAuthorOrReadOnly

from posts.models import Group, Post


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    )

    def __get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.__get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.__get_post()
        )


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
