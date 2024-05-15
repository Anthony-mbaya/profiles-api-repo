from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""
    def get(self, request, format=None):
        """return list of objects or apiview features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional django view',
        'Gives most control over your application logic',
        'Is maped manually in urls'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
