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

    prompt1 = "Enter a name!"
    prompt2 = "Enter your story's quest!"
    prompt3 = "Enter a location!"

    NameDictionary = {"Best Friend":"IMG1", "Parent":"IMG2", "Sibling":"IMG3", "Celebrity":"IMG4", "Movie Character":"IMG5",}
    QuestDictionary = {"Looking for treasure":"IMG", "Saving the planet":"IMG2", "Stopping a zombie apocalypse":"IMG3", "Rescuing a princess":"IMG4", "Helping an old lady cross the road":"IMG5"}
    LocationDictionary = {"an Alien Planet":"IMG1", "Middle Earth":"IMG2", "Atlantis":"IMG3", "Gotham City":"IMG4", "Hogwarts":"IMG5"}

    NameKeys = sorted(NameDictionary.keys())
    QuestKeys = sorted(QuestDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    RandomKey1 = []
    RandomKey2 = []
    RandomKey3 = []

    counter = 0
    for counter in range(2):
        index = randint(0,4)
        RandomNameKey = NameKeys[index]
        RandomQuestKey = QuestKeys[index]
        RandomLocationKey = LocationKeys[index]
        RandomKey1.append(RandomNameKey)
        RandomKey2.append(RandomQuestKey)
        RandomKey3.append(RandomLocationKey)

    re_index = randint(0,1)
    context = {
            "prompt1":prompt1,
            "prompt2":prompt2,
            "prompt3":prompt3,
            "name":RandomKey1[re_index],
            "contained":RandomKey2[re_index],
            "location":RandomKey3[re_index],
        } 


    if request.method == 'POST':
        
        bookName = "a protagonist called " + request.POST['bestfriendsname'] + " on a quest " + request.POST['superpower'] + " based in " + request.POST['location']
        bookImg = bookName
        
        name = request.POST['bestfriendsname']
        quest = request.POST['superpower']
        location = request.POST['location']

        context = {
            "name":name,
            "contained":quest,
            "location":location,
        }

        context['storybookName'] = returnStorybookName(bookName)
        context['storybookStory'] = returnFantasyStorybookStory(name, quest, location)
        context['coverImage'] = returnStorybookImg(bookImg)[0]
        context['image2'] = returnStorybookImg(bookImg)[1]

        return render(request, 'html/base/story.html', context)

    return render(request, 'html/base/home.html', context)



def sportsPage(request):

    prompt1 = "Enter a name!"
    prompt2 = "Enter your favorite sport!"
    prompt3 = "Enter a location!"

    NameDictionary = {"Your Name":"IMG1", "Grandparent":"IMG2", "Teacher":"IMG3", "Pop Star":"IMG4", "Disney Character":"IMG5"}
    SportDictionary = {"Rugby":"IMG", "Basketball":"IMG2","Soccer":"IMG3", "Baseball":"IMG4", "Hockey":"IMG5"}
    LocationDictionary = {"Summer Camp":"IMG1", "High School":"IMG2", "Your City":"IMG3", "Stadium":"IMG4", "The Beach":"IMG5"}

    NameKeys = sorted(NameDictionary.keys())
    SportKeys = sorted(SportDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    RandomKey1 = []
    RandomKey2 = []
    RandomKey3 = []

    counter = 0
    for counter in range(2):
        index = randint(0,4)
        RandomNameKey = NameKeys[index]
        RandomSportKey = SportKeys[index]
        RandomLocationKey = LocationKeys[index]
        RandomKey1.append(RandomNameKey)
        RandomKey2.append(RandomSportKey)
        RandomKey3.append(RandomLocationKey)

    re_index = randint(0,1)
    context = {
            "prompt1":prompt1,
            "prompt2":prompt2,
            "prompt3":prompt3,
            "name":RandomKey1[re_index],
            "contained":RandomKey2[re_index],
            "location":RandomKey3[re_index],
        } 

    if request.method == 'POST':
        
        #bookImg = "someone called " + request.POST['bestfriendsname'] + " with " + request.POST['superpower'] + " powers in " + request.POST['location']
        #bookName = bookImg
        
        name = request.POST['bestfriendsname']
        sport = request.POST['superpower']
        location = request.POST['location']

        context = {
            "name":name,
            "contained":sport,
            "location":location,
        }

        #context['storybookName'] = returnStorybookName(bookName)
        context['storybookStory'] = returnSportsStorybookStory(name, sport, location)
        #context['coverImage'] = returnStorybookImg(bookImg)[0]
        #context['image2'] = returnStorybookImg(bookImg)[1]

        return render(request, 'html/base/story.html', context)

    return render(request, 'html/base/home.html', context)



def adventurePage(request):

    NameDictionary = {"adventure1":"IMG1", "adventure2":"IMG2", "adventure3":"IMG3"}
    QuestDictionary = {"superpower":"IMG", "fear":"IMG2","loved":"IMG3"}
    LocationDictionary = {"camp":"IMG1", "high school":"IMG2", "church":"IMG3"}

    NameKeys = sorted(NameDictionary.keys())
    QuestKeys = sorted(QuestDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    RandomKey1 = []
    RandomKey2 = []
    RandomKey3 = []

    counter = 0
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

        return render(request, 'html/base/story.html', context)

    return render(request, 'html/base/home.html', context)



def spookyPage(request):

    NameDictionary = {"spooky1":"IMG1", "spooky2":"IMG2", "spooky3":"IMG3"}
    QuestDictionary = {"superpower":"IMG", "fear":"IMG2","loved":"IMG3"}
    LocationDictionary = {"camp":"IMG1", "high school":"IMG2", "church":"IMG3"}

    NameKeys = sorted(NameDictionary.keys())
    QuestKeys = sorted(QuestDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    RandomKey1 = []
    RandomKey2 = []
    RandomKey3 = []

    counter = 0
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

        return render(request, 'html/base/story.html', context)

    return render(request, 'html/base/home.html', context)



def storyPage(request):

    fantasyFont = "'MedievalSharp', cursive;"
    sportsFont = "'Bungee', cursive;"
    adventureFont = "'Bangers', cursive;"
    spookyFont = "'Creepster', cursive;"

    context = {
        "fantasyFont":fantasyFont,
        "sportsFont":sportsFont,
        "adventureFont":adventureFont,
        "spookyFont":spookyFont,
    } 
    return render(request, 'html/base/story.html', context)
