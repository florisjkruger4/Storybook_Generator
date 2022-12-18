# secret key: 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

import os
import openai
from django.conf import settings
from random import randint

openai.api_key =  settings.OPENAI_API_KEY
openai.Model.list()

def returnStorybookName(bookName):
    response = openai.Completion.create(
        model="text-davinci-001",
        prompt="Write a name for a storybook about \n {}".format(bookName),
        temperature=0.55,
        max_tokens=10,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text'].replace('\n', '')
            return answer
        else:
            return ''
    else:
        return ''

# Fantasy Storybook Generator Options
def returnFantasyStorybookStory(name, quest, location):

    fantasyPrompts1value = randint(0, 7)
    fantasyPrompts1 = ["funny", "heroic", "courageous", "daunting", "impactful", "happy", "magical", "medieval"]
    fantasyPrompts2value = randint(0, 1)
    fantasyPrompts2 = ["person", "cow", "dog", "rhino"]

    fantasyPromptsCompleted = []
    fantasyPromptsCompleted.append("Write a " + fantasyPrompts1[fantasyPrompts1value] + " fantasy story about a " + fantasyPrompts2[fantasyPrompts2value] + " named {}".format(name) + " who is on a quest {}".format(quest) + " that takes place in or on {}".format(location) + " in the form of a bedtime storybook for a child.")

    print(fantasyPromptsCompleted[0])

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=fantasyPromptsCompleted[0],
        temperature=0.25,
        max_tokens=500,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text'].replace('\n', '')
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



