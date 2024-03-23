from typing import Any
from django import forms
from .models import Gallery
from django.core.exceptions import ValidationError


class GalleryForms(forms.ModelForm):
    def clean(self):
        data = super().clean()
        if 'image' not in data:
            raise ValidationError('')
        if data['image'].size/1024 > 500 and data['i_agree'] != True:
            raise ValidationError('Есть неотмеченные большие файлы!')
        return data
        
    class Meta:
        model = Gallery
        fields = '__all__'