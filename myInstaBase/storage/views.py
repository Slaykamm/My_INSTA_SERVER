from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from storage.serializer import VideoDetailSerializer, VideoViewSerializer, AuthorDetailSerializer, AuthorViewSerializer, CommentsDetailSerializer, CommentsViewSerializer
from storage.models import Video, Author, Comments


# Create your views here.

#Author

class AuthorCreateView(generics.CreateAPIView):
    serializer_class =  AuthorDetailSerializer


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorDetailSerializer
    queryset = Video.objects.all()    


class AuthorViewSet(viewsets.ModelViewSet):
   queryset = Author.objects.all()

   serializer_class = AuthorViewSerializer



   def get_queryset(self, **kwargs):
        id =  self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)  
        email =  self.request.query_params.get('email', None)
        print("test from View Search")

        if id:
            return Author.objects.filter(id=id)

        elif name:
            return Author.objects.filter(name=name)

        elif email:
            return Author.objects.filter(email=email)
            
        else:
            return Author.objects.all()



#Video

class VideoCreateView(generics.CreateAPIView):
    serializer_class =  VideoDetailSerializer


class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VideoDetailSerializer
    queryset = Video.objects.all()    


class VideoViewSet(viewsets.ModelViewSet):
   queryset = Video.objects.all()

   serializer_class = VideoViewSerializer



   def get_queryset(self, **kwargs):
        id =  self.request.query_params.get('id', None)
        title = self.request.query_params.get('title', None)  
        author =  self.request.query_params.get('author', None)
        rating = self.request.query_params.get('rating', None)  
        create_at = self.request.query_params.get('create_at', None)  


        if id:
            return Video.objects.filter(id=id)

        elif title:
            return Video.objects.filter(title=title)

        elif author:
            return Video.objects.filter(author=author)

        elif rating:
            return Video.objects.filter(rating=rating)

        elif create_at:
            return Video.objects.filter(create_at=create_at)

        else:
            return Video.objects.all()



#Comments

class CommentsCreateView(generics.CreateAPIView):
    serializer_class =  CommentsDetailSerializer


class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsDetailSerializer
    queryset = Comments.objects.all()    


class CommentsViewSet(viewsets.ModelViewSet):
   queryset = Comments.objects.all()

   serializer_class = CommentsViewSerializer



   def get_queryset(self, **kwargs):
        id =  self.request.query_params.get('id', None)
        author =  self.request.query_params.get('author', None)
        video = self.request.query_params.get('video', None)  
        rating = self.request.query_params.get('rating', None)  
        create_at = self.request.query_params.get('create_at', None)  


        if id:
            return Comments.objects.filter(id=id)

        elif author:
            return Comments.objects.filter(author=author)

        elif video:
            return Comments.objects.filter(video=video)

        elif rating:
            return Comments.objects.filter(rating=rating)

        elif create_at:
            return Comments.objects.filter(create_at=create_at)
            
        else:
            return Comments.objects.all()
