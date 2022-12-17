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
def returnStorybookStory(name, power, location):

    value = randint(0, 2)
    fantasyPrompts = []
    fantasyPrompts.append("Write a kids storybook a toad that goes on an adventure to fight a frog")
    fantasyPrompts.append("Write a kids storybook a pirate that needs to fight off an army of crabs")
    fantasyPrompts.append("Write a kids storybook about someone named \n {}".format(name) + " with {}".format(power) + " superpowers that that takes place in {}".format(location))

    response = openai.Completion.create(
        model="text-davinci-001",
        #prompt=fantasyPrompts[value], 
        prompt="Write a kids storybook about someone named \n {}".format(name) + " with {}".format(power) + " superpowers that that takes place in {}".format(location),
        temperature=0.25,
        max_tokens=300,
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
    #print(imageTwo_url)

    return imageOne_url, imageTwo_url



