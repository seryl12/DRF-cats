from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cat
from .serializers import CatSerializer
from .forms import CatForm


# Create your views here.
def homepage_view(request: HttpRequest):
    return render(request, 'index.html')


@api_view(['GET', 'POST'])
def cats_view(request: HttpRequest):
    if request.method == 'POST':
        cat = Cat(name=request.data['name'], color=request.data['color'],
                  year_of_birth=request.data['year_of_birth'])
        cat.save()
        return Response({"message": "added", "data": request.data})
    serializer_obj = CatSerializer(Cat.objects.all(), many=True)
    return Response(serializer_obj.data)
