from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.decorators import api_view
from .models import Cat
from .serializers import CatSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


# Create your views here.
def homepage_view(request: HttpRequest):
    return render(request, 'index.html')


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def my_cats_view(request: HttpRequest):
    if request.method == 'POST':
        # создание data = {name , color, year_of_birth}
        cat = Cat(name=request.data['name'], color=request.data['color'],
                  year_of_birth=request.data['year_of_birth'])
        cat.save()
        return Response({"message": "added", "data": request.data})
    if request.method == 'GET':
        # получение списка
        serializer_obj = CatSerializer(Cat.objects.all(), many=True)
        return Response(serializer_obj.data)
    if request.method == 'PUT':
        # полная замена данных data = {old_name , name, color, year_of_birth}
        cat = Cat.objects.get(name=request.data['old_name'])
        cat.name = request.data['name']
        cat.color = request.data['color']
        cat.year_of_birth = request.data['year_of_birth']
        cat.save()
        return Response({"message": "cat updated", "data": request.data})
    if request.method == 'PATCH':
        # частичная замена данных data = {old_name , name, color, year_of_birth}
        data = request.data.copy()
        cat = Cat.objects.get(name=data['old_name'])
        del data['old_name']
        for key in data.keys():
            setattr(cat, key, request.data[key])
        cat.save()
        return Response({"message": "cat updated", "data": request.data})
    if request.method == 'DELETE':
        # удаление
        cat = Cat.objects.get(name=request.data['name'])
        cat.delete()
        return Response({"message": "deleted", "data": request.data})


class ApiCatsView(APIView):
    def post(self, request):
        """
        создание data = {name , color, year_of_birth}
        """
        cat = Cat(name=request.data['name'], color=request.data['color'],
                  year_of_birth=request.data['year_of_birth'])
        cat.save()
        return Response({"message": "added", "data": request.data})

    def get(self, request):
        """
        получение списка
        """
        serializer_obj = CatSerializer(Cat.objects.all(), many=True)
        return Response(serializer_obj.data)

    def put(self, request):
        """
        полная замена данных data = {old_name , name, color, year_of_birth}
        """
        cat = Cat.objects.get(name=request.data['old_name'])
        cat.name = request.data['name']
        cat.color = request.data['color']
        cat.year_of_birth = request.data['year_of_birth']
        cat.save()
        return Response({"message": "cat updated", "data": request.data})

    def patch(self, request):
        """
        частичная замена данных data = {old_name , name, color, year_of_birth}
        """
        data = request.data.copy()
        cat = Cat.objects.get(name=data['old_name'])
        del data['old_name']
        for key in data.keys():
            setattr(cat, key, request.data[key])
        cat.save()
        return Response({"message": "cat updated", "data": request.data})

    def delete(self, request):
        """
        удаление
        """
        cat = Cat.objects.get(name=request.data['name'])
        cat.delete()
        return Response({"message": "deleted", "data": request.data})


class ViewSetCat(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        serializer_obj = CatSerializer(Cat.objects.all(), many=True)
        return Response(serializer_obj.data)

    def create(self, request):
        cat = Cat(name=request.data['name'], color=request.data['color'],
                  year_of_birth=request.data['year_of_birth'])
        cat.save()
        return Response({"message": "added", "data": request.data})

    def update(self, request, name):
        cat = Cat.objects.get(name=name)
        cat.name = request.data['name']
        cat.color = request.data['color']
        cat.year_of_birth = request.data['year_of_birth']
        cat.save()
        return Response({"message": "cat updated", "data": request.data})

    def partial_update(self, request, name):
        data = request.data.copy()
        cat = Cat.objects.get(name=name)
        for key in data.keys():
            setattr(cat, key, request.data[key])
        cat.save()
        return Response({"message": "cat updated", "data": request.data})

    def destroy(self, request, name):
        cat = Cat.objects.get(name=name)
        cat.delete()
        return Response({"message": "deleted", "name": name})
