from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from dataKendaraan.models import Kendaraan
from dataKendaraan.serializers import KendaraanSerializer

# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def kendaraan_list(request):
    if request.method == 'GET':
        kendaraan = Kendaraan.objects.all()
        kendaraan_serializer = KendaraanSerializer(kendaraan, many=True)
        return JSONResponse(kendaraan_serializer.data)
        
    elif request.method == 'PUT':
        kendaraan_data = JSONParser().parse(request)
        kendaraan_serializer = KendaraanSerializer(kendaraan, data=kendaraan_data)
        if kendaraan_serializer.is_valid():
            kendaraan_serializer.save()
            return JSONResponse(kendaraan_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(kendaraan_serializer.errors, status=status.HTTP_404_BAD_REQUEST)

@csrf_exempt
def kendaraan_detail(request, pk):
    try:
        kendaraan = Kendaraan.objects.get(pk=pk)
    except Kendaraan.DoesNotExist:
        return HttpResponse(status=status.Http_404_NOT_FOUND)

    if request.method == 'GET':
        kendaraan_serializer = KendaraanSerializer(kendaraan)
        return JSONResponse(kendaraan_serializer.data)

    elif request.method == 'PUT':
        kendaraan_data = JSONParser().parse(request)
        kendaraan_serializer = KendaraanSerializer(kendaraan, data=kendaraan_data)
        if kendaraan_serializer.is_valid():
            kendaraan_serializers.save()
            return JSONResponse(kendaraan_serializer.data)
        return JSONResponse(kendaraan_serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        kendaraan.delete()
        return HTTPResponse(status=status.HTTP_204_NO_CONTENT)
    