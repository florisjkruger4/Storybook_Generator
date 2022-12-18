from multiprocessing import context
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from .models import *
from .aigenerator import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

def fantasyPage(request):

    NameDictionary = {"best friend":"IMG1", "mother":"IMG2", "spouse":"IMG3"}
    QuestDictionary = {"looking for treasure":"IMG", "saving the planet":"IMG2","making friends":"IMG3"}
    LocationDictionary = {"the moon":"IMG1", "middle earth":"IMG2", "atlantis":"IMG3"}

    NameKeys = sorted(NameDictionary.keys())
    QuestKeys = sorted(QuestDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    RandomKey1 = []
    RandomKey2 = []
    RandomKey3 = []

    for counter in range(2):
        index = randint(0,2)
        RandomNounKey = NameKeys[index]
        RandomTraitKey = QuestKeys[index]
        RandomLocationKey = LocationKeys[index]
        RandomKey1.append(RandomNounKey)
        RandomKey2.append(RandomTraitKey)
        RandomKey3.append(RandomLocationKey)

    re_index = randint(0,1)
    context = {
            "name":RandomKey1[re_index],
            "quest":RandomKey2[re_index],
            "location":RandomKey3[re_index],
        } 

    if request.method == 'POST':
        
        #bookImg = "someone called " + request.POST['bestfriendsname'] + " with " + request.POST['superpower'] + " powers in " + request.POST['location']
        #bookName = bookImg
        
        name = request.POST['bestfriendsname']
        quest = request.POST['superpower']
        location = request.POST['location']

        context = {
            "name":name,
            "quest":quest,
            "location":location,
        }

        #context['storybookName'] = returnStorybookName(bookName)
        context['storybookStory'] = returnFantasyStorybookStory(name, quest, location)
        #context['coverImage'] = returnStorybookImg(bookImg)[0]
        #context['image2'] = returnStorybookImg(bookImg)[1]

        return render(request, 'html/base/img.html', context)

    return render(request, 'html/base/home.html', context)



def sportsPage(request):

    NameDictionary = {"best friend":"IMG1", "mother":"IMG2", "spouse":"IMG3"}
    QuestDictionary = {"superpower":"IMG", "fear":"IMG2","loved":"IMG3"}
    LocationDictionary = {"camp":"IMG1", "high school":"IMG2", "church":"IMG3"}

    NameKeys = sorted(NameDictionary.keys())
    QuestKeys = sorted(QuestDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    RandomKey1 = []
    RandomKey2 = []
    RandomKey3 = []

    for counter in range(2):
        index = randint(0,2)
        RandomNounKey = NameKeys[index]
        RandomTraitKey = QuestKeys[index]
        RandomLocationKey = LocationKeys[index]
        RandomKey1.append(RandomNounKey)
        RandomKey2.append(RandomTraitKey)
        RandomKey3.append(RandomLocationKey)

    re_index = randint(0,1)
    context = {
            "name":RandomKey1[re_index],
            "power":RandomKey2[re_index],
            "location":RandomKey3[re_index],
        } 

    if request.method == 'POST':
        
        bookImg = "someone called " + request.POST['bestfriendsname'] + " with " + request.POST['superpower'] + " powers in " + request.POST['location']
        bookName = bookImg
        
        name = request.POST['bestfriendsname']
        power = request.POST['superpower']
        location = request.POST['location']

        context = {
            "name":name,
            "power":power,
            "location":location,
        }

        context['storybookName'] = returnStorybookName(bookName)
        context['storybookStory'] = returnFantasyStorybookStory(name, power, location)
        context['coverImage'] = returnStorybookImg(bookImg)[0]
        context['image2'] = returnStorybookImg(bookImg)[1]

        return render(request, 'html/base/img.html', context)

    return render(request, 'html/base/home.html', context)



def adventurePage(request):

    NameDictionary = {"best friend":"IMG1", "mother":"IMG2", "spouse":"IMG3"}
    QuestDictionary = {"superpower":"IMG", "fear":"IMG2","loved":"IMG3"}
    LocationDictionary = {"camp":"IMG1", "high school":"IMG2", "church":"IMG3"}

    NameKeys = sorted(NameDictionary.keys())
    QuestKeys = sorted(QuestDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    RandomKey1 = []
    RandomKey2 = []
    RandomKey3 = []

    for counter in range(2):
        index = randint(0,2)
        RandomNounKey = NameKeys[index]
        RandomTraitKey = QuestKeys[index]
        RandomLocationKey = LocationKeys[index]
        RandomKey1.append(RandomNounKey)
        RandomKey2.append(RandomTraitKey)
        RandomKey3.append(RandomLocationKey)

    re_index = randint(0,1)
    context = {
            "name":RandomKey1[re_index],
            "power":RandomKey2[re_index],
            "location":RandomKey3[re_index],
        } 

    if request.method == 'POST':
        
        bookImg = "someone called " + request.POST['bestfriendsname'] + " with " + request.POST['superpower'] + " powers in " + request.POST['location']
        bookName = bookImg
        
        name = request.POST['bestfriendsname']
        power = request.POST['superpower']
        location = request.POST['location']

        context = {
            "name":name,
            "power":power,
            "location":location,
        }

        context['storybookName'] = returnStorybookName(bookName)
        context['storybookStory'] = returnFantasyStorybookStory(name, power, location)
        context['coverImage'] = returnStorybookImg(bookImg)[0]
        context['image2'] = returnStorybookImg(bookImg)[1]

        return render(request, 'html/base/img.html', context)

    return render(request, 'html/base/home.html', context)



def spookyPage(request):

    NameDictionary = {"best friend":"IMG1", "mother":"IMG2", "spouse":"IMG3"}
    QuestDictionary = {"superpower":"IMG", "fear":"IMG2","loved":"IMG3"}
    LocationDictionary = {"camp":"IMG1", "high school":"IMG2", "church":"IMG3"}

    NameKeys = sorted(NameDictionary.keys())
    QuestKeys = sorted(QuestDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    RandomKey1 = []
    RandomKey2 = []
    RandomKey3 = []

    for counter in range(2):
        index = randint(0,2)
        RandomNounKey = NameKeys[index]
        RandomTraitKey = QuestKeys[index]
        RandomLocationKey = LocationKeys[index]
        RandomKey1.append(RandomNounKey)
        RandomKey2.append(RandomTraitKey)
        RandomKey3.append(RandomLocationKey)

    re_index = randint(0,1)
    context = {
            "name":RandomKey1[re_index],
            "power":RandomKey2[re_index],
            "location":RandomKey3[re_index],
        } 

    if request.method == 'POST':
        
        bookImg = "someone called " + request.POST['bestfriendsname'] + " with " + request.POST['superpower'] + " powers in " + request.POST['location']
        bookName = bookImg
        
        name = request.POST['bestfriendsname']
        power = request.POST['superpower']
        location = request.POST['location']

        context = {
            "name":name,
            "power":power,
            "location":location,
        }

        context['storybookName'] = returnStorybookName(bookName)
        context['storybookStory'] = returnFantasyStorybookStory(name, power, location)
        context['coverImage'] = returnStorybookImg(bookImg)[0]
        context['image2'] = returnStorybookImg(bookImg)[1]

        return render(request, 'html/base/img.html', context)

    return render(request, 'html/base/home.html', context)



def ImgPage(request):

    context = {} 
    return render(request, 'html/base/img.html', context)