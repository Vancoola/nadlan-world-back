from rest_framework import serializers
from .models import Cards




class CardsSerializer(serializers.ModelSerializer):
    preview = serializers.CharField(source='previews')
    images = serializers.ListField(source='view_image')
    class Meta:
        model = Cards
        fields = ['id', 'title', 'desc', 'desc_main', 'preview', 'images']