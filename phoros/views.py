from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def gallery(request):
  all_images = Image.objects.all()
  return render(request,'make-gallery/gallery.html',{'all_images': all_images})

