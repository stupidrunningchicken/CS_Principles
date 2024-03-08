# This file was created by: Theodore Do

#import libraries
import pygame as pg
from mainsettings import * 
from sprites import *
import sys
from os import path 
from random import randint

#create a class game
class Game: 
    def __init__(self):
        pg.init()
        