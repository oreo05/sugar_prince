from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Anime
from taggit.models import Tag



class StaticViewSitemap(Sitemap):
	priority = 1.0
	changefreq = 'daily'
	
	def items(self):
		return ['index']

	def location(self, item):
		return reverse(f"sugar_p:{item}")

class StaticMainViewSitemap(Sitemap):
	priority = 0.8
	changefreq = 'daily'

	def items(self):
		return ['animes', 'top_fifteen']

	def location(self, item):
		return reverse(f"sugar_p:{item}")


class DynamicTagViewSitemap(Sitemap):
	priority = 0.8
	changefreq = 'weekly'
	
	def items(self):
		return Tag.objects.all()

	def location(self, item):
		return reverse(f"sugar_p:animes_by_tag", kwargs={"tag_slug": item.slug})


class DynamicViewSitemap(Sitemap):
	changefreq = 'weekly'
	priority = 0.6

	def items(self):
		return Anime.objects.all()

	def location(self, item):
		# return reverse('news-page', args=[item.pk])
		return 	reverse(f"sugar_p:anime", kwargs={'anime_slug': item.slug})     #f'/anime/{item.slug}/'