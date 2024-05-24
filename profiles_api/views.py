from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """return list of objects or apiview features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional django view',
        'Gives most control over your application logic',
        'Is maped manually in urls'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request):
        """create hello message with our name"""
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                  serializer.errors,
                  status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """handle updates"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle partial update"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """deleting requests"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""

    serializer_class = serializers.HelloSerializer


    def list(self,request):
        a_viewset = [
           'uses actions (list,create,retrieve,update,partial update)',
           'automatically maps to urls using routers',
           'provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create new hello messsage"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """handle getting oobject by its id"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """handle updating"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """updating part of the object"""
        return Response({'http_method':'PATCH'})


    def destroy(self, request, pk=None):
        """handle removing object"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
