from django import views
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from .ru_taggit import RuTaggedItem

class Ip(models.Model): # наша таблица где будут айпи адреса
	ip = models.CharField(max_length=100)

	def __str__(self):
 		return self.ip

class Anime(models.Model):
	"""Аниме и информация о ней"""
	title = models.CharField(max_length=255, verbose_name="Название")
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
	poster = models.ImageField(upload_to='imgs', verbose_name="Постер")
	date_added = models.DateField(auto_now_add=True, verbose_name="Дата")
	desc = models.TextField(verbose_name="Описание", blank=True, default="")
	source = models.TextField(verbose_name="Ссылка iframe")
	tags = TaggableManager(through=RuTaggedItem, verbose_name='Жанры')
	views = models.ManyToManyField(Ip, related_name="anime_views", blank=True)

	def __str__(self):
		return self.title
	
	def total_views(self):
		return self.views.count()

	def get_absolute_url(self):
		return reverse('anime', kwargs={'anime_slug': self.slug})

	class Meta:
		verbose_name = "Аниме"
		verbose_name_plural = 'Аниме'