# secret key: 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

import os
import openai
from django.conf import settings

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


def returnStorybookStory(bookContent):
    response = openai.Completion.create(
        model="text-davinci-001",
        prompt="Write a kids storybook (minimum 100 words) about \n {}".format(bookContent),
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
        prompt = "Generate a storybook image of \n {}".format(bookImg),
        n = 2,
        size = "256x256"
    )

    imageOne_url = response['data'][0]['url']
    imageTwo_url = response['data'][1]['url']
    #print(imageTwo_url)

    return imageOne_url, imageTwo_url



