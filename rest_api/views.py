from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, ststus=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

