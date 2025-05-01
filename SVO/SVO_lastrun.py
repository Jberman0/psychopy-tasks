#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on April 30, 2025, at 17:52
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
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Josh\\Downloads\\SVO\\SVO_lastrun.py',
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
    pos=(0, .3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
slider_1 = visual.Slider(win=win, name='slider_1',
    startValue=5, size=(1.0, 0.15), pos=(0, -.12), units=None,
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
     pos=(-.5, 0.08),     letterHeight=0.05,
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
     pos=(-.375, 0.08),     letterHeight=0.05,
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
     pos=(-.125, 0.08),     letterHeight=0.05,
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
     pos=(-.25, 0.08),     letterHeight=0.05,
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
     pos=(0, 0.08),     letterHeight=0.05,
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
     pos=(.25, 0.08),     letterHeight=0.05,
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
     pos=(.125, 0.08),     letterHeight=0.05,
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
     pos=(.375, 0.08),     letterHeight=0.05,
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
     pos=(.5, 0.08),     letterHeight=0.05,
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
     pos=(-.5, -.18),     letterHeight=0.05,
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
     pos=(-.375, -.18),     letterHeight=0.05,
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
     pos=(-.125, -.18),     letterHeight=0.05,
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
     pos=(-.25, -.18),     letterHeight=0.05,
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
     pos=(0, -.18),     letterHeight=0.05,
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
     pos=(.25, -.18),     letterHeight=0.05,
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
     pos=(.125, -.18),     letterHeight=0.05,
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
     pos=(.375, -.18),     letterHeight=0.05,
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
     pos=(.5, -.18),     letterHeight=0.05,
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
    pos=(-.72, 0.08), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
OtherReceiveText = visual.TextStim(win=win, name='OtherReceiveText',
    text='Other receives',
    font='Open Sans',
    pos=(-.72, -.18), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-23.0);
YouDistribution = visual.TextStim(win=win, name='YouDistribution',
    text='You',
    font='Open Sans',
    pos=(.65, 0.08), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-24.0);
OtherDistribution = visual.TextStim(win=win, name='OtherDistribution',
    text='Other',
    font='Open Sans',
    pos=(.65, -.18), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-25.0);
TaskOutline = visual.Rect(
    win=win, name='TaskOutline',
    width=(1.43, 0.4)[0], height=(1.43, 0.4)[1],
    ori=0.0, pos=(-.15, -.05),
    lineWidth=4.0,     colorSpace='rgb',  lineColor='white', fillColor='grey',
    opacity=0.2, depth=-26.0, interpolate=True)
You_Amount_Text = visual.TextStim(win=win, name='You_Amount_Text',
    text='50',
    font='Open Sans',
    pos=(.75, 0.08), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-27.0);
Other_Amount_Text = visual.TextStim(win=win, name='Other_Amount_Text',
    text='40',
    font='Open Sans',
    pos=(.75, -.18), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-28.0);

# Initialize components for Routine "welcome_3"
welcome_3Clock = core.Clock()

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
    waitOnFlip = False
    if IntroKey_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IntroKey_1.frameNStart = frameN  # exact frame index
        IntroKey_1.tStart = t  # local t and not account for scr refresh
        IntroKey_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroKey_1, 'tStartRefresh')  # time at next scr refresh
        IntroKey_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(IntroKey_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(IntroKey_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if IntroKey_1.status == STARTED and not waitOnFlip:
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
thisExp.addData('IntroKey_1.started', IntroKey_1.tStartRefresh)
thisExp.addData('IntroKey_1.stopped', IntroKey_1.tStopRefresh)
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
# keep track of which components have finished
welcome_2Components = [IntroText_2, slider_1, IntroText_3, YouReceiveText_1, YouReceiveText_2, YouReceiveText_3, YouReceiveText_4, YouReceiveText_5, YouReceiveText_6, YouReceiveText_7, YouReceiveText_8, YouReceiveText_9, OtherReceiveText_1, OtherReceiveText_2, OtherReceiveText_3, OtherReceiveText_4, OtherReceiveText_5, OtherReceiveText_6, OtherReceiveText_7, OtherReceiveText_8, OtherReceiveText_9, YouReceiveText, OtherReceiveText, YouDistribution, OtherDistribution, TaskOutline, You_Amount_Text, Other_Amount_Text]
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
    slider_1.getMarkerPos()
    
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
thisExp.addData('slider_1.response', slider_1.getRating())
thisExp.addData('slider_1.rt', slider_1.getRT())
thisExp.addData('slider_1.started', slider_1.tStartRefresh)
thisExp.addData('slider_1.stopped', slider_1.tStopRefresh)
thisExp.addData('IntroText_3.started', IntroText_3.tStartRefresh)
thisExp.addData('IntroText_3.stopped', IntroText_3.tStopRefresh)
thisExp.addData('YouReceiveText.started', YouReceiveText.tStartRefresh)
thisExp.addData('YouReceiveText.stopped', YouReceiveText.tStopRefresh)
thisExp.addData('OtherReceiveText.started', OtherReceiveText.tStartRefresh)
thisExp.addData('OtherReceiveText.stopped', OtherReceiveText.tStopRefresh)
thisExp.addData('YouDistribution.started', YouDistribution.tStartRefresh)
thisExp.addData('YouDistribution.stopped', YouDistribution.tStopRefresh)
thisExp.addData('OtherDistribution.started', OtherDistribution.tStartRefresh)
thisExp.addData('OtherDistribution.stopped', OtherDistribution.tStopRefresh)
thisExp.addData('You_Amount_Text.started', You_Amount_Text.tStartRefresh)
thisExp.addData('You_Amount_Text.stopped', You_Amount_Text.tStopRefresh)
thisExp.addData('Other_Amount_Text.started', Other_Amount_Text.tStartRefresh)
thisExp.addData('Other_Amount_Text.stopped', Other_Amount_Text.tStopRefresh)
# the Routine "welcome_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome_3"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
welcome_3Components = []
for thisComponent in welcome_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcome_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome_3"-------
while continueRoutine:
    # get current time
    t = welcome_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcome_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_3"-------
for thisComponent in welcome_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome_3" was not non-slip safe, so reset the non-slip timer
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
