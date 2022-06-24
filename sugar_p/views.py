from django.shortcuts import render
from .models import Anime, Ip
from taggit.models import Tag
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from random import sample

def random_animes(anime):
	"""Возвращает 3 рандомные аниме"""
	my_ids = anime.objects.values_list('id', flat=True)
	my_ids = list(my_ids)
	rand_ids = sample(my_ids, 3)
	random_animes = anime.objects.filter(id__in=rand_ids)
	return random_animes

def get_client_ip(request):
	"""Получает IP и возвращает его"""
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
	return ip

def index(request):
	"""Домашняя страница приложения Sugar Prince"""
	random_anime = random_animes(Anime)
	context = {'random_animes': random_anime}
	return render(request, 'sugar_p/index.html', context)

def animes(request, tag_slug=None):
	"""Выводит список аниме"""
	animes = Anime.objects.order_by('-date_added')
	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug) 
		animes = animes.filter(tags__in=[tag])

	page = request.GET.get('page')
	paginator = Paginator(animes, 20)
	try:
		animes = paginator.page(page)
	except PageNotAnInteger:
		animes = paginator.page(1)
	except EmptyPage:
		animes = paginator.page(paginator.num_pages)
	random_anime = random_animes(Anime)
	all_tags = Tag.objects.all()
	context = {'animes': animes, 'page': page, 'tag': tag, 'random_animes': random_anime,
														'all_tags': all_tags}
	return render(request, 'sugar_p/animes.html', context)

def animes_by_genre(request, tag_slug=None):
	"""Выводит список аниме"""
	animes = Anime.objects.order_by('-date_added')
	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug) 
		animes = animes.filter(tags__in=[tag])

	page = request.GET.get('page')
	paginator = Paginator(animes, 20)
	try:
		animes = paginator.page(page)
	except PageNotAnInteger:
		animes = paginator.page(1)
	except EmptyPage:
		animes = paginator.page(paginator.num_pages)
	random_anime = random_animes(Anime)
	all_tags = Tag.objects.all()
	context = {'animes': animes, 'page': page, 'tag': tag, 'random_animes': random_anime,
														'all_tags': all_tags}
	return render(request, 'sugar_p/animesgenre.html', context)

def search(request):
	"""Выводит список аниме по запросу в поисковике"""
	search_query = request.GET.get("q")

	if search_query == None:
		animes = Anime.objects.order_by('-date_added')
	else:
		animes = Anime.objects.filter(title__icontains=search_query).order_by('-date_added')

	page = request.GET.get('page')
	paginator = Paginator(animes, 2)
	try:
		animes = paginator.page(page)
	except PageNotAnInteger:
		animes = paginator.page(1)
	except EmptyPage:
		animes = paginator.page(paginator.num_pages)
	
	all_tags = Tag.objects.all()
	random_anime = random_animes(Anime)
	context = {'animes': animes, 'page': page, 'search_q': search_query,
							'random_animes': random_anime, 'all_tags': all_tags}
	return render(request, 'sugar_p/search.html', context)

def anime(request, anime_slug):
	"""Выводит аниме"""
	anime = get_object_or_404(Anime, slug=anime_slug)

	ip = get_client_ip(request)

	if Ip.objects.filter(ip=ip).exists():
		anime.views.add(Ip.objects.get(ip=ip))
	else:
		Ip.objects.create(ip=ip)
		anime.views.add(Ip.objects.get(ip=ip))
	random_anime = random_animes(Anime)
	context = {'anime': anime, 'random_animes': random_anime}
	return render(request, 'sugar_p/anime.html', context)

def top_fifteen(request):
	"""Выводит топ 50 аниме"""
	animes = Anime.objects.order_by('-views')[:50]
	page = request.GET.get('page')
	paginator = Paginator(animes, 20)
	try:
		animes = paginator.page(page)
	except PageNotAnInteger:
		animes = paginator.page(1)
	except EmptyPage:
		animes = paginator.page(paginator.num_pages)
	random_anime = random_animes(Anime)
	all_tags = Tag.objects.all()
	context = {'animes': animes, 'page': page, 'random_animes': random_anime,
														'all_tags': all_tags}
	return render(request, 'sugar_p/top_fifteen.html', context)