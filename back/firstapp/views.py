from django.shortcuts import render
from datetime import date
from .models import Games1
from firstapp.serialaizers import Games1Serializer
from rest_framework import viewsets
from rest_framework import permissions

def hello(request):
    return render(request, 'index.html', {
        'current_date': date.today()
    })

def gameList(request):
    return render(request, 'games.html', {'data' : {
        'current_date': date.today(),
        'games': Games1.objects.all()
    }})

def GetGame(request, id):
    return render(request, 'game.html', {'data' : {
        'current_date': date.today(),
        'game': Games1.objects.filter(id=id)[0]
    }})

class Games1ViewSet(viewsets.ModelViewSet):
    permission_classes=(permissions.AllowAny,)
    queryset = Games1.objects.all().order_by('id')
    serializer_class = Games1Serializer  # Сериализатор для модели
    # http_method_names = ['get', 'post', 'put', 'patch']
