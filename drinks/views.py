from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drinks.models import Drink
from drinks.serializers import DrinkSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def drinks_list(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({"drinks": serializer.data})
    else:
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, pk):
    drink = Drink.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return JsonResponse({"drink": serializer.data})
    elif request.method == 'PUT':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
