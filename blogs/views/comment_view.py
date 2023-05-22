from rest_framework import generics

from blogs.models import Comment
from blogs.serializers import CommentSerializer, CommentsDetailSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.order_by("-id")

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CommentsDetailSerializer
        return CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return CommentsDetailSerializer
        return CommentSerializer
