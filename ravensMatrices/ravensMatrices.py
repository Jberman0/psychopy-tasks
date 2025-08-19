#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on August 18, 2025, at 22:40
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
import shutil

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'ravensMatricesBuilder'  # from the Builder filename that created this script
expInfo = {'participantID': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participantID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='ravensMatricesBuilder.py',
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
    size=[1920, 1080], fullscr=False, screen=0, 
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

# Initialize components for Routine "IntroText"
IntroTextClock = core.Clock()
Intro = visual.TextStim(win=win, name='Intro',
    text='We are beginning the Puzzle Task.\n\nIn this task, you will be shown a series of puzzles. For each puzzle, your goal is to identify the MISSING piece from the options appearing to the right of the puzzle.\n\nThere are 9 puzzles in total. You will have 30 seconds for EACH puzzle.\n\nTry to be as accurate as you can be. If you cannot solve the puzzle before time runs out, then you should guess.\n\nPress SPACE to begin.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
introNext = keyboard.Keyboard()

# Initialize components for Routine "beginText"
beginTextClock = core.Clock()
begin = visual.TextStim(win=win, name='begin',
    text='5',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
Stimuli = visual.ImageStim(
    win=win,
    name='Stimuli', 
    image='sin', mask=None,
    ori=0.0, pos=(-.5, 0), size=(0.6, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
n_choices = 0
col_wrap = 0
choice_1 = visual.ImageStim(
    win=win,
    name='choice_1', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
choice_2 = visual.ImageStim(
    win=win,
    name='choice_2', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
choice_3 = visual.ImageStim(
    win=win,
    name='choice_3', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
choice_4 = visual.ImageStim(
    win=win,
    name='choice_4', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
choice_5 = visual.ImageStim(
    win=win,
    name='choice_5', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
choice_6 = visual.ImageStim(
    win=win,
    name='choice_6', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
choice_7 = visual.ImageStim(
    win=win,
    name='choice_7', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
choice_8 = visual.ImageStim(
    win=win,
    name='choice_8', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
timer = visual.TextStim(win=win, name='timer',
    text='5',
    font='Open Sans',
    pos=(-.78,.43), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "end"
endClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='Thank you for playing.\n\nThe experiment will now end.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "IntroText"-------
continueRoutine = True
# update component parameters for each repeat
introNext.keys = []
introNext.rt = []
_introNext_allKeys = []
# keep track of which components have finished
IntroTextComponents = [Intro, introNext]
for thisComponent in IntroTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "IntroText"-------
while continueRoutine:
    # get current time
    t = IntroTextClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroTextClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Intro* updates
    if Intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Intro.frameNStart = frameN  # exact frame index
        Intro.tStart = t  # local t and not account for scr refresh
        Intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro, 'tStartRefresh')  # time at next scr refresh
        Intro.setAutoDraw(True)
    
    # *introNext* updates
    waitOnFlip = False
    if introNext.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        introNext.frameNStart = frameN  # exact frame index
        introNext.tStart = t  # local t and not account for scr refresh
        introNext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introNext, 'tStartRefresh')  # time at next scr refresh
        introNext.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(introNext.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(introNext.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if introNext.status == STARTED and not waitOnFlip:
        theseKeys = introNext.getKeys(keyList=['space'], waitRelease=False)
        _introNext_allKeys.extend(theseKeys)
        if len(_introNext_allKeys):
            introNext.keys = _introNext_allKeys[-1].name  # just the last key pressed
            introNext.rt = _introNext_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "IntroText"-------
for thisComponent in IntroTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Intro.started', Intro.tStartRefresh)
thisExp.addData('Intro.stopped', Intro.tStopRefresh)
# check responses
if introNext.keys in ['', [], None]:  # No response was made
    introNext.keys = None
thisExp.addData('introNext.keys',introNext.keys)
if introNext.keys != None:  # we had a response
    thisExp.addData('introNext.rt', introNext.rt)
thisExp.addData('introNext.started', introNext.tStartRefresh)
thisExp.addData('introNext.stopped', introNext.tStopRefresh)
thisExp.nextEntry()
# the Routine "IntroText" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "beginText"-------
continueRoutine = True
# update component parameters for each repeat
trial_timer = core.Clock()
time_left = 3
# keep track of which components have finished
beginTextComponents = [begin]
for thisComponent in beginTextComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beginTextClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "beginText"-------
while continueRoutine:
    # get current time
    t = beginTextClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beginTextClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin* updates
    if begin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin.frameNStart = frameN  # exact frame index
        begin.tStart = t  # local t and not account for scr refresh
        begin.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin, 'tStartRefresh')  # time at next scr refresh
        begin.setAutoDraw(True)
    time_left = 3 - trial_timer.getTime()
    
    if 0 < time_left <= 3:
        begin.text = str(round(time_left))
    
    
    if trial_timer.getTime() >= 3:
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginTextComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "beginText"-------
for thisComponent in beginTextComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('begin.started', begin.tStartRefresh)
thisExp.addData('begin.stopped', begin.tStopRefresh)
# the Routine "beginText" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trials.csv'),
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
    Stimuli.setImage(stimulus)
    # Split CSV into a list of choices
    choices = [choice.strip() for choice in choices.split(',')]
    n_choices = len(choices)
    start_time = globalClock.getTime()
    trial_timer = core.Clock()
    
    #Show active choices
    for i in range(8):
        choice = globals()[(f'choice_{i+1}')]
        if i < n_choices:
            choice.image = choices[i]
            choice.setAutoDraw(True)
            choice.opacity = 1
            if n_choices == 6:
                row = i // 3
                col = i % 3
                x_pos = 0.1 + (0.25 * col)
                y_pos = 0.13 - (0.25 * row)
            else:
                if i < 6:
                    row = i // 3
                    col = i % 3
                    x_pos = 0.1 + (0.25 * col)
                    y_pos = 0.23 - (0.25 * row)
                else:
                    x_pos = 0.225 + (0.25 * (i-6))
                    y_pos = -0.27
        else:
            choice.setAutoDraw(False)
            choice.opacity = 0
        choice.pos = [x_pos, y_pos]
        choice.size = [0.2, 0.2]
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    trialComponents = [Stimuli, choice_1, choice_2, choice_3, choice_4, choice_5, choice_6, choice_7, choice_8, mouse, timer]
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
        
        # *Stimuli* updates
        if Stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Stimuli.frameNStart = frameN  # exact frame index
            Stimuli.tStart = t  # local t and not account for scr refresh
            Stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli, 'tStartRefresh')  # time at next scr refresh
            Stimuli.setAutoDraw(True)
        time_left = 30 - trial_timer.getTime()
        
        if 0 < time_left <= 5:
            timer.text = str(round(time_left, 1))
        
        
        if trial_timer.getTime() >= 30:
            continueRoutine = False
        
        # *choice_1* updates
        if choice_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_1.frameNStart = frameN  # exact frame index
            choice_1.tStart = t  # local t and not account for scr refresh
            choice_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_1, 'tStartRefresh')  # time at next scr refresh
            choice_1.setAutoDraw(True)
        
        # *choice_2* updates
        if choice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_2.frameNStart = frameN  # exact frame index
            choice_2.tStart = t  # local t and not account for scr refresh
            choice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_2, 'tStartRefresh')  # time at next scr refresh
            choice_2.setAutoDraw(True)
        
        # *choice_3* updates
        if choice_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_3.frameNStart = frameN  # exact frame index
            choice_3.tStart = t  # local t and not account for scr refresh
            choice_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_3, 'tStartRefresh')  # time at next scr refresh
            choice_3.setAutoDraw(True)
        
        # *choice_4* updates
        if choice_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_4.frameNStart = frameN  # exact frame index
            choice_4.tStart = t  # local t and not account for scr refresh
            choice_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_4, 'tStartRefresh')  # time at next scr refresh
            choice_4.setAutoDraw(True)
        
        # *choice_5* updates
        if choice_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_5.frameNStart = frameN  # exact frame index
            choice_5.tStart = t  # local t and not account for scr refresh
            choice_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_5, 'tStartRefresh')  # time at next scr refresh
            choice_5.setAutoDraw(True)
        
        # *choice_6* updates
        if choice_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_6.frameNStart = frameN  # exact frame index
            choice_6.tStart = t  # local t and not account for scr refresh
            choice_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_6, 'tStartRefresh')  # time at next scr refresh
            choice_6.setAutoDraw(True)
        
        # *choice_7* updates
        if choice_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_7.frameNStart = frameN  # exact frame index
            choice_7.tStart = t  # local t and not account for scr refresh
            choice_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_7, 'tStartRefresh')  # time at next scr refresh
            choice_7.setAutoDraw(True)
        
        # *choice_8* updates
        if choice_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_8.frameNStart = frameN  # exact frame index
            choice_8.tStart = t  # local t and not account for scr refresh
            choice_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_8, 'tStartRefresh')  # time at next scr refresh
            choice_8.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([choice_1,choice_2,choice_3,choice_4,choice_5,choice_6,choice_7,choice_8])
                        clickableList = [choice_1,choice_2,choice_3,choice_4,choice_5,choice_6,choice_7,choice_8]
                    except:
                        clickableList = [[choice_1,choice_2,choice_3,choice_4,choice_5,choice_6,choice_7,choice_8]]
                    for obj in clickableList:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *timer* updates
        if timer.status == NOT_STARTED and tThisFlip >= 25-frameTolerance:
            # keep track of start time/frame for later
            timer.frameNStart = frameN  # exact frame index
            timer.tStart = t  # local t and not account for scr refresh
            timer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timer, 'tStartRefresh')  # time at next scr refresh
            timer.setAutoDraw(True)
        if timer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > timer.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                timer.tStop = t  # not accounting for scr refresh
                timer.frameNStop = frameN  # exact frame index
                win.timeOnFlip(timer, 'tStopRefresh')  # time at next scr refresh
                timer.setAutoDraw(False)
        if timer.status == STARTED:  # only update if drawing
            timer.setColor('red', colorSpace='rgb', log=False)
        
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
    trials.addData('Stimuli.started', Stimuli.tStartRefresh)
    trials.addData('Stimuli.stopped', Stimuli.tStopRefresh)
    thisExp.addData('trial.time', globalClock.getTime() - start_time)
    
    try:
        current_choice = mouse.clicked_name[0]
        if current_choice == f'choice_{correct + 1}':
            thisExp.addData('trial.correct', 1)
        else:
            thisExp.addData('trial.correct', 0)
    except:
        continueRoutine = False
    # store data for trials (TrialHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([choice_1,choice_2,choice_3,choice_4,choice_5,choice_6,choice_7,choice_8])
            clickableList = [choice_1,choice_2,choice_3,choice_4,choice_5,choice_6,choice_7,choice_8]
        except:
            clickableList = [[choice_1,choice_2,choice_3,choice_4,choice_5,choice_6,choice_7,choice_8]]
        for obj in clickableList:
            if obj.contains(mouse):
                gotValidClick = True
                mouse.clicked_name.append(obj.name)
    trials.addData('mouse.x', x)
    trials.addData('mouse.y', y)
    trials.addData('mouse.leftButton', buttons[0])
    trials.addData('mouse.midButton', buttons[1])
    trials.addData('mouse.rightButton', buttons[2])
    if len(mouse.clicked_name):
        trials.addData('mouse.clicked_name', mouse.clicked_name[0])
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(2.500000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [endText]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    if endText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endText.tStartRefresh + 2.5-frameTolerance:
            # keep track of stop time/frame for later
            endText.tStop = t  # not accounting for scr refresh
            endText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(endText, 'tStopRefresh')  # time at next scr refresh
            endText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endText.started', endText.tStartRefresh)
thisExp.addData('endText.stopped', endText.tStopRefresh)
import math

def dot_product(x, y):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * y[i]
    return sum

# Extract the relevant data from the experiment
# Looking at the 'trial.correct' column which contains 1 for correct and 0 for incorrect
accuracy = []
reaction_times = []

for trial in range(len(thisExp.entries)):
    # Check if this is a trial with stimulus and correctness data
    if 'stimulus' in thisExp.entries[trial] and 'trial.correct' in thisExp.entries[trial]:
        if thisExp.entries[trial]['stimulus'] != '':  # Only include actual trials
            accuracy.append(thisExp.entries[trial]['trial.correct'])
            reaction_times.append(thisExp.entries[trial]['trial.time'])

# Calculate scores
rpm_raw = sum(accuracy)
rpm_err = 9 - rpm_raw
rpm_rt = sum(reaction_times)

# Convert errors to the format needed (1 for error, 0 for correct)
errors = [1 - acc for acc in accuracy]

# Score RPM using Bilker et al. 2012 formula
weights = [0.168, 0.212, 0.247, 0.189, 0.203, 0.135, 0.243, 0.316, 0.193]
rpm_adj = 60 - (rpm_err + math.exp(1.875 + dot_product(errors, weights)))

# Store results in experiment data
thisExp.addData('rpm_raw', rpm_raw)
thisExp.addData('rpm_err', rpm_err)
thisExp.addData('rpm_adj', rpm_adj)
thisExp.addData('rpm_rt', rpm_rt)

'''
# Print results to output for verification
print(f"RPM Raw Score: {rpm_raw}")
print(f"RPM Error Count: {rpm_err}")
print(f"RPM Adjusted Score: {rpm_adj:.2f}")
print(f"RPM Total Response Time: {rpm_rt:.2f}")
'''

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()

# Save to Box
try:
    box_path = r"C:\Users\Josh\Box\box-group-sldlab\slb\fMRI\post_scan\digit_span"
    src_path = filename
    dst_path = os.path.join(box_path, os.path.basename(filename))
    shutil.copy2(src_path, dst_path)

except Exception as e:
    print(f"Error saving to Box: {e}")

# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
