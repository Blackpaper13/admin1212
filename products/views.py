from django.http import response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from products.models import Product, User
from products.serializers import ProductSerializer
import random

# Create your views here.

class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self,request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response()


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })