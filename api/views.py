from rest_framework import status
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Inventory, Order, OrderDetail
from .serializers import InventorySerializer, OrderSerializer, OrderDetailSerializer


class inventory_list(APIView):

    def get(self, request, format=None):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class inventory_item(APIView):

    def get_object(self, name):
        try:
            return Inventory.objects.filter(name__icontains=name)
        except Inventory.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        name = self.request.query_params.get('name')
        item = self.get_object(name)
        serializer = InventorySerializer(item, many=True)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        item = self.get_object(name)
        serializer = InventorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        item = self.get_object(name)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class addOrder(APIView):

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class addOrderDetail(APIView):

    def post(self, request, format=None):
        cart = request.data
        for item in cart:
            serializer = OrderDetailSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'detail': 'order added successfully'}, status=status.HTTP_200_OK)
