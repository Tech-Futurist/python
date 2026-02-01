#!/usr/bin/python3

import os, random
from threading import Thread
from time import sleep
from pygame import mixer
from termcolor import colored
from playsound import playsound

from config import *

# Importing module specified in the config file
art = __import__(f'arts.{artFile}', globals(), locals(), ['*'])


def replaceMultiple(mainString, toBeReplace, newString):

    # Iterate over the list to be replaced
    for elem in toBeReplace:
        # Check if the element is in the main string
        if elem in mainString:
            # Replace the string
            mainString = mainString.replace(elem, newString)

    return mainString


# def pprint(art, time):
#     color_used = [random.choice(color)]
#     colorAttribute = []
#     for i in range(len(art)):
#         if art[i] in colorCodes:
#             # Color attr set to blink if 9
#             if art[i] == '⑨':
#                 colorAttribute = [colorCodes[art[i]]]
#             # color attr none if 10
#             elif art[i] == '⑩' \
#                            '' \
#                            '':
#                 colorAttribute = []
#             # Random color if R
#             elif art[i] == '®':
#                 color_used = color
#
#             else:
#                 color_used = [colorCodes[art[i]]]
#
#         print(colored(replaceMultiple(art[i], colorCodes, ''), random.choice(color_used), attrs=colorAttribute), sep='',
#               end='', flush=True)
#         sleep(time)
def pprint(art, time):
    color_used = random.choice(color)
    colorAttribute = []
    for i in range(len(art)):
        if art[i] in colorCodes:
            if art[i] == '⑨':
                colorAttribute = ['blink']
            elif art[i] == '⑩':
                colorAttribute = []
            elif art[i] == '®':
                color_used = random.choice(color)
            else:
                color_used = colorCodes[art[i]]

        # Check if color_used is a valid color
        if color_used in colorCodes.values():
            print(colored(replaceMultiple(art[i], colorCodes, ''), color_used, attrs=colorAttribute), sep='', end='', flush=True)
        else:
            # Default to white if an invalid color is specified
            print(colored(replaceMultiple(art[i], colorCodes, ''), 'white', attrs=colorAttribute), sep='', end='', flush=True)
        sleep(time)


# def pAudio():
#     if playAudio:
#         playsound(audio)
def pAudio():
    if playAudio:
        mixer.init()
        mixer.music.load(audio)
        mixer.music.play()
        while mixer.music.get_busy():
            sleep(0.1)


def pcode():
    # Print the code before wishing
    if codePrint:
        for i in range(len(art.code)):
            print(colored(art.code[i], codeColor), sep='', end='', flush=True)
            sleep(codingSpeed)
        input('\n\n' + colored('python3', 'blue') + colored(' PyBirthdayWish.py', 'yellow'))
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        input(colored('press {Enter} and turn up volume to max', 'blue'))
        os.system('cls' if os.name == 'nt' else 'clear')
    


# Clearing terminal
os.system('cls' if os.name == 'nt' else 'clear')
pcode()
Thread(target=pAudio).start()
Thread(target=pprint, args=(art.mainArt, speed)).start()
