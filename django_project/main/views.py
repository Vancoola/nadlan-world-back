from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .serializer import CardsSerializer
from .models import Cards, Gallery
from rest_framework.response import Response
from django.http import FileResponse
from urllib.parse import unquote
# Create your views here.

class CardsVS(ViewSet):
    def create(self, request):
        if request.POST.get('ctn') != None and Cards.objects.filter(country__country_code=request.data['ctn']).exists():
            serializer = CardsSerializer(instance=Cards.objects.filter(country__country_code=request.data['ctn']), many=True)
        else:
             return Response({'detail': '404 NOT FOUND'}, status=404)
        return Response (serializer.data)
    

class GalleryVS(ViewSet):
    def create(self, request):
            if request.POST.get('id') != None and Gallery.objects.filter(id=request.data['id']).exists():
                obj = Gallery.objects.get(id=request.data['id'])
                url = list({obj.image.url})[0][7:]
                f = open(f'/home/django/django_project/image/{unquote(url)}', 'rb')
                return FileResponse(f)
            else:
                return Response({'detail': 'error'})
