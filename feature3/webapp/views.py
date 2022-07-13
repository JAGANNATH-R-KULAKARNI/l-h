from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import featurefunc
from .serializers import featurefuncSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView

from webapp import serializers

class FeatureList(GenericAPIView):
    serializer_class = featurefuncSerializer
    queryset = featurefunc.objects.all()
    lookup_field = 'flagid'

    def get(self, request, format=None):
        feature1 = featurefunc.objects.all()
        serializer = featurefuncSerializer(feature1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = featurefuncSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeatureDetail(GenericAPIView):
    serializer_class = featurefuncSerializer
    queryset = featurefunc.objects.all()

    def get_object(self, pk):
      try:
        return featurefunc.objects.get(pk=pk)
      except featurefunc.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        feature2 = self.get_object(pk)
        serializer = featurefuncSerializer(feature2)
        return Response(serializer.data)    

    def put(self, request, pk, format=None):
        feature2 = self.get_object(pk)
        serializer = featurefuncSerializer(feature2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def patch(self, request, pk, format=None):
        feature2 = self.get_object(pk)
        serializer = featurefuncSerializer(feature2,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, pk, format=None):
        feature1 = self.get_object(pk)
        feature1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

# class API(GenericAPIView):
#  serializers_class = featurefuncSerializer
# @api_view(['GET','POST'])
# def FeatureList(request,format=None):
#      # serializers_class = featurefuncSerializer
#     if request.method == 'GET':
#         feature1 = featurefunc.objects.all()
#         serializer = featurefuncSerializer(feature1, many=True)
#         return Response(serializer.data)

#     elif request.method =='POST':
#         serializer = featurefuncSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return JsonResponse(serializers.errors, status.HTTP_400_BAD_REQUEST)    
 
# @api_view(['GET','PUT','DELETE'])
# def FeatureDetail(request,pk):
#     try:
#         feature2= featurefunc.objects.get(pk=pk)
#     except featurefunc.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = featurefuncSerializer(feature2)
#         return Response(serializer.data)

#     elif request.method=='PUT':
#         serializer = featurefunc(feature2,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    

#     elif request.method =='DELETE':
#         feature2.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)