from rest_framework.views import APIView, status, Response
from django.http import Http404
from .models import *
from .serializers import *

class CarListCreate(APIView):
    
    def get(self, *args, **kwargs):
        car = CarModel.objects.all()
        serializer = AllCarsSerializers(car, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
class CarViewUpdateDelete(APIView):
    
    def get(self, *args, **kwargs):
        pk:int = kwargs['pk']
        try:
            car = CarModel.objects.get(id=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        serializer =  CarSerializers(car)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, *args, **kwargs):
        pk:int = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(id=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        serializer = CarSerializers(car, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    
    def patch(self, *args, **kwargs):
        pk:int = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(id=pk)
        except CarModel.DoesNotExist:
            raise Http404()
        serializer = CarSerializers(car, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    
    def delete(self, *args, **kwargs):
        pk:int = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(id=pk)
            car.delete()
        except CarModel.DoesNotExist:
            raise Http404()
 
        return Response( status=status.HTTP_200_OK)
    
            
        