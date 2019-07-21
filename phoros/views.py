from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome!')

def gallery(request):
  all_images = Image.objects.all()
  return render(request,'make-gallery/gallery.html',{'all_images': all_images})

