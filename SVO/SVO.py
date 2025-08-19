#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on August 18, 2025, at 22:45
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'SVO'  # from the Builder filename that created this script
expInfo = {'pOrder': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['pOrder'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='SVO.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920,1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome_1"
welcome_1Clock = core.Clock()
IntroText_1 = visual.TextStim(win=win, name='IntroText_1',
    text='INSTRUCTIONS\n\nIn this task you have been randomly paired with another person, whom we will refer to as the other. This other person is someone you do not know and will remain mutually anonymous. All of your choices are completely confidential. You will be making a series of decisions about allocating resources between you and this other person. \n\nPress SPACE to continue',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
IntroKey_1 = keyboard.Keyboard()

# Initialize components for Routine "welcome_2"
welcome_2Clock = core.Clock()
IntroText_2 = visual.TextStim(win=win, name='IntroText_2',
    text='Your decisions will yield money for both yourself and the other person. In the example below, a person has chosen to distribute money so that he/she receives 50 dollars, while the anonymous other person receives 40 dollars.\n\nThere are no right or wrong answers, this is all about personal preferences. After you have made your decision, the resulting distribution will apear on the spaces on the right. As you can see, your choices will influence both the amount of money you receive as well as the amount of money the other receives. ',
    font='Open Sans',
    pos=(0, .27), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_1 = visual.Slider(win=win, name='slider_1',
    startValue=5, size=(1.0, 0.15), pos=(0, -.16), units=None,
    labels=None, ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9), granularity=0.5,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=True)
IntroText_3 = visual.TextStim(win=win, name='IntroText_3',
    text='Press SPACE to begin',
    font='Open Sans',
    pos=(0, -.43), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
YouReceiveText_1 = visual.TextBox2(
     win, text=' 30', font='Open Sans',
     pos=(-.5, -.03),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveText_1',
     autoLog=False,
)
YouReceiveText_2 = visual.TextBox2(
     win, text=' 35', font='Open Sans',
     pos=(-.375, -.03),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveText_2',
     autoLog=False,
)
YouReceiveText_3 = visual.TextBox2(
     win, text=' 40', font='Open Sans',
     pos=(-.125, -.03),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveText_3',
     autoLog=False,
)
YouReceiveText_4 = visual.TextBox2(
     win, text=' 45', font='Open Sans',
     pos=(-.25, -.03),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveText_4',
     autoLog=False,
)
YouReceiveText_5 = visual.TextBox2(
     win, text=' 50', font='Open Sans',
     pos=(0, -.03),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveText_5',
     autoLog=False,
)
YouReceiveText_6 = visual.TextBox2(
     win, text=' 55', font='Open Sans',
     pos=(.25, -.03),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveText_6',
     autoLog=False,
)
YouReceiveText_7 = visual.TextBox2(
     win, text=' 60', font='Open Sans',
     pos=(.125, -.03),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveText_7',
     autoLog=False,
)
YouReceiveText_8 = visual.TextBox2(
     win, text=' 65', font='Open Sans',
     pos=(.375, -.03),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveText_8',
     autoLog=False,
)
YouReceiveText_9 = visual.TextBox2(
     win, text=' 70', font='Open Sans',
     pos=(.5, -.03),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveText_9',
     autoLog=False,
)
OtherReceiveText_1 = visual.TextBox2(
     win, text=' 80', font='Open Sans',
     pos=(-.5, -.29),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveText_1',
     autoLog=False,
)
OtherReceiveText_2 = visual.TextBox2(
     win, text=' 70', font='Open Sans',
     pos=(-.375, -.29),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveText_2',
     autoLog=False,
)
OtherReceiveText_3 = visual.TextBox2(
     win, text=' 60', font='Open Sans',
     pos=(-.125, -.29),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveText_3',
     autoLog=False,
)
OtherReceiveText_4 = visual.TextBox2(
     win, text=' 50', font='Open Sans',
     pos=(-.25, -.29),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveText_4',
     autoLog=False,
)
OtherReceiveText_5 = visual.TextBox2(
     win, text=' 40', font='Open Sans',
     pos=(0, -.29),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveText_5',
     autoLog=False,
)
OtherReceiveText_6 = visual.TextBox2(
     win, text=' 30', font='Open Sans',
     pos=(.25, -.29),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveText_6',
     autoLog=False,
)
OtherReceiveText_7 = visual.TextBox2(
     win, text=' 20', font='Open Sans',
     pos=(.125, -.29),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveText_7',
     autoLog=False,
)
OtherReceiveText_8 = visual.TextBox2(
     win, text=' 10', font='Open Sans',
     pos=(.375, -.29),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveText_8',
     autoLog=False,
)
OtherReceiveText_9 = visual.TextBox2(
     win, text='  0', font='Open Sans',
     pos=(.5, -.29),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveText_9',
     autoLog=False,
)
YouReceiveText = visual.TextStim(win=win, name='YouReceiveText',
    text='You receive',
    font='Open Sans',
    pos=(-.72, -.03), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
OtherReceiveText = visual.TextStim(win=win, name='OtherReceiveText',
    text='Other receives',
    font='Open Sans',
    pos=(-.72, -.29), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-23.0);
YouDistribution = visual.TextStim(win=win, name='YouDistribution',
    text='You',
    font='Open Sans',
    pos=(.65, -.03), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-24.0);
OtherDistribution = visual.TextStim(win=win, name='OtherDistribution',
    text='Other',
    font='Open Sans',
    pos=(.65, -.29), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-25.0);
TaskOutline = visual.Rect(
    win=win, name='TaskOutline',
    width=(1.45, 0.4)[0], height=(1.45, 0.4)[1],
    ori=0.0, pos=(-.15, -.17),
    lineWidth=4.0,     colorSpace='rgb',  lineColor='white', fillColor='grey',
    opacity=0.2, depth=-26.0, interpolate=True)
You_Amount_Text = visual.TextStim(win=win, name='You_Amount_Text',
    text='50',
    font='Open Sans',
    pos=(.75, -.03), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-27.0);
Other_Amount_Text = visual.TextStim(win=win, name='Other_Amount_Text',
    text='40',
    font='Open Sans',
    pos=(.75, -.29), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-28.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
slider_2 = visual.Slider(win=win, name='slider_2',
    startValue=5, size=(1.0, 0.15), pos=(0, 0), units=None,
    labels=None, ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9), granularity=0.5,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=0, readOnly=False)
raw_self = []
raw_other = []
YouReceiveTextTrial_1 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(-.5, .13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveTextTrial_1',
     autoLog=False,
)
YouReceiveTextTrial_2 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(-.375, .13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveTextTrial_2',
     autoLog=False,
)
YouReceiveTextTrial_3 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(-.25, .13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveTextTrial_3',
     autoLog=False,
)
YouReceiveTextTrial_4 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(-.125, .13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveTextTrial_4',
     autoLog=False,
)
YouReceiveTextTrial_5 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, .13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveTextTrial_5',
     autoLog=False,
)
YouReceiveTextTrial_6 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(.125, .13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveTextTrial_6',
     autoLog=False,
)
YouReceiveTextTrial_7 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(.25, .13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveTextTrial_7',
     autoLog=False,
)
YouReceiveTextTrial_8 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(.375, .13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveTextTrial_8',
     autoLog=False,
)
YouReceiveTextTrial_9 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(.5, .13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='YouReceiveTextTrial_9',
     autoLog=False,
)
OtherReceiveTextTrial_1 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(-.5, -.13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveTextTrial_1',
     autoLog=False,
)
OtherReceiveTextTrial_2 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(-.375, -.13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveTextTrial_2',
     autoLog=False,
)
OtherReceiveTextTrial_3 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(-.25, -.13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveTextTrial_3',
     autoLog=False,
)
OtherReceiveTextTrial_4 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(-.125, -.13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveTextTrial_4',
     autoLog=False,
)
OtherReceiveTextTrial_5 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, -.13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveTextTrial_5',
     autoLog=False,
)
OtherReceiveTextTrial_6 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(.125, -.13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveTextTrial_6',
     autoLog=False,
)
OtherReceiveTextTrial_7 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(.25, -.13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveTextTrial_7',
     autoLog=False,
)
OtherReceiveTextTrial_8 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(.375, -.13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveTextTrial_8',
     autoLog=False,
)
OtherReceiveTextTrial_9 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(.5, -.13),     letterHeight=0.05,
     size=(.1,.07), borderWidth=4.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.004,
     anchor='center',
     fillColor=None, borderColor='white',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='OtherReceiveTextTrial_9',
     autoLog=False,
)
TrialOutline = visual.Rect(
    win=win, name='TrialOutline',
    width=(1.45, 0.4)[0], height=(1.45, 0.4)[1],
    ori=0.0, pos=(-.15, -.01),
    lineWidth=4.0,     colorSpace='rgb',  lineColor='white', fillColor='grey',
    opacity=0.2, depth=-20.0, interpolate=True)
YouReceiveTextTrial = visual.TextStim(win=win, name='YouReceiveTextTrial',
    text='You receive',
    font='Open Sans',
    pos=(-.72, .13), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-21.0);
OtherReceiveTextTrial = visual.TextStim(win=win, name='OtherReceiveTextTrial',
    text='Other receives',
    font='Open Sans',
    pos=(-.72, -.13), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
YouAmountTextTrial = visual.TextStim(win=win, name='YouAmountTextTrial',
    text='50',
    font='Open Sans',
    pos=(.78, .13), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-23.0);
OtherAmountTextTrial = visual.TextStim(win=win, name='OtherAmountTextTrial',
    text='40',
    font='Open Sans',
    pos=(.78, -.13), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-24.0);
trial_next_space = keyboard.Keyboard()
YouDistributionTrial = visual.TextStim(win=win, name='YouDistributionTrial',
    text='You',
    font='Open Sans',
    pos=(.65, .13), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-26.0);
OtherDistributionTrial = visual.TextStim(win=win, name='OtherDistributionTrial',
    text='Other',
    font='Open Sans',
    pos=(.65, -.13), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-27.0);
space_trial_text = visual.TextStim(win=win, name='space_trial_text',
    text='Please select a distribution',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-28.0);
text = visual.TextStim(win=win, name='text',
    text='Press SPACE to continue',
    font='Open Sans',
    pos=(0, -.41), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-29.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='Thank you for your participantion. \n\n\nPress SPACE to end',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
space_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome_1"-------
continueRoutine = True
# update component parameters for each repeat
IntroKey_1.keys = []
IntroKey_1.rt = []
_IntroKey_1_allKeys = []
# keep track of which components have finished
welcome_1Components = [IntroText_1, IntroKey_1]
for thisComponent in welcome_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_1"-------
while continueRoutine:
    # get current time
    t = welcome_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IntroText_1* updates
    if IntroText_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IntroText_1.frameNStart = frameN  # exact frame index
        IntroText_1.tStart = t  # local t and not account for scr refresh
        IntroText_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroText_1, 'tStartRefresh')  # time at next scr refresh
        IntroText_1.setAutoDraw(True)
    
    # *IntroKey_1* updates
    if IntroKey_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IntroKey_1.frameNStart = frameN  # exact frame index
        IntroKey_1.tStart = t  # local t and not account for scr refresh
        IntroKey_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroKey_1, 'tStartRefresh')  # time at next scr refresh
        IntroKey_1.status = STARTED
        # keyboard checking is just starting
        IntroKey_1.clock.reset()  # now t=0
    if IntroKey_1.status == STARTED:
        theseKeys = IntroKey_1.getKeys(keyList=['space'], waitRelease=False)
        _IntroKey_1_allKeys.extend(theseKeys)
        if len(_IntroKey_1_allKeys):
            IntroKey_1.keys = _IntroKey_1_allKeys[-1].name  # just the last key pressed
            IntroKey_1.rt = _IntroKey_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_1"-------
for thisComponent in welcome_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if IntroKey_1.keys in ['', [], None]:  # No response was made
    IntroKey_1.keys = None
thisExp.addData('IntroKey_1.keys',IntroKey_1.keys)
if IntroKey_1.keys != None:  # we had a response
    thisExp.addData('IntroKey_1.rt', IntroKey_1.rt)
thisExp.nextEntry()
# the Routine "welcome_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome_2"-------
continueRoutine = True
# update component parameters for each repeat
slider_1.reset()
from psychopy.visual.slider import Slider
from psychopy.visual.line import Line
 
# Adjust the marker size (smaller = less than default 0.05)
slider_1.marker.size = 0.04

tick_xpos = [-.5, -.375, -.25, -.125, 0, .125, .25, .375, .5]
midpoints = []
slider_ypos = slider_1.pos[1]
for i in range(len(tick_xpos)-1):
    midpoint = (tick_xpos[i] + tick_xpos[i+1]) / 2
    midpoints.append(midpoint)

line_pos = []
for x in midpoints:
    line = Line(
        win,
        start = (x , slider_ypos -.04),
        end = (x , slider_ypos +.04),
        lineColor = 'gray',  
        lineWidth = 6,
        autoDraw = True
    )
    line_pos.append(line)
YouReceiveText_1.reset()
YouReceiveText_2.reset()
YouReceiveText_3.reset()
YouReceiveText_4.reset()
YouReceiveText_5.reset()
YouReceiveText_6.reset()
YouReceiveText_7.reset()
YouReceiveText_8.reset()
YouReceiveText_9.reset()
OtherReceiveText_1.reset()
OtherReceiveText_2.reset()
OtherReceiveText_3.reset()
OtherReceiveText_4.reset()
OtherReceiveText_5.reset()
OtherReceiveText_6.reset()
OtherReceiveText_7.reset()
OtherReceiveText_8.reset()
OtherReceiveText_9.reset()
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
welcome_2Components = [IntroText_2, slider_1, IntroText_3, YouReceiveText_1, YouReceiveText_2, YouReceiveText_3, YouReceiveText_4, YouReceiveText_5, YouReceiveText_6, YouReceiveText_7, YouReceiveText_8, YouReceiveText_9, OtherReceiveText_1, OtherReceiveText_2, OtherReceiveText_3, OtherReceiveText_4, OtherReceiveText_5, OtherReceiveText_6, OtherReceiveText_7, OtherReceiveText_8, OtherReceiveText_9, YouReceiveText, OtherReceiveText, YouDistribution, OtherDistribution, TaskOutline, You_Amount_Text, Other_Amount_Text, key_resp]
for thisComponent in welcome_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_2"-------
while continueRoutine:
    # get current time
    t = welcome_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IntroText_2* updates
    if IntroText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IntroText_2.frameNStart = frameN  # exact frame index
        IntroText_2.tStart = t  # local t and not account for scr refresh
        IntroText_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroText_2, 'tStartRefresh')  # time at next scr refresh
        IntroText_2.setAutoDraw(True)
    
    # *slider_1* updates
    if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        slider_1.frameNStart = frameN  # exact frame index
        slider_1.tStart = t  # local t and not account for scr refresh
        slider_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
        slider_1.setAutoDraw(True)
    
    # *IntroText_3* updates
    if IntroText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IntroText_3.frameNStart = frameN  # exact frame index
        IntroText_3.tStart = t  # local t and not account for scr refresh
        IntroText_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroText_3, 'tStartRefresh')  # time at next scr refresh
        IntroText_3.setAutoDraw(True)
    
    # *YouReceiveText_1* updates
    if YouReceiveText_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        YouReceiveText_1.frameNStart = frameN  # exact frame index
        YouReceiveText_1.tStart = t  # local t and not account for scr refresh
        YouReceiveText_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(YouReceiveText_1, 'tStartRefresh')  # time at next scr refresh
        YouReceiveText_1.setAutoDraw(True)
    
    # *YouReceiveText_2* updates
    if YouReceiveText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        YouReceiveText_2.frameNStart = frameN  # exact frame index
        YouReceiveText_2.tStart = t  # local t and not account for scr refresh
        YouReceiveText_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(YouReceiveText_2, 'tStartRefresh')  # time at next scr refresh
        YouReceiveText_2.setAutoDraw(True)
    
    # *YouReceiveText_3* updates
    if YouReceiveText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        YouReceiveText_3.frameNStart = frameN  # exact frame index
        YouReceiveText_3.tStart = t  # local t and not account for scr refresh
        YouReceiveText_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(YouReceiveText_3, 'tStartRefresh')  # time at next scr refresh
        YouReceiveText_3.setAutoDraw(True)
    
    # *YouReceiveText_4* updates
    if YouReceiveText_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        YouReceiveText_4.frameNStart = frameN  # exact frame index
        YouReceiveText_4.tStart = t  # local t and not account for scr refresh
        YouReceiveText_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(YouReceiveText_4, 'tStartRefresh')  # time at next scr refresh
        YouReceiveText_4.setAutoDraw(True)
    
    # *YouReceiveText_5* updates
    if YouReceiveText_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        YouReceiveText_5.frameNStart = frameN  # exact frame index
        YouReceiveText_5.tStart = t  # local t and not account for scr refresh
        YouReceiveText_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(YouReceiveText_5, 'tStartRefresh')  # time at next scr refresh
        YouReceiveText_5.setAutoDraw(True)
    
    # *YouReceiveText_6* updates
    if YouReceiveText_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        YouReceiveText_6.frameNStart = frameN  # exact frame index
        YouReceiveText_6.tStart = t  # local t and not account for scr refresh
        YouReceiveText_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(YouReceiveText_6, 'tStartRefresh')  # time at next scr refresh
        YouReceiveText_6.setAutoDraw(True)
    
    # *YouReceiveText_7* updates
    if YouReceiveText_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        YouReceiveText_7.frameNStart = frameN  # exact frame index
        YouReceiveText_7.tStart = t  # local t and not account for scr refresh
        YouReceiveText_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(YouReceiveText_7, 'tStartRefresh')  # time at next scr refresh
        YouReceiveText_7.setAutoDraw(True)
    
    # *YouReceiveText_8* updates
    if YouReceiveText_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        YouReceiveText_8.frameNStart = frameN  # exact frame index
        YouReceiveText_8.tStart = t  # local t and not account for scr refresh
        YouReceiveText_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(YouReceiveText_8, 'tStartRefresh')  # time at next scr refresh
        YouReceiveText_8.setAutoDraw(True)
    
    # *YouReceiveText_9* updates
    if YouReceiveText_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        YouReceiveText_9.frameNStart = frameN  # exact frame index
        YouReceiveText_9.tStart = t  # local t and not account for scr refresh
        YouReceiveText_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(YouReceiveText_9, 'tStartRefresh')  # time at next scr refresh
        YouReceiveText_9.setAutoDraw(True)
    
    # *OtherReceiveText_1* updates
    if OtherReceiveText_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OtherReceiveText_1.frameNStart = frameN  # exact frame index
        OtherReceiveText_1.tStart = t  # local t and not account for scr refresh
        OtherReceiveText_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OtherReceiveText_1, 'tStartRefresh')  # time at next scr refresh
        OtherReceiveText_1.setAutoDraw(True)
    
    # *OtherReceiveText_2* updates
    if OtherReceiveText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OtherReceiveText_2.frameNStart = frameN  # exact frame index
        OtherReceiveText_2.tStart = t  # local t and not account for scr refresh
        OtherReceiveText_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OtherReceiveText_2, 'tStartRefresh')  # time at next scr refresh
        OtherReceiveText_2.setAutoDraw(True)
    
    # *OtherReceiveText_3* updates
    if OtherReceiveText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OtherReceiveText_3.frameNStart = frameN  # exact frame index
        OtherReceiveText_3.tStart = t  # local t and not account for scr refresh
        OtherReceiveText_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OtherReceiveText_3, 'tStartRefresh')  # time at next scr refresh
        OtherReceiveText_3.setAutoDraw(True)
    
    # *OtherReceiveText_4* updates
    if OtherReceiveText_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OtherReceiveText_4.frameNStart = frameN  # exact frame index
        OtherReceiveText_4.tStart = t  # local t and not account for scr refresh
        OtherReceiveText_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OtherReceiveText_4, 'tStartRefresh')  # time at next scr refresh
        OtherReceiveText_4.setAutoDraw(True)
    
    # *OtherReceiveText_5* updates
    if OtherReceiveText_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OtherReceiveText_5.frameNStart = frameN  # exact frame index
        OtherReceiveText_5.tStart = t  # local t and not account for scr refresh
        OtherReceiveText_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OtherReceiveText_5, 'tStartRefresh')  # time at next scr refresh
        OtherReceiveText_5.setAutoDraw(True)
    
    # *OtherReceiveText_6* updates
    if OtherReceiveText_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OtherReceiveText_6.frameNStart = frameN  # exact frame index
        OtherReceiveText_6.tStart = t  # local t and not account for scr refresh
        OtherReceiveText_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OtherReceiveText_6, 'tStartRefresh')  # time at next scr refresh
        OtherReceiveText_6.setAutoDraw(True)
    
    # *OtherReceiveText_7* updates
    if OtherReceiveText_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OtherReceiveText_7.frameNStart = frameN  # exact frame index
        OtherReceiveText_7.tStart = t  # local t and not account for scr refresh
        OtherReceiveText_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OtherReceiveText_7, 'tStartRefresh')  # time at next scr refresh
        OtherReceiveText_7.setAutoDraw(True)
    
    # *OtherReceiveText_8* updates
    if OtherReceiveText_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OtherReceiveText_8.frameNStart = frameN  # exact frame index
        OtherReceiveText_8.tStart = t  # local t and not account for scr refresh
        OtherReceiveText_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OtherReceiveText_8, 'tStartRefresh')  # time at next scr refresh
        OtherReceiveText_8.setAutoDraw(True)
    
    # *OtherReceiveText_9* updates
    if OtherReceiveText_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OtherReceiveText_9.frameNStart = frameN  # exact frame index
        OtherReceiveText_9.tStart = t  # local t and not account for scr refresh
        OtherReceiveText_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OtherReceiveText_9, 'tStartRefresh')  # time at next scr refresh
        OtherReceiveText_9.setAutoDraw(True)
    
    # *YouReceiveText* updates
    if YouReceiveText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        YouReceiveText.frameNStart = frameN  # exact frame index
        YouReceiveText.tStart = t  # local t and not account for scr refresh
        YouReceiveText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(YouReceiveText, 'tStartRefresh')  # time at next scr refresh
        YouReceiveText.setAutoDraw(True)
    
    # *OtherReceiveText* updates
    if OtherReceiveText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OtherReceiveText.frameNStart = frameN  # exact frame index
        OtherReceiveText.tStart = t  # local t and not account for scr refresh
        OtherReceiveText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OtherReceiveText, 'tStartRefresh')  # time at next scr refresh
        OtherReceiveText.setAutoDraw(True)
    
    # *YouDistribution* updates
    if YouDistribution.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        YouDistribution.frameNStart = frameN  # exact frame index
        YouDistribution.tStart = t  # local t and not account for scr refresh
        YouDistribution.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(YouDistribution, 'tStartRefresh')  # time at next scr refresh
        YouDistribution.setAutoDraw(True)
    
    # *OtherDistribution* updates
    if OtherDistribution.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        OtherDistribution.frameNStart = frameN  # exact frame index
        OtherDistribution.tStart = t  # local t and not account for scr refresh
        OtherDistribution.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OtherDistribution, 'tStartRefresh')  # time at next scr refresh
        OtherDistribution.setAutoDraw(True)
    
    # *TaskOutline* updates
    if TaskOutline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TaskOutline.frameNStart = frameN  # exact frame index
        TaskOutline.tStart = t  # local t and not account for scr refresh
        TaskOutline.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TaskOutline, 'tStartRefresh')  # time at next scr refresh
        TaskOutline.setAutoDraw(True)
    
    # *You_Amount_Text* updates
    if You_Amount_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        You_Amount_Text.frameNStart = frameN  # exact frame index
        You_Amount_Text.tStart = t  # local t and not account for scr refresh
        You_Amount_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(You_Amount_Text, 'tStartRefresh')  # time at next scr refresh
        You_Amount_Text.setAutoDraw(True)
    
    # *Other_Amount_Text* updates
    if Other_Amount_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Other_Amount_Text.frameNStart = frameN  # exact frame index
        Other_Amount_Text.tStart = t  # local t and not account for scr refresh
        Other_Amount_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Other_Amount_Text, 'tStartRefresh')  # time at next scr refresh
        Other_Amount_Text.setAutoDraw(True)
    
    # *key_resp* updates
    if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clock.reset()  # now t=0
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_2"-------
for thisComponent in welcome_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
for line in line_pos:
    line.autoDraw = False
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "welcome_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SVO_Trials.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    slider_2.reset()
    from psychopy.visual.slider import Slider
    from psychopy.visual.line import Line
    from psychopy import event
    
    this_trial_you = [YouReceiveText_1, YouReceiveText_2, YouReceiveText_3,
                      YouReceiveText_4, YouReceiveText_5, YouReceiveText_6,
                      YouReceiveText_7, YouReceiveText_8, YouReceiveText_9]
                      
    this_trial_other = [OtherReceiveText_1, OtherReceiveText_2, OtherReceiveText_3,
                       OtherReceiveText_4, OtherReceiveText_5, OtherReceiveText_6,
                       OtherReceiveText_7, OtherReceiveText_8, OtherReceiveText_9]
    
    # Adjust the marker size (smaller = less than default 0.05)
    slider_2.marker.size = 0.04
    
    tick_xpos = [-.5, -.375, -.25, -.125, 0, .125, .25, .375, .5]
    midpoints = []
    slider_ypos = slider_2.pos[1]
    for i in range(len(tick_xpos)-1):
        midpoint = (tick_xpos[i] + tick_xpos[i+1]) / 2
        midpoints.append(midpoint)
    
    line_pos = []
    for x in midpoints:
        line = Line(
            win,
            start = (x , slider_ypos -.04),
            end = (x , slider_ypos +.04),
            lineColor = 'gray',  
            lineWidth = 6,
            autoDraw = True
        )
        line_pos.append(line)
    
    for prefix in ['YouReceiveText_', 'OtherReceiveText_']:  # Handle both prefixes
        for i in range(1, 10):  # Covers _1 through _9
            var_name = f"{prefix}{i}"
            if var_name in locals():  # Check if variable exists
                text_value = str(locals()[var_name])  # Force string conversion
                if len(text_value) == 1:
                    locals()[var_name] = '  ' + text_value  # 2 spaces for single-digit
                elif len(text_value) == 2:
                    locals()[var_name] = ' ' + text_value   # 1 space for double-digit
                else:
                    locals()[var_name] = text_value
    YouReceiveTextTrial_1.reset()
    YouReceiveTextTrial_1.setText(YouReceiveText_1)
    YouReceiveTextTrial_2.reset()
    YouReceiveTextTrial_2.setText(YouReceiveText_2)
    YouReceiveTextTrial_3.reset()
    YouReceiveTextTrial_3.setText(YouReceiveText_3)
    YouReceiveTextTrial_4.reset()
    YouReceiveTextTrial_4.setText(YouReceiveText_4)
    YouReceiveTextTrial_5.reset()
    YouReceiveTextTrial_5.setText(YouReceiveText_5)
    YouReceiveTextTrial_6.reset()
    YouReceiveTextTrial_6.setText(YouReceiveText_6)
    YouReceiveTextTrial_7.reset()
    YouReceiveTextTrial_7.setText(YouReceiveText_7)
    YouReceiveTextTrial_8.reset()
    YouReceiveTextTrial_8.setText(YouReceiveText_8)
    YouReceiveTextTrial_9.reset()
    YouReceiveTextTrial_9.setText(YouReceiveText_9)
    OtherReceiveTextTrial_1.reset()
    OtherReceiveTextTrial_1.setText(OtherReceiveText_1)
    OtherReceiveTextTrial_2.reset()
    OtherReceiveTextTrial_2.setText(OtherReceiveText_2)
    OtherReceiveTextTrial_3.reset()
    OtherReceiveTextTrial_3.setText(OtherReceiveText_3)
    OtherReceiveTextTrial_4.reset()
    OtherReceiveTextTrial_4.setText(OtherReceiveText_4)
    OtherReceiveTextTrial_5.reset()
    OtherReceiveTextTrial_5.setText(OtherReceiveText_5)
    OtherReceiveTextTrial_6.reset()
    OtherReceiveTextTrial_6.setText(OtherReceiveText_6)
    OtherReceiveTextTrial_7.reset()
    OtherReceiveTextTrial_7.setText(OtherReceiveText_7)
    OtherReceiveTextTrial_8.reset()
    OtherReceiveTextTrial_8.setText(OtherReceiveText_8)
    OtherReceiveTextTrial_9.reset()
    OtherReceiveTextTrial_9.setText(OtherReceiveText_9)
    trial_next_space.keys = []
    trial_next_space.rt = []
    _trial_next_space_allKeys = []
    # keep track of which components have finished
    trialComponents = [slider_2, YouReceiveTextTrial_1, YouReceiveTextTrial_2, YouReceiveTextTrial_3, YouReceiveTextTrial_4, YouReceiveTextTrial_5, YouReceiveTextTrial_6, YouReceiveTextTrial_7, YouReceiveTextTrial_8, YouReceiveTextTrial_9, OtherReceiveTextTrial_1, OtherReceiveTextTrial_2, OtherReceiveTextTrial_3, OtherReceiveTextTrial_4, OtherReceiveTextTrial_5, OtherReceiveTextTrial_6, OtherReceiveTextTrial_7, OtherReceiveTextTrial_8, OtherReceiveTextTrial_9, TrialOutline, YouReceiveTextTrial, OtherReceiveTextTrial, YouAmountTextTrial, OtherAmountTextTrial, trial_next_space, YouDistributionTrial, OtherDistributionTrial, space_trial_text, text]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *slider_2* updates
        if slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_2.frameNStart = frameN  # exact frame index
            slider_2.tStart = t  # local t and not account for scr refresh
            slider_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
            slider_2.setAutoDraw(True)
        # Get precise slider position (1-9)
        slider_pos = slider_2.getRating()
        
        # Calculate neighboring positions
        lower_pos = int(np.floor(slider_pos)) - 1  # 0-7 index
        upper_pos = int(np.ceil(slider_pos)) - 1   # 0-7 index
        weight = slider_pos % 1  # How close to upper position (0-1)
        
        # Calculate weighted average (interpolation)
        if weight == 0:  # Exactly on a tick
            you_value = this_trial_you[lower_pos]
            other_value = this_trial_other[lower_pos]
        else:  # Between ticks
            you_value = (1-weight) * this_trial_you[lower_pos] + weight * this_trial_you[upper_pos]
            other_value = (1-weight) * this_trial_other[lower_pos] + weight * this_trial_other[upper_pos]
        
        # Format the values - round to integer if it's a whole number, otherwise one decimal place
        def format_value(value):
            # Round to one decimal place
            rounded = round(value, 1)
            # Check if it's effectively a whole number
            if rounded == int(rounded):
                return str(int(rounded))  # Return as integer without decimal
            else:
                return str(rounded)  # Return with one decimal place
        
        # Update displays with appropriate formatting
        YouAmountTextTrial.text = format_value(you_value)
        OtherAmountTextTrial.text = format_value(other_value)
        
        
        
        # *YouReceiveTextTrial_1* updates
        if YouReceiveTextTrial_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YouReceiveTextTrial_1.frameNStart = frameN  # exact frame index
            YouReceiveTextTrial_1.tStart = t  # local t and not account for scr refresh
            YouReceiveTextTrial_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YouReceiveTextTrial_1, 'tStartRefresh')  # time at next scr refresh
            YouReceiveTextTrial_1.setAutoDraw(True)
        
        # *YouReceiveTextTrial_2* updates
        if YouReceiveTextTrial_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YouReceiveTextTrial_2.frameNStart = frameN  # exact frame index
            YouReceiveTextTrial_2.tStart = t  # local t and not account for scr refresh
            YouReceiveTextTrial_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YouReceiveTextTrial_2, 'tStartRefresh')  # time at next scr refresh
            YouReceiveTextTrial_2.setAutoDraw(True)
        
        # *YouReceiveTextTrial_3* updates
        if YouReceiveTextTrial_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YouReceiveTextTrial_3.frameNStart = frameN  # exact frame index
            YouReceiveTextTrial_3.tStart = t  # local t and not account for scr refresh
            YouReceiveTextTrial_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YouReceiveTextTrial_3, 'tStartRefresh')  # time at next scr refresh
            YouReceiveTextTrial_3.setAutoDraw(True)
        
        # *YouReceiveTextTrial_4* updates
        if YouReceiveTextTrial_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YouReceiveTextTrial_4.frameNStart = frameN  # exact frame index
            YouReceiveTextTrial_4.tStart = t  # local t and not account for scr refresh
            YouReceiveTextTrial_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YouReceiveTextTrial_4, 'tStartRefresh')  # time at next scr refresh
            YouReceiveTextTrial_4.setAutoDraw(True)
        
        # *YouReceiveTextTrial_5* updates
        if YouReceiveTextTrial_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YouReceiveTextTrial_5.frameNStart = frameN  # exact frame index
            YouReceiveTextTrial_5.tStart = t  # local t and not account for scr refresh
            YouReceiveTextTrial_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YouReceiveTextTrial_5, 'tStartRefresh')  # time at next scr refresh
            YouReceiveTextTrial_5.setAutoDraw(True)
        
        # *YouReceiveTextTrial_6* updates
        if YouReceiveTextTrial_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YouReceiveTextTrial_6.frameNStart = frameN  # exact frame index
            YouReceiveTextTrial_6.tStart = t  # local t and not account for scr refresh
            YouReceiveTextTrial_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YouReceiveTextTrial_6, 'tStartRefresh')  # time at next scr refresh
            YouReceiveTextTrial_6.setAutoDraw(True)
        
        # *YouReceiveTextTrial_7* updates
        if YouReceiveTextTrial_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YouReceiveTextTrial_7.frameNStart = frameN  # exact frame index
            YouReceiveTextTrial_7.tStart = t  # local t and not account for scr refresh
            YouReceiveTextTrial_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YouReceiveTextTrial_7, 'tStartRefresh')  # time at next scr refresh
            YouReceiveTextTrial_7.setAutoDraw(True)
        
        # *YouReceiveTextTrial_8* updates
        if YouReceiveTextTrial_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YouReceiveTextTrial_8.frameNStart = frameN  # exact frame index
            YouReceiveTextTrial_8.tStart = t  # local t and not account for scr refresh
            YouReceiveTextTrial_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YouReceiveTextTrial_8, 'tStartRefresh')  # time at next scr refresh
            YouReceiveTextTrial_8.setAutoDraw(True)
        
        # *YouReceiveTextTrial_9* updates
        if YouReceiveTextTrial_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YouReceiveTextTrial_9.frameNStart = frameN  # exact frame index
            YouReceiveTextTrial_9.tStart = t  # local t and not account for scr refresh
            YouReceiveTextTrial_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YouReceiveTextTrial_9, 'tStartRefresh')  # time at next scr refresh
            YouReceiveTextTrial_9.setAutoDraw(True)
        
        # *OtherReceiveTextTrial_1* updates
        if OtherReceiveTextTrial_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OtherReceiveTextTrial_1.frameNStart = frameN  # exact frame index
            OtherReceiveTextTrial_1.tStart = t  # local t and not account for scr refresh
            OtherReceiveTextTrial_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OtherReceiveTextTrial_1, 'tStartRefresh')  # time at next scr refresh
            OtherReceiveTextTrial_1.setAutoDraw(True)
        
        # *OtherReceiveTextTrial_2* updates
        if OtherReceiveTextTrial_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OtherReceiveTextTrial_2.frameNStart = frameN  # exact frame index
            OtherReceiveTextTrial_2.tStart = t  # local t and not account for scr refresh
            OtherReceiveTextTrial_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OtherReceiveTextTrial_2, 'tStartRefresh')  # time at next scr refresh
            OtherReceiveTextTrial_2.setAutoDraw(True)
        
        # *OtherReceiveTextTrial_3* updates
        if OtherReceiveTextTrial_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OtherReceiveTextTrial_3.frameNStart = frameN  # exact frame index
            OtherReceiveTextTrial_3.tStart = t  # local t and not account for scr refresh
            OtherReceiveTextTrial_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OtherReceiveTextTrial_3, 'tStartRefresh')  # time at next scr refresh
            OtherReceiveTextTrial_3.setAutoDraw(True)
        
        # *OtherReceiveTextTrial_4* updates
        if OtherReceiveTextTrial_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OtherReceiveTextTrial_4.frameNStart = frameN  # exact frame index
            OtherReceiveTextTrial_4.tStart = t  # local t and not account for scr refresh
            OtherReceiveTextTrial_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OtherReceiveTextTrial_4, 'tStartRefresh')  # time at next scr refresh
            OtherReceiveTextTrial_4.setAutoDraw(True)
        
        # *OtherReceiveTextTrial_5* updates
        if OtherReceiveTextTrial_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OtherReceiveTextTrial_5.frameNStart = frameN  # exact frame index
            OtherReceiveTextTrial_5.tStart = t  # local t and not account for scr refresh
            OtherReceiveTextTrial_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OtherReceiveTextTrial_5, 'tStartRefresh')  # time at next scr refresh
            OtherReceiveTextTrial_5.setAutoDraw(True)
        
        # *OtherReceiveTextTrial_6* updates
        if OtherReceiveTextTrial_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OtherReceiveTextTrial_6.frameNStart = frameN  # exact frame index
            OtherReceiveTextTrial_6.tStart = t  # local t and not account for scr refresh
            OtherReceiveTextTrial_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OtherReceiveTextTrial_6, 'tStartRefresh')  # time at next scr refresh
            OtherReceiveTextTrial_6.setAutoDraw(True)
        
        # *OtherReceiveTextTrial_7* updates
        if OtherReceiveTextTrial_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OtherReceiveTextTrial_7.frameNStart = frameN  # exact frame index
            OtherReceiveTextTrial_7.tStart = t  # local t and not account for scr refresh
            OtherReceiveTextTrial_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OtherReceiveTextTrial_7, 'tStartRefresh')  # time at next scr refresh
            OtherReceiveTextTrial_7.setAutoDraw(True)
        
        # *OtherReceiveTextTrial_8* updates
        if OtherReceiveTextTrial_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OtherReceiveTextTrial_8.frameNStart = frameN  # exact frame index
            OtherReceiveTextTrial_8.tStart = t  # local t and not account for scr refresh
            OtherReceiveTextTrial_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OtherReceiveTextTrial_8, 'tStartRefresh')  # time at next scr refresh
            OtherReceiveTextTrial_8.setAutoDraw(True)
        
        # *OtherReceiveTextTrial_9* updates
        if OtherReceiveTextTrial_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OtherReceiveTextTrial_9.frameNStart = frameN  # exact frame index
            OtherReceiveTextTrial_9.tStart = t  # local t and not account for scr refresh
            OtherReceiveTextTrial_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OtherReceiveTextTrial_9, 'tStartRefresh')  # time at next scr refresh
            OtherReceiveTextTrial_9.setAutoDraw(True)
        
        # *TrialOutline* updates
        if TrialOutline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrialOutline.frameNStart = frameN  # exact frame index
            TrialOutline.tStart = t  # local t and not account for scr refresh
            TrialOutline.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrialOutline, 'tStartRefresh')  # time at next scr refresh
            TrialOutline.setAutoDraw(True)
        
        # *YouReceiveTextTrial* updates
        if YouReceiveTextTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YouReceiveTextTrial.frameNStart = frameN  # exact frame index
            YouReceiveTextTrial.tStart = t  # local t and not account for scr refresh
            YouReceiveTextTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YouReceiveTextTrial, 'tStartRefresh')  # time at next scr refresh
            YouReceiveTextTrial.setAutoDraw(True)
        
        # *OtherReceiveTextTrial* updates
        if OtherReceiveTextTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OtherReceiveTextTrial.frameNStart = frameN  # exact frame index
            OtherReceiveTextTrial.tStart = t  # local t and not account for scr refresh
            OtherReceiveTextTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OtherReceiveTextTrial, 'tStartRefresh')  # time at next scr refresh
            OtherReceiveTextTrial.setAutoDraw(True)
        
        # *YouAmountTextTrial* updates
        if YouAmountTextTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YouAmountTextTrial.frameNStart = frameN  # exact frame index
            YouAmountTextTrial.tStart = t  # local t and not account for scr refresh
            YouAmountTextTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YouAmountTextTrial, 'tStartRefresh')  # time at next scr refresh
            YouAmountTextTrial.setAutoDraw(True)
        
        # *OtherAmountTextTrial* updates
        if OtherAmountTextTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OtherAmountTextTrial.frameNStart = frameN  # exact frame index
            OtherAmountTextTrial.tStart = t  # local t and not account for scr refresh
            OtherAmountTextTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OtherAmountTextTrial, 'tStartRefresh')  # time at next scr refresh
            OtherAmountTextTrial.setAutoDraw(True)
        
        # *trial_next_space* updates
        if trial_next_space.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_next_space.frameNStart = frameN  # exact frame index
            trial_next_space.tStart = t  # local t and not account for scr refresh
            trial_next_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_next_space, 'tStartRefresh')  # time at next scr refresh
            trial_next_space.status = STARTED
            # keyboard checking is just starting
            trial_next_space.clock.reset()  # now t=0
        if trial_next_space.status == STARTED:
            theseKeys = trial_next_space.getKeys(keyList=['space'], waitRelease=False)
            _trial_next_space_allKeys.extend(theseKeys)
            if len(_trial_next_space_allKeys):
                trial_next_space.keys = _trial_next_space_allKeys[-1].name  # just the last key pressed
                trial_next_space.rt = _trial_next_space_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *YouDistributionTrial* updates
        if YouDistributionTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            YouDistributionTrial.frameNStart = frameN  # exact frame index
            YouDistributionTrial.tStart = t  # local t and not account for scr refresh
            YouDistributionTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(YouDistributionTrial, 'tStartRefresh')  # time at next scr refresh
            YouDistributionTrial.setAutoDraw(True)
        
        # *OtherDistributionTrial* updates
        if OtherDistributionTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OtherDistributionTrial.frameNStart = frameN  # exact frame index
            OtherDistributionTrial.tStart = t  # local t and not account for scr refresh
            OtherDistributionTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OtherDistributionTrial, 'tStartRefresh')  # time at next scr refresh
            OtherDistributionTrial.setAutoDraw(True)
        
        # *space_trial_text* updates
        if space_trial_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_trial_text.frameNStart = frameN  # exact frame index
            space_trial_text.tStart = t  # local t and not account for scr refresh
            space_trial_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_trial_text, 'tStartRefresh')  # time at next scr refresh
            space_trial_text.setAutoDraw(True)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('slider_2.response', slider_2.getRating())
    trials.addData('slider_2.rt', slider_2.getRT())
    # Remove minor tick lines after trial
    for line in line_pos:
        line.autoDraw = False
    
    # Save trial data 
    thisExp.addData('You_Distribution', float(YouAmountTextTrial.text))
    thisExp.addData('Other_Distribution', float(OtherAmountTextTrial.text))
    
    
    # Save data to lists for scoring
    raw_self.append(float(YouAmountTextTrial.text))
    raw_other.append(float(OtherAmountTextTrial.text))
    
    # check responses
    if trial_next_space.keys in ['', [], None]:  # No response was made
        trial_next_space.keys = None
    trials.addData('trial_next_space.keys',trial_next_space.keys)
    if trial_next_space.keys != None:  # we had a response
        trials.addData('trial_next_space.rt', trial_next_space.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
space_end.keys = []
space_end.rt = []
_space_end_allKeys = []
import numpy as np
# Scoring - Murphy, R. O., Ackermann, K. A., & Handgraaf, M. J. J. (2011)
self_30 = np.array(raw_self) - 50
other_30 = np.array(raw_other) - 50

mean_self = np.mean(self_30)
mean_other = np.mean(other_30)

ratio = mean_other / mean_self

angle_rad = np.arctan(ratio)
angle_deg = np.degrees(angle_rad)

def classify_svo(angle):
    if angle > 57.15:
        return "Altruistic"
    elif 22.45 < angle < 57.15:
        return "Prosocial"
    elif -12.04 < angle < 22.45:
        return "Individualistic"
    elif angle < -12.04:
        return "Competitive"

# Get SVO classification
svo_category = classify_svo(angle_deg)

# Store the result
thisExp.addData('SVO_angle_deg', angle_deg)
thisExp.addData('SVO_category', svo_category)
'''
print(f'mean self: {mean_self}')
print(f'mean other: {mean_other}')
print(f'angle: {angle_deg}')
print(svo_category)
'''
# keep track of which components have finished
EndComponents = [end_text, space_end]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    
    # *space_end* updates
    if space_end.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_end.frameNStart = frameN  # exact frame index
        space_end.tStart = t  # local t and not account for scr refresh
        space_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_end, 'tStartRefresh')  # time at next scr refresh
        space_end.status = STARTED
        # keyboard checking is just starting
        space_end.clock.reset()  # now t=0
    if space_end.status == STARTED:
        theseKeys = space_end.getKeys(keyList=['space'], waitRelease=False)
        _space_end_allKeys.extend(theseKeys)
        if len(_space_end_allKeys):
            space_end.keys = _space_end_allKeys[-1].name  # just the last key pressed
            space_end.rt = _space_end_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if space_end.keys in ['', [], None]:  # No response was made
    space_end.keys = None
thisExp.addData('space_end.keys',space_end.keys)
if space_end.keys != None:  # we had a response
    thisExp.addData('space_end.rt', space_end.rt)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
