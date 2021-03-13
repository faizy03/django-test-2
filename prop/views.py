from django.shortcuts import render
from .serializers import  PropertySerializer, BuyAPropertySerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Property, BuyAProperty

# Create your views here.

class PropertyAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        props = Property.objects.all()
        serializer = PropertySerializer(props, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PropertySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PropertyDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_object(self, id):
        try:
            ls = Property.objects.get(id=id)
            return ls

        except Property.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        prop = self.get_object(id)
        serializer = PropertySerializer(prop)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        prop = self.get_object(id)
        serializer = PropertySerializer(prop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        prop = self.get_object(id)
        prop.delete()
        msg = "Successfully Deleted"
        return Response(msg, status=status.HTTP_204_NO_CONTENT)