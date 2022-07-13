from rest_framework import serializers
from .models import featurefunc


# class featurefuncSerializer(serializers.Serializer):
#     class Meta:
#         model = featurefunc
#         fields = '__all__'

class featurefuncSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    tags = serializers.CharField(max_length=25)
    lastupdateby = serializers.CharField(max_length=25)
    updateat = serializers.DateTimeField()
    flagid = serializers.IntegerField()
    enable = serializers.BooleanField()


    def create(self, validated_data):
        return featurefunc.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.lastupdateby = validated_data.get('lastupdateby', instance.lastupdateby)
        instance.updateat = validated_data.get('updateat', instance.updateat)
        instance.flagid = validated_data.get('flagid', instance.flagid)
        instance.enable = validated_data.get('enable', instance.enable)
        instance.save()
        return instance