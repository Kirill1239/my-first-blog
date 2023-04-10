from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image, User, Account, Images
from django.views import generic




def index(request):
    num_images = Image.objects.all().count()
    num_authors = User.objects.count()

    return render(request, 'index.html', context={'num_images': num_images, 'num_authors': num_authors},)

class ImagesListView(generic.ListView):
    model = Image


def image_view(request):
    if request.method == 'POST':
        form = Images(request.POST, request.FILES)
        print(form)
        print(request)


        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = Images()
    return render(request, 'upload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def display_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        Images = Image.objects.all()
        return render(request, 'image_list.html', {'images': Images})
