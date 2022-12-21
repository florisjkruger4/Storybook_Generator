import os
import openai
from django.conf import settings
from random import randint

openai.api_key =  settings.OPENAI_API_KEY
openai.Model.list()

def returnStorybookName(bookName):
    response = openai.Completion.create(
        model="text-davinci-001",
        prompt="Give a name for a childrens storybook about \n {}".format(bookName),
        temperature=0.65,
        max_tokens=15,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text'].replace('\n', ' ')
            return answer
        else:
            return ''
    else:
        return ''

# Fantasy Storybook Generator Options
def returnFantasyStorybookStory(name, quest, location):

    randomPromptSelect = randint(0, 2)
    fantasyPromptsCompleted = []

    firstfantasyPrompts1value = randint(0, 7)
    firstfantasyPrompts1 = ["funny", "heroic", "courageous", "daunting", "impactful", "happy", "magical", "medieval", "space", "pirate"]
    firstfantasyPrompts2value = randint(0, 1)
    firstfantasyPrompts2 = ["person", "hero"]
    fantasyPromptsCompleted.append("Write a " + firstfantasyPrompts1[firstfantasyPrompts1value] + " fantasy story about a " + firstfantasyPrompts2[firstfantasyPrompts2value] + " protagonist named {}".format(name) + " who is on a quest {}".format(quest) + " that takes place in or on {}".format(location) + " in the form of a bedtime storybook for a child.")

    secondfantasyPrompts1value = randint(0, 1)
    secondfantasyPrompts1 = ["past", "future"]
    secondfantasyPrompts2value = randint(0, 3)
    secondfantasyPrompts2 = ["sunny", "cold", "stormy", "cloudy"]
    secondfantasyPrompts3value = randint(0, 1)
    secondfantasyPrompts3 = ["person", "hero"]
    secondfantasyPrompts4value = randint(0, 5)
    secondfantasyPrompts4 = ["goblins", "trolls", "witches", "aliens", "robots", "pirates"]
    fantasyPromptsCompleted.append("Write a bedtime story for a child based in the " + secondfantasyPrompts1[secondfantasyPrompts1value] + " that takes place in or on {}".format(location) + " on a " + secondfantasyPrompts2[secondfantasyPrompts2value] + " day about a " + secondfantasyPrompts3[secondfantasyPrompts3value] + " protagonist named {}".format(name) + " who is on a mission {}".format(quest) + " with a trusty companion and encounters bad " + secondfantasyPrompts4[secondfantasyPrompts4value] + " foes along the way.")

    thirdfantasyPrompts1value = randint(0, 4)
    thirdfantasyPrompts1 = ["medieval", "outer space", "pirate", "special agent", "magical"]
    thirdfantasyPrompts2value = randint(0, 1)
    thirdfantasyPrompts2 = ["person", "hero"]
    thirdfantasyPrompts3value = randint(0, 2)
    thirdfantasyPrompts3 = ["loyal", "brave", "funny"]
    fantasyPromptsCompleted.append("Write a " + thirdfantasyPrompts1[thirdfantasyPrompts1value] + " fantasy bedtime story about a " + thirdfantasyPrompts2[thirdfantasyPrompts2value] + " protagonist named {}".format(name) + " who makes a group of " + thirdfantasyPrompts3[thirdfantasyPrompts3value] + " friends to go {}".format(quest) + " together and learns a valuable lesson and takes place in or on {}.".format(location))

    print(fantasyPromptsCompleted[randomPromptSelect])

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=fantasyPromptsCompleted[randomPromptSelect],
        temperature=0.25,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
    )


    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text'].replace('\n', ' ')
            return answer
        else:
            return ''
    else:
        return ''

def returnStorybookImg(bookImg):
    response = openai.Image.create(
        prompt = "Generate a kids storybook image of \n {}".format(bookImg),
        n = 2,
        size = "256x256"
    )

    imageOne_url = response['data'][0]['url']
    imageTwo_url = response['data'][1]['url']

    return imageOne_url, imageTwo_url


# Sports Storybook Generator Options
def returnSportsStorybookStory(name, sport, location):

    randomPromptSelect = randint(0, 2)
    sportsPromptsCompleted = []

    firstsportsPrompts1value = randint(0, 7)
    firstsportsPrompts1 = ["funny", "courageous", "daunting", "impactful", "happy", "heartwarming", "silly", "underdog"]
    firstsportsPrompts2value = randint(0, 1)
    firstsportsPrompts2 = ["outgoing", "shy"]
    sportsPromptsCompleted.append("Write a " + firstsportsPrompts1[firstsportsPrompts1value] + " sports story about a person named {}".format(name) + " who is an " + firstsportsPrompts2[firstsportsPrompts2value] + " player on a {}".format(sport) + " team who works together with teammates to win a tournament based in or on {}".format(location) + " in the form of a bedtime storybook for a child.")

    secondsportsPrompts1value = randint(0, 7)
    secondsportsPrompts1 = ["funny", "courageous", "daunting", "impactful", "happy", "heartwarming", "silly", "underdog"]
    secondsportsPrompts2value = randint(0, 3)
    secondsportsPrompts2 = ["tall", "short", "strong", "fast"]
    secondsportsPrompts3value = randint(0, 1)
    secondsportsPrompts3 = ["outgoing", "shy"]
    secondsportsPrompts4value = randint(0, 5)
    secondsportsPrompts4 = ["stormy", "rainy", "cold", "hot", "windy", "foggy"]
    sportsPromptsCompleted.append("Write a " + secondsportsPrompts1[secondsportsPrompts1value] + " sports bedtime story for a child about a " + secondsportsPrompts2[secondsportsPrompts2value] + " and " + secondsportsPrompts3[secondsportsPrompts3value] + " and determined person named {}".format(name) + " who forms a group of friends who decide to make flyers to start a new {}".format(sport) + " team to go on and play against a rival team on a " + secondsportsPrompts4[secondsportsPrompts4value] + " day based in or on {}".format(location))

    thirdsportsPrompts1value = randint(0, 7)
    thirdsportsPrompts1 = ["funny", "courageous", "daunting", "impactful", "happy", "heartwarming", "silly", "underdog"]
    thirdsportsPrompts2value = randint(0, 1)
    thirdsportsPrompts2 = ["outgoing", "shy"]
    sportsPromptsCompleted.append("Write a " + thirdsportsPrompts1[thirdsportsPrompts1value] + " sports bedtime story for a child based in or on {}".format(location) + " about a " + thirdsportsPrompts2[thirdsportsPrompts2value] + " person named {}".format(name) + " who works hard to get a spot on the team for a {}".format(sport) + " league and makes friends with a bully on the team and work together to win.")

    print(sportsPromptsCompleted[randomPromptSelect])

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=sportsPromptsCompleted[randomPromptSelect],
        temperature=0.25,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text'].replace('\n', ' ')
            return answer
        else:
            return ''
    else:
        return ''

def returnStorybookImg(bookImg):
    response = openai.Image.create(
        prompt = "Generate a kids storybook image of \n {}".format(bookImg),
        n = 2,
        size = "256x256"
    )

    imageOne_url = response['data'][0]['url']
    imageTwo_url = response['data'][1]['url']

    return imageOne_url, imageTwo_url



