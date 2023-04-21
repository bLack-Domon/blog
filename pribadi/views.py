from django.shortcuts import render
from . models import *
# Create your views here.
def PAGE(request):
 data = Profil.objects.all()
 artikel = Artikel.objects.all()

 manda = {
  'd' : data,
  'a' : artikel,
  'menu' : 'blog', 
 }
 return render(request, 'blog.html', manda)


def ABOUT(request):
 data = Profil.objects.all()

 manda = {
  'd' : data,
  'menu' : 'about', 
 }
 return render(request, 'about.html', manda)


def ALBUM(request):
 data = Album.objects.all()

 manda = {
  'd' : data,
  'menu' : 'album', 
 }
 return render(request, 'album.html', manda)


def ARTIKEL(request):
 data = Artikel.objects.all()

 manda = {
  'd' : data,
  'menu' : 'artikel', 
 }
 return render(request, 'artikel.html', manda)


def DETAIL_ARTIKEL(request, id):
 data = Artikel.objects.get(id=id)

 manda = {
  'd' : data,
  'menu' : 'artikel', 
 }
 return render(request, 'detail_artikel.html', manda)


def DETAIL_KHUTBAH(request, id):
 data = Khutbah.objects.get(id=id)

 manda = {
  'd' : data,
  'menu' : 'khutbah', 
 }
 return render(request, 'detail_khutbah.html', manda)


def KHUTBAH(request):
 data = Khutbah.objects.all()

 manda = {
  'd' : data,
  'menu' : 'khutbah', 
 }
 return render(request, 'khutbah.html', manda)