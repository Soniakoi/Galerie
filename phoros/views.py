from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Location,Category
import datetime as dt

# Create your views here.
def welcome(request):
  images = Image.get_all_images()
  return render(request,'welcome.html',{'images':images})

def photos(request):
  all_pics = Image.objects.all()
  return render(request,'all-phoros/photos.html',{'all_pics': all_pics})

def pics(request,pics_id):
  try:
    pics = Pics.objects.get(id=pics_id)
  except DoesNotExist:
    raise Http404()
  return render(request,'all-phoros/pics.html',{'pics':pics})

def search_pics(request):
  if 'category' in request.GET and request.GET['category']:
    search_term = request.GET.get('category')
    searched_pics = Image.search_by_category(search_term)
    
    message = f'{search_term}'

    return render(request,'all-phoros/pics.html',{"message":message, "all_images":searched_pics})

  else:
    message = "You haven't searched for any term."
    return render(request,'all-phoros/photos.html',{"message":message})

def pics_location(request,location):
  pics =  Pics.objects.all()
  try:
    pics_location= Pics.filter_by_location(location)
  except DoesNotExist:
    raise Http404()
  return render(request,'all-phoros/photos.html',{"all_pics":pics_location})
  