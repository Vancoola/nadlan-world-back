from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .serializer import CardsSerializer
from .models import Cards, Gallery
from rest_framework.response import Response
from django.http import FileResponse
from urllib.parse import unquote
from django.db.models import Q
# Create your views here.

class CardsVS(ViewSet):
    def create(self, request):
        if request.POST.get('ctn') != None: #and Cards.objects.filter(country__country_code=request.data['ctn']).exists():
            par = Q(country__country_code=request.data['ctn'])
            if request.POST.get('bedrooms') != None:
                 par &= Q(bedrooms__gte=request.POST.get('bedrooms'))
            if request.POST.get('new_building') != None:
                 par &= Q(new_building=request.POST.get('new_building'))
            if request.POST.get('hot_offers') != None:
                 par &= Q(hot_offers=request.POST.get('hot_offers'))
            if request.POST.get('distances_to_the_sea') != None:
                 par &= Q(distances_to_the_sea=request.POST.get('distances_to_the_sea'))
            if request.POST.get('min_price') != None:
                 par &= Q(price__gte=request.POST.get('min_price'))
            if request.POST.get('max_price') != None:
                 par &= Q(price__lte=request.POST.get('max_price'))
            serializer = CardsSerializer(instance=Cards.objects.filter(par), many=True)
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
