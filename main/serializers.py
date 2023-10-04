from rest_framework import serializers
from .models import CarModel



class CarSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    model = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    countPlace = serializers.IntegerField()
    typeCar = serializers.CharField(max_length=50)
    capacityEngine = serializers.FloatField()


    def create(self, validated_data):
        car = CarModel.objects.create(**validated_data)
        return car
    
    def update(self, instance, validated_data):
        for k,v in validated_data.items():
            setattr(instance, k ,v)
        instance.save()
        return instance
    


class AllCarsSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    model = serializers.CharField(max_length=50)
    year = serializers.IntegerField()