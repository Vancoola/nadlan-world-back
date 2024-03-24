from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.safestring import mark_safe
from lxml import etree
from django.utils.html import format_html
from country_list import countries_for_language

from django.core.exceptions import ValidationError


#class CityModel(models.Model):
   # title = models.CharField("Название", max_length=200)
  #  country = models.ForeignKey('CountryModels', on_delete=models.CASCADE, verbose_name='Страна', related_name="city")

 #   def __str__(self):
        #return self.title

DISTANCES = (
    ('first_line', 'Первая линия'),
    ('500', '500 Метров'),
)

class Cards(models.Model):
    title = CKEditor5Field('Название', max_length=200, config_name='title', blank=False, null=False)
    desc = CKEditor5Field('Краткое описание', max_length=500)
    desc_main = CKEditor5Field(verbose_name='Полное описание')
    country = models.ForeignKey('СountryModels', on_delete=models.CASCADE, verbose_name='Страна', related_name='country', null=True)
    city = models.ForeignKey('CityModels', on_delete=models.CASCADE, verbose_name='Город', related_name='cards', null=True)
    
    bedrooms = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    new_building = models.BooleanField(default=False)
    hot_offers = models.BooleanField(default=False)
    distances_to_the_sea = models.CharField(max_length=255, choices=DISTANCES, default='500')


    def size_warning(self):
        return format_html('<h1 style="color: red">{}</h1>', 'Внимание! Если размер файла превышает 500 кб, то скорость загрузки сайта будет снижена!')
    size_warning.short_description = 'Большие размеры'
    
    def view_image(self):
        if self.image.first() is not None:
            return list(self.image.exclude(id=int(self.image.all().first().id)).values_list('image', flat=True))
        else:
            return []

    def previews(self):
        if self.image.first() is not None:
            return self.image.first().image.name
        else:
            return -1

    def __str__(self):
        parser = etree.HTMLParser()
        tree = etree.fromstring(self.title, parser)
        return etree.tostring(tree, encoding='unicode', method='text').strip()
    
    def decs_return(self):
        parser = etree.HTMLParser()
        tree = etree.fromstring(self.desc, parser)
        return etree.tostring(tree, encoding='unicode', method='text').strip()
    decs_return.short_description = 'Краткое описание'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

class Gallery(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    product = models.ForeignKey(Cards, on_delete=models.CASCADE, related_name='image', null=True, blank=True)
    i_agree = models.BooleanField(verbose_name='Большой размер', default=False)


    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    image_tag.short_description = 'Предпросмотр'

    def size(self):
        if self.image.url is not None:
            return str(round(self.image.size / 1024, 3)) + ' кб'
        else:
            return ""
        
    def __str__(self):
        return self.image.name
    size.short_description = 'Размер'

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Галерея'


class СountryModels(models.Model):
    name = models.CharField('Название страны:', max_length=50)
    country_code = models.CharField('Код страны', max_length=5, blank=True, null=True)

    def clean(self):
        data = super().clean()
        if self.country_code == None:
            try:
                country_names = {name: code for code, name in countries_for_language('ru')}
                self.country_code = country_names[self.name].lower()
                return data
            except:
                raise ValidationError('Поле кода пустое и название страны неверно!')
        return data

    def save(self, *args, **kwargs):
        if self.country_code != None:
            super(СountryModels, self).save(*args, **kwargs)
        else:
            country_names = {name: code for code, name in countries_for_language('ru')}
            self.country_code = country_names[self.name].lower()
            super(СountryModels, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страну'
        verbose_name_plural = 'Страны'

class CityModels(models.Model):
    title = models.CharField("Name", max_length=255)
    country = models.ForeignKey(СountryModels, on_delete=models.CASCADE, verbose_name='Страна', related_name='city')

    def __str__(self):
        return self.title
