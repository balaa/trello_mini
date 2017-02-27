from trelloboard.models import Board, Card, List
from trelloboard.serializers import BoardSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

model_serializers = {"board": "BoardSerializer", "list": "ListSerializer", "card": "CardSerializer"}


def get_model_details(path):
    path = path.split('/')
    model_key = path[3].split('_')
    if model_key[0] in model_serializers:
        return model_key[0].capitalize(), model_serializers[model_key[0]]
    else:
        return None, None


class TrelloList(APIView):
    """
    List all instances, or create a new instance.
    """

    def get(self, request, format=None):
        model_obj, serializer_obj = get_model_details(self.path)
        try:
            obj = model_obj.objects.all()
            serializer = serializer_obj(obj, many=True)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        try:
            model_obj, serializer_obj = get_model_details(self.path)
            serializer = serializer_obj(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_204_NO_CONTENT)


class TrelloDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        model_obj, serializer_obj = get_model_details(self.path)
        try:
            return model_obj.objects.get(pk=pk)
        except model_obj.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            model_obj, serializer_obj = get_model_details(self.path)
            obj = self.get_object(pk)
            serializer = serializer_obj(obj)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        try:
            model_obj, serializer_obj = get_model_details(self.path)
            obj = self.get_object(pk)
            serializer = serializer_obj(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        try:
            obj = self.get_object(pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response(status=status.HTTP_204_NO_CONTENT)
