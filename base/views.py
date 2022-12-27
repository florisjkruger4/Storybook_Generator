import os
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

    audioPath = "/Users/floriskruger4/Desktop/Storybook_Generator/Storybook_Generator/static/audio/StoryAudio.mp3"
    audioDirPath = "/Users/floriskruger4/Desktop/Storybook_Generator/Storybook_Generator/static/audio"
    audioDir = os.listdir(audioDirPath)

    if (len(audioDir) != 0):
        os.remove(audioPath)

    prompt1 = "Enter a name!"
    prompt2 = "Enter your story's quest!"
    prompt3 = "Enter a location!"

    NameDictionary = {"Best Friend":"IMG1", "Parent":"IMG2", "Sibling":"IMG3", "Celebrity":"IMG4", "Movie Character":"IMG5",}
    QuestDictionary = {"Slaying a dragon":"IMG", "Saving the planet":"IMG2", "Stopping a zombie apocalypse":"IMG3", "Rescuing a princess":"IMG4", "Getting superpowers":"IMG5"}
    LocationDictionary = {"Alien Planet":"IMG1", "Middle Earth":"IMG2", "Atlantis":"IMG3", "Gotham City":"IMG4", "Hogwarts":"IMG5"}

    NameKeys = sorted(NameDictionary.keys())
    QuestKeys = sorted(QuestDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    index1 = randint(0,4)
    index2 = randint(0,4)
    index3 = randint(0,4)

    RandomKey1 = NameKeys[index1]
    RandomKey2 = QuestKeys[index2]
    RandomKey3 = LocationKeys[index3]

    context = {
            "prompt1":prompt1,
            "prompt2":prompt2,
            "prompt3":prompt3,
            "name":RandomKey1,
            "contained":RandomKey2,
            "location":RandomKey3,
        } 


    if request.method == 'POST':
        
        bookName = "someone called " + request.POST['name'] + " on a quest " + request.POST['contained'] + " based in " + request.POST['location']
        bookImg = bookName
        
        name = request.POST['name']
        quest = request.POST['contained']
        location = request.POST['location']

        context = {
            "name":name,
            "contained":quest,
            "location":location,
        }

        context['storybookName'] = returnStorybookName(bookName)
        context['storybookStory'] = returnFantasyStorybookStory(name, quest, location)
        context['coverImage'] = returnStorybookImg(bookImg)

        return render(request, 'html/base/story.html', context)

    return render(request, 'html/base/home.html', context)



def sportsPage(request):

    audioPath = "/Users/floriskruger4/Desktop/Storybook_Generator/Storybook_Generator/static/audio/StoryAudio.mp3"
    audioDirPath = "/Users/floriskruger4/Desktop/Storybook_Generator/Storybook_Generator/static/audio"
    audioDir = os.listdir(audioDirPath)

    if (len(audioDir) != 0):
        os.remove(audioPath)

    prompt1 = "Enter a name!"
    prompt2 = "Enter a sport!"
    prompt3 = "Enter a location!"

    NameDictionary = {"Your Name":"IMG1", "Grandparent":"IMG2", "Teacher":"IMG3", "Pop Star":"IMG4", "Disney Character":"IMG5"}
    SportDictionary = {"Rugby":"IMG", "Basketball":"IMG2","Soccer":"IMG3", "Baseball":"IMG4", "Hockey":"IMG5"}
    LocationDictionary = {"Summer Camp":"IMG1", "High School":"IMG2", "Your City":"IMG3", "Sport Stadium":"IMG4", "The Beach":"IMG5"}

    NameKeys = sorted(NameDictionary.keys())
    SportKeys = sorted(SportDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    index1 = randint(0,4)
    index2 = randint(0,4)
    index3 = randint(0,4)

    RandomKey1 = NameKeys[index1]
    RandomKey2 = SportKeys[index2]
    RandomKey3 = LocationKeys[index3]

    context = {
            "prompt1":prompt1,
            "prompt2":prompt2,
            "prompt3":prompt3,
            "name":RandomKey1,
            "contained":RandomKey2,
            "location":RandomKey3,
        } 

    if request.method == 'POST':
        
        bookName = "someone called " + request.POST['name'] + " who plays and loves the sport " + request.POST['contained'] + " based in " + request.POST['location']
        bookImg = bookName
        
        name = request.POST['name']
        sport = request.POST['contained']
        location = request.POST['location']

        context = {
            "name":name,
            "contained":sport,
            "location":location,
        }

        context['storybookName'] = returnStorybookName(bookName)
        context['storybookStory'] = returnSportsStorybookStory(name, sport, location)
        context['coverImage'] = returnStorybookImg(bookImg)

        return render(request, 'html/base/story.html', context)

    return render(request, 'html/base/home.html', context)



def adventurePage(request):

    audioPath = "/Users/floriskruger4/Desktop/Storybook_Generator/Storybook_Generator/static/audio/StoryAudio.mp3"
    audioDirPath = "/Users/floriskruger4/Desktop/Storybook_Generator/Storybook_Generator/static/audio"
    audioDir = os.listdir(audioDirPath)

    if (len(audioDir) != 0):
        os.remove(audioPath)

    prompt1 = "Enter a name!"
    prompt2 = "Enter your story's adventure!"
    prompt3 = "Enter a location!"

    NameDictionary = {"Your Crush":"IMG1", "Comedian":"IMG2", "Philosopher":"IMG3", "Artist":"IMG4", "Cousin":"IMG5"}
    AdventureDictionary = {"Looking for treasure":"IMG", "Exploring outer space":"IMG2", "Helping an old lady cross the road":"IMG3", "Riding a hot air balloon":"IMG4", "Going skydiving":"IMG5"}
    LocationDictionary = {"USA":"IMG1", "The Woods":"IMG2", "Theme Park":"IMG3", "Arcade":"IMG4", "Vacation Resort":"IMG5"}

    NameKeys = sorted(NameDictionary.keys())
    AdventureKeys = sorted(AdventureDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    index1 = randint(0,2)
    index2 = randint(0,2)
    index3 = randint(0,2)

    RandomKey1 = NameKeys[index1]
    RandomKey2 = AdventureKeys[index2]
    RandomKey3 = LocationKeys[index3]

    context = {
            "prompt1":prompt1,
            "prompt2":prompt2,
            "prompt3":prompt3,
            "name":RandomKey1,
            "contained":RandomKey2,
            "location":RandomKey3,
        } 

    if request.method == 'POST':
        
        bookName = "someone called " + request.POST['name'] + " on an adventure " + request.POST['contained'] + " based in " + request.POST['location']
        bookImg = bookName
        
        name = request.POST['name']
        adventure = request.POST['contained']
        location = request.POST['location']

        context = {
            "name":name,
            "contained":adventure,
            "location":location,
        }

        context['storybookName'] = returnStorybookName(bookName)
        context['storybookStory'] = returnAdventureStorybookStory(name, adventure, location)
        context['coverImage'] = returnStorybookImg(bookImg)

        return render(request, 'html/base/story.html', context)

    return render(request, 'html/base/home.html', context)



def spookyPage(request):

    audioPath = "/Users/floriskruger4/Desktop/Storybook_Generator/Storybook_Generator/static/audio/StoryAudio.mp3"
    audioDirPath = "/Users/floriskruger4/Desktop/Storybook_Generator/Storybook_Generator/static/audio"
    audioDir = os.listdir(audioDirPath)

    if (len(audioDir) != 0):
        os.remove(audioPath)

    prompt1 = "Enter a name!"
    prompt2 = "Enter something scary!"
    prompt3 = "Enter a location!"

    NameDictionary = {"Frankenstein":"IMG1", "Scooby Doo":"IMG2", "Your Dog":"IMG3", "Spouse":"IMG4", "Famous Athlete":"IMG5"}
    SpookyDictionary = {"Exploring a haunted house":"IMG", "Ghost hunting in a spooky mansion":"IMG2", "Escaping a pack of werewolf's on a full moon night":"IMG3", "Stopping vampires from sucking your blood":"IMG4", "Getting no candy on Halloween":"IMG5"}
    LocationDictionary = {"Neighborhood":"IMG1", "Haunted House":"IMG2", "Spooky Mansion":"IMG3", "Scary Dungeon":"IMG4", "Eerie Old Castle":"IMG5"}

    NameKeys = sorted(NameDictionary.keys())
    SpookyKeys = sorted(SpookyDictionary.keys())
    LocationKeys = sorted(LocationDictionary.keys())

    index1 = randint(0,2)
    index2 = randint(0,2)
    index3 = randint(0,2)

    RandomKey1 = NameKeys[index1]
    RandomKey2 = SpookyKeys[index2]
    RandomKey3 = LocationKeys[index3]

    context = {
            "prompt1":prompt1,
            "prompt2":prompt2,
            "prompt3":prompt3,
            "name":RandomKey1,
            "contained":RandomKey2,
            "location":RandomKey3,
        } 

    if request.method == 'POST':
        
        bookName = "someone called " + request.POST['name'] + " in a spooky situation " + request.POST['contained'] + " based in " + request.POST['location']
        bookImg = bookName
        
        name = request.POST['name']
        spooky = request.POST['contained']
        location = request.POST['location']

        context = {
            "name":name,
            "contained":spooky,
            "location":location,
        }

        context['storybookName'] = returnStorybookName(bookName)
        context['storybookStory'] = returnSpookyStorybookStory(name, spooky, location)
        context['coverImage'] = returnStorybookImg(bookImg)

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


def test(request):
    context = {}
    return render(request, 'html/base/test.html', context)
