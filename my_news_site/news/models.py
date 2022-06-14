import datetime

from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_of_change = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    snapshot = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_new', kwargs={"new_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-creation_date']
        
    def was_published_recently(self):
        if self.is_published:
            return timezone.now() - datetime.timedelta(days=7) <= self.creation_date <= timezone.now()

            


class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']