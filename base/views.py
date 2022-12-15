from multiprocessing import context
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from .models import *
from .aigenerator import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def homePage(request):

    context = {} 

    if request.method == 'POST':
        bookName = request.POST['storyDescription']
        bookContent = request.POST['storyDescription']
        bookImg = request.POST['imgDescription']
        # print(bookImg)

        context['storybookName'] = returnStorybookName(bookName)
        context['storybookStory'] = returnStorybookStory(bookContent)
        context['coverImage'] = returnStorybookImg(bookImg)[0]
        context['image2'] = returnStorybookImg(bookImg)[1]

        return render(request, 'img.html', context)

    return render(request, 'home.html', context)



def ImgPage(request):

    context = {} 
    return render(request, 'img.html', context)