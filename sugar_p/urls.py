""" Определяет схемы URL для sugar_p."""

from django.urls import path
from django.views.generic.base import TemplateView

from . import views
from django.contrib.sitemaps.views import sitemap
from sugar_p.sitemap import DynamicViewSitemap, StaticViewSitemap, StaticMainViewSitemap, DynamicTagViewSitemap

sitemaps = {
	'static': StaticViewSitemap,
	'static_main': StaticMainViewSitemap,
	'dynamic_tag': DynamicTagViewSitemap,
	'dynamic': DynamicViewSitemap
}

app_name = 'sugar_p'
urlpatterns = [
	# Домашняя страница
	path('', views.index, name='index'),
	# Страница со списком аниме
	path('anime/', views.animes, name='animes'),
	path('search/', views.search, name='search'),
	path('anime/genre/<slug:tag_slug>/', views.animes_by_genre, name='animes_by_tag'),
	path('anime/<slug:anime_slug>/', views.anime, name='anime'),
	path('anime/top-50', views.top_fifteen, name='top_fifteen'),
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
]