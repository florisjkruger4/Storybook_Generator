from multiprocessing import context
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from .models import *
from .aigenerator import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):

    context = {} 

    if request.method == 'POST':
        #bookName = request.POST['storyDescription']
        #bookContent = request.POST['storyDescription']
        bookImg = "someone called " + request.POST['bestfriendsname'] + " with " + request.POST['superpower'] + " powers in " + request.POST['location']

        name = request.POST['bestfriendsname']
        power = request.POST['superpower']
        location = request.POST['location']

        # print(bookImg)

        #context['storybookName'] = returnStorybookName(bookName)
        context['storybookStory'] = returnStorybookStory(name, power, location)
        context['coverImage'] = returnStorybookImg(bookImg)[0]
        context['image2'] = returnStorybookImg(bookImg)[1]

        return render(request, 'html/base/img.html', context)

    return render(request, 'html/base/home.html', context)



def ImgPage(request):

    context = {} 
    return render(request, 'html/base/img.html', context)