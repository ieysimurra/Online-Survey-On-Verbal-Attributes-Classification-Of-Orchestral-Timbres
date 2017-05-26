#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Tue 23 May 2017 03:29:12 PM BRT
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'teste_experiment'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'age': u'', u'session': u'001', u'participant': u'', u'pro_experience': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1366, 768), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "presentation"
presentationClock = core.Clock()
presentation_text = visual.TextStim(win=win, name='presentation_text',
    text='Online Survey \n\nOn Verbal Attributes Classification \n\nOf \n\nOrchestral Timbres',
    font='Neuropolitical',
    pos=(0, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
presentation_text2 = visual.TextStim(win=win, name='presentation_text2',
    text="Press 'space' to continue",
    font='Times New Roman',
    pos=(0.81, -0.83), height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-1.0);
presentation_image = visual.ImageStim(
    win=win, name='presentation_image',
    image='compmus.png', mask=None,
    ori=0, pos=(0, 0.75), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
presentation_image2 = visual.ImageStim(
    win=win, name='presentation_image2',
    image='fapesp.png', mask=None,
    ori=0, pos=(-0.81, -0.83), size=(0.25, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "instructions1"
instructions1Clock = core.Clock()
text_instructions11 = visual.TextStim(win=win, name='text_instructions11',
    text='Hey, you!\n\nWelcome and thank you for your interest in our survey\nwhich shall be part of the evaluation of the research developed by the Computer Music Research Group at University of Sao Paulo - USP/Brazil\n\nPlease take time to read the following information carefully. \nIf there is anything that is not clear or if you would like more information, please ask us by writing to ieys[at]ime.usp.br',
    font='Arial',
    pos=(0, 0.53), height=0.059, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text_instructions_12 = visual.TextStim(win=win, name='text_instructions_12',
    text='The purpose of the survey is to analyze some verbal attributes used to describe intuitively the sound perception of a set of Orchestral Timbres.\nIt will take approximately 40 minutes to complete the survey.\n',
    font='Arial',
    pos=(0.01, -0.17), height=0.059, wrapWidth=None, ori=0, 
    color=[1.000,0.294,-1.000], colorSpace='rgb', opacity=1,
    depth=-1.0);
text_instructions_13 = visual.TextStim(win=win, name='text_instructions_13',
    text='Your participation in this experiment is completely voluntary. \nIf you wish to stop participating, you may do so at any time.\n',
    font='Arial',
    pos=(-0.07, -0.53), height=0.059, wrapWidth=None, ori=0, 
    color=[1.000,0.506,0.592], colorSpace='rgb', opacity=1,
    depth=-2.0);
text_instructions_14 = visual.TextStim(win=win, name='text_instructions_14',
    text="Press 'space' to continue",
    font='Times New Roman',
    pos=(0.81, -0.83), height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
text_instructions21 = visual.TextStim(win=win, name='text_instructions21',
    text='Specific Instructions\n\nIn this survey:\n\n-> You will be presented to 33 musical audio-examples of 5 seconds duration each\n\n-> You will rate them by a set of several 7-points scales on verbal attributes (e.g.: from attribute xxx to attribute yyy)\n\n-> There are 13 scales that are going to be used to evaluate the sound stimuli. Rate them according to the appropriateness of each scale to each of excerpts that it will be heard.',
    font='Arial',
    pos=(0, 0.47), height=0.059, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text_instructions22 = visual.TextStim(win=win, name='text_instructions22',
    text='Example',
    font='Arial',
    pos=(-0.03, -0.07), height=0.19, wrapWidth=None, ori=0, 
    color=[-0.765,0.129,1.000], colorSpace='rgb', opacity=1,
    depth=-1.0);
text_instructions23 = visual.TextStim(win=win, name='text_instructions23',
    text=u"-> Attribute xxx \u2194 Attribute yyy (please, mark in only one cell)\n    Extremely xxx \u2013 Moderately xxx \u2013 Slightly xxx \u2013 Neutral - Slightly yyy\n    Moderately yyy \u2013 Extremely yyy\n-> Please, after selecting your choice press the 'Key, Click' button to confirm your alternative",
    font='Arial',
    pos=(-0.01, -0.37), height=0.059, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
rating = visual.RatingScale(win=win, name='rating', marker='circle', size=0.9, pos=[0.0, -0.7], low=1, high=7, labels=['Hard', ' Soft'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
text_instructions24 = visual.TextStim(win=win, name='text_instructions24',
    text="Press 'space' to continue",
    font='Times New Roman',
    pos=(0.81, -0.83), height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "instructions3"
instructions3Clock = core.Clock()
text_instructions32 = visual.TextStim(win=win, name='text_instructions32',
    text='Please make sure to carefully listen to the audio excerpts in full duration\n\nYou will first start with a training example which should allow you to familiarise yourself with the type of stimuli in the experiment.',
    font='Arial',
    pos=(0, -0.07), height=0.059, wrapWidth=None, ori=0, 
    color=[0.004,-1.000,0.004], colorSpace='rgb', opacity=1,
    depth=0.0);
text_instructions33 = visual.TextStim(win=win, name='text_instructions33',
    text='Good quality headphones or external speakers and a quiet environment are required as the survey involves listening to sound clips.',
    font='Arial',
    pos=(0, -0.35), height=0.059, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_instructions34 = visual.TextStim(win=win, name='text_instructions34',
    text="To begin the experiment, please press the 'y' key. By pressing this key, you confirm that you have read and understood the experiment instructions and give your consent for your rating data to be anonymously analysed when reporting experimental results.\n\nThe data gathered from this survey will only be used as research purpose",
    font='Arial',
    pos=(0, -0.73), height=0.059, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-2.0);
text_instructions31 = visual.TextStim(win=win, name='text_instructions31',
    text='\nThese are the scales that are going to be used to evaluate thesound stimuli\n\n                                                    * 01 - Hard <-> Soft\n                                                    * 02 - Colorless <-> Colorful\n                                                    * 03 - Dull <-> Sharp\n                                                    * 04 - Heavy <-> Lightweight\n                                                    * 05 - Complex <-> Simple\n                                                    * 06 - Cold <-> Warm\n                                                    * 07 - Dim <-> Bright\n                                                    * 08 - Mixed <-> Pure\n                                                    * 09 - Strong <-> Weak\n                                                    * 10 - Full <-> Empty\n                                                    * 11 - Rough <-> Smooth\n                                                    * 12 - Thick <-> Thin\n                                                    * 13 - Scattered <-> Compact',
    font='Arial',
    pos=(-0.1, 0.57), height=0.047, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
text_instructions35 = visual.TextStim(win=win, name='text_instructions35',
    text="Prees 'y' to continue",
    font='Times New Roman',
    pos=(0.81, -0.83), height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-5.0);

# Initialize components for Routine "exposure"
exposureClock = core.Clock()
exposure_sound = sound.Sound('/home/ieysimurra/Documents/psychopy_backup/pilot/sounds/exposure.wav', secs=-1)
exposure_sound.setVolume(1)
exposure_text = visual.TextStim(win=win, name='exposure_text',
    text='Training Step',
    font='Arial',
    pos=(-0.7, 0.95), height=0.081, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=0.7, pos=[-0.7, 0.7], low=1, high=7, labels=['Hard', 'Soft'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
rating_3 = visual.RatingScale(win=win, name='rating_3', marker='triangle', size=0.7, pos=[-0.7, 0.3], low=1, high=7, labels=['Colorless', ' Colorful'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
rating_4 = visual.RatingScale(win=win, name='rating_4', marker='triangle', size=0.7, pos=[-0.7, -0.1], low=1, high=7, labels=['Dull', ' Sharp'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
rating_5 = visual.RatingScale(win=win, name='rating_5', marker='triangle', size=0.7, pos=[-0.7, -0.5], low=1, high=7, labels=['Heayv', ' Lighteight'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
rating_6 = visual.RatingScale(win=win, name='rating_6', marker='triangle', size=0.7, pos=[0.0, 0.8], low=1, high=7, labels=['Complex', ' Simple'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
rating_7 = visual.RatingScale(win=win, name='rating_7', marker='triangle', size=0.7, pos=[0.0, 0.4], low=1, high=7, labels=['Cold', ' Warm'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
rating_8 = visual.RatingScale(win=win, name='rating_8', marker='triangle', size=0.7, pos=[0.0, 0.0], low=1, high=7, labels=['Dim', ' Bright'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
rating_9 = visual.RatingScale(win=win, name='rating_9', marker='triangle', size=0.7, pos=[0.0, -0.4], low=1, high=7, labels=['Mixed', ' Pure'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
rating_10 = visual.RatingScale(win=win, name='rating_10', marker='triangle', size=0.7, pos=[0.0, -0.79], low=1, high=7, labels=['Strong', ' Weak'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
rating_11 = visual.RatingScale(win=win, name='rating_11', marker='triangle', size=0.7, pos=[0.7, 0.7], low=1, high=7, labels=['Full', ' Empty'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
rating_12 = visual.RatingScale(win=win, name='rating_12', marker='triangle', size=0.7, pos=[0.7, 0.3], low=1, high=7, labels=['Rough', ' Smooth'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
rating_13 = visual.RatingScale(win=win, name='rating_13', marker='triangle', size=0.7, pos=[0.7, -0.1], low=1, high=7, labels=['Thick', ' Thin'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
rating_14 = visual.RatingScale(win=win, name='rating_14', marker='triangle', size=0.7, pos=[0.7, -0.5], low=1, high=7, labels=['Scattered', ' Compact'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
exposure_text2 = visual.TextStim(win=win, name='exposure_text2',
    text="Press 'space' to continue",
    font='Arial',
    pos=(0.71, -0.91), height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-15.0);

exposure_text3 = visual.TextStim(win=win, name='exposure_text3',
    text=u"Press 'p' to play stimulus again",
    font=u'Arial',
    pos=(-0.71, -0.91), height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-18.0);

# Initialize components for Routine "ready"
readyClock = core.Clock()
text_ready1 = visual.TextStim(win=win, name='text_ready1',
    text="READY?\n\n(please, press 'return' to start experiment)",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "listening_exp"
listening_expClock = core.Clock()
listening_sound = sound.Sound('A', secs=-1)
listening_sound.setVolume(1)
listening_hard_soft = visual.RatingScale(win=win, name='listening_hard_soft', marker='triangle', size=0.7, pos=[-0.7, 0.7], low=1, high=7, labels=['Hard', 'Soft'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_colorless_Colorful = visual.RatingScale(win=win, name='listening_colorless_Colorful', marker='triangle', size=0.7, pos=[-0.7, 0.3], low=1, high=7, labels=['Colorless', 'Colorful'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_dull_dharp = visual.RatingScale(win=win, name='listening_dull_dharp', marker='triangle', size=0.7, pos=[-0.7, -0.1], low=1, high=7, labels=['Dull', 'Sharp'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_heavy_lightweight = visual.RatingScale(win=win, name='listening_heavy_lightweight', marker='triangle', size=0.7, pos=[-0.7, -0.5], low=1, high=7, labels=['Heavy', 'Lightweight'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_complex_simple = visual.RatingScale(win=win, name='listening_complex_simple', marker='triangle', size=0.7, pos=[0.0, 0.8], low=1, high=7, labels=['Complex', 'Simple'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_cold_warm = visual.RatingScale(win=win, name='listening_cold_warm', marker='triangle', size=0.7, pos=[0.0, 0.4], low=1, high=7, labels=['Cold', 'Warm'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_dim_bright = visual.RatingScale(win=win, name='listening_dim_bright', marker='triangle', size=0.7, pos=[0.0, 0.0], low=1, high=7, labels=['Dim', 'Bright'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_mixed_pure = visual.RatingScale(win=win, name='listening_mixed_pure', marker='triangle', size=0.7, pos=[0.0, -0.4], low=1, high=7, labels=['Mixed', 'Pure'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_strong_weak = visual.RatingScale(win=win, name='listening_strong_weak', marker='triangle', size=0.7, pos=[0.0, -0.79], low=1, high=7, labels=['Strong', 'Weak'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_full_empty = visual.RatingScale(win=win, name='listening_full_empty', marker='triangle', size=0.7, pos=[0.7, 0.7], low=1, high=7, labels=['Full', 'Empty'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_rough_smooth = visual.RatingScale(win=win, name='listening_rough_smooth', marker='triangle', size=0.7, pos=[0.7, 0.3], low=1, high=7, labels=['Rough', 'Smooth'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_thick_thin = visual.RatingScale(win=win, name='listening_thick_thin', marker='triangle', size=0.7, pos=[0.7, -0.1], low=1, high=7, labels=['Thick', 'Thin'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_scattered_compact = visual.RatingScale(win=win, name='listening_scattered_compact', marker='triangle', size=0.7, pos=[0.7, -0.5], low=1, high=7, labels=['Scattered', 'Compact'], scale='Extr.  Mod.  Sli. Neutral  Sli.  Mod.  Extr')
listening_text1 = visual.TextStim(win=win, name='listening_text1',
    text="Press 'space' to continue",
    font='Arial',
    pos=(0.81, -0.91), height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-14.0);
listening_text2 = visual.TextStim(win=win, name='listening_text2',
    text=u"Press 'p' to play stimulus again",
    font=u'Arial',
    pos=(-0.71, -0.91), height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-16.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_thanks = visual.TextStim(win=win, name='text_thanks',
    text='Thanks, done!\n\nAny questions can be sent to ieys [at] ime . usp . br and the instructor will reply ASAP.\nThank you very much for participating.\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "presentation"-------
t = 0
presentationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
presentationComponents = [presentation_text, presentation_text2, key_resp_4, presentation_image, presentation_image2]
for thisComponent in presentationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "presentation"-------
while continueRoutine:
    # get current time
    t = presentationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *presentation_text* updates
    if t >= 0.0 and presentation_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        presentation_text.tStart = t
        presentation_text.frameNStart = frameN  # exact frame index
        presentation_text.setAutoDraw(True)
    
    # *presentation_text2* updates
    if t >= 0.0 and presentation_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        presentation_text2.tStart = t
        presentation_text2.frameNStart = frameN  # exact frame index
        presentation_text2.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *presentation_image* updates
    if t >= 0.0 and presentation_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        presentation_image.tStart = t
        presentation_image.frameNStart = frameN  # exact frame index
        presentation_image.setAutoDraw(True)
    
    # *presentation_image2* updates
    if t >= 0.0 and presentation_image2.status == NOT_STARTED:
        # keep track of start time/frame for later
        presentation_image2.tStart = t
        presentation_image2.frameNStart = frameN  # exact frame index
        presentation_image2.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in presentationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "presentation"-------
for thisComponent in presentationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "presentation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions1"-------
t = 0
instructions1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
instructions1Components = [text_instructions11, text_instructions_12, text_instructions_13, text_instructions_14, key_resp_2]
for thisComponent in instructions1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions1"-------
while continueRoutine:
    # get current time
    t = instructions1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions11* updates
    if t >= 0.0 and text_instructions11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions11.tStart = t
        text_instructions11.frameNStart = frameN  # exact frame index
        text_instructions11.setAutoDraw(True)
    
    # *text_instructions_12* updates
    if t >= 0.0 and text_instructions_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions_12.tStart = t
        text_instructions_12.frameNStart = frameN  # exact frame index
        text_instructions_12.setAutoDraw(True)
    
    # *text_instructions_13* updates
    if t >= 0.0 and text_instructions_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions_13.tStart = t
        text_instructions_13.frameNStart = frameN  # exact frame index
        text_instructions_13.setAutoDraw(True)
    
    # *text_instructions_14* updates
    if t >= 0.0 and text_instructions_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions_14.tStart = t
        text_instructions_14.frameNStart = frameN  # exact frame index
        text_instructions_14.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions1"-------
for thisComponent in instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions2"-------
t = 0
instructions2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating.reset()
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
instructions2Components = [text_instructions21, text_instructions22, text_instructions23, rating, text_instructions24, key_resp_5]
for thisComponent in instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions2"-------
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions21* updates
    if t >= 0.0 and text_instructions21.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions21.tStart = t
        text_instructions21.frameNStart = frameN  # exact frame index
        text_instructions21.setAutoDraw(True)
    
    # *text_instructions22* updates
    if t >= 0.0 and text_instructions22.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions22.tStart = t
        text_instructions22.frameNStart = frameN  # exact frame index
        text_instructions22.setAutoDraw(True)
    
    # *text_instructions23* updates
    if t >= 0.0 and text_instructions23.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions23.tStart = t
        text_instructions23.frameNStart = frameN  # exact frame index
        text_instructions23.setAutoDraw(True)
    # *rating* updates
    if t >= 0.0 and rating.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating.tStart = t
        rating.frameNStart = frameN  # exact frame index
        rating.setAutoDraw(True)
    
    # *text_instructions24* updates
    if t >= 0.0 and text_instructions24.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions24.tStart = t
        text_instructions24.frameNStart = frameN  # exact frame index
        text_instructions24.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions3"-------
t = 0
instructions3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()
# keep track of which components have finished
instructions3Components = [text_instructions32, text_instructions33, text_instructions34, key_resp_6, text_instructions31, text_instructions35]
for thisComponent in instructions3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions3"-------
while continueRoutine:
    # get current time
    t = instructions3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions32* updates
    if t >= 0.0 and text_instructions32.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions32.tStart = t
        text_instructions32.frameNStart = frameN  # exact frame index
        text_instructions32.setAutoDraw(True)
    
    # *text_instructions33* updates
    if t >= 0.0 and text_instructions33.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions33.tStart = t
        text_instructions33.frameNStart = frameN  # exact frame index
        text_instructions33.setAutoDraw(True)
    
    # *text_instructions34* updates
    if t >= 0.0 and text_instructions34.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions34.tStart = t
        text_instructions34.frameNStart = frameN  # exact frame index
        text_instructions34.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['y'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *text_instructions31* updates
    if t >= 0.0 and text_instructions31.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions31.tStart = t
        text_instructions31.frameNStart = frameN  # exact frame index
        text_instructions31.setAutoDraw(True)
    
    # *text_instructions35* updates
    if t >= 0.0 and text_instructions35.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions35.tStart = t
        text_instructions35.frameNStart = frameN  # exact frame index
        text_instructions35.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions3"-------
for thisComponent in instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "exposure"-------
t = 0
exposureClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_2.reset()
rating_3.reset()
rating_4.reset()
rating_5.reset()
rating_6.reset()
rating_7.reset()
rating_8.reset()
rating_9.reset()
rating_10.reset()
rating_11.reset()
rating_12.reset()
rating_13.reset()
rating_14.reset()
key_resp_7 = event.BuilderKeyResponse()
p_sound = sound.Sound(u'/home/ieysimurra/Documents/psychopy_backup/pilot/sounds/exposure.wav', secs=5.0) 
# keep track of which components have finished
exposureComponents = [exposure_sound, exposure_text, rating_2, rating_3, rating_4, rating_5, rating_6, rating_7, rating_8, rating_9, rating_10, rating_11, rating_12, rating_13, rating_14, exposure_text2, key_resp_7, exposure_text3]
for thisComponent in exposureComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "exposure"-------
while continueRoutine:
    # get current time
    t = exposureClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop exposure_sound
    if t >= 0.0 and exposure_sound.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_sound.tStart = t
        exposure_sound.frameNStart = frameN  # exact frame index
        exposure_sound.play()  # start the sound (it finishes automatically)
    
    # *exposure_text* updates
    if t >= 0.0 and exposure_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_text.tStart = t
        exposure_text.frameNStart = frameN  # exact frame index
        exposure_text.setAutoDraw(True)
    # *rating_2* updates
    if t >= 0.0 and rating_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_2.tStart = t
        rating_2.frameNStart = frameN  # exact frame index
        rating_2.setAutoDraw(True)
    # *rating_3* updates
    if t >= 0.0 and rating_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_3.tStart = t
        rating_3.frameNStart = frameN  # exact frame index
        rating_3.setAutoDraw(True)
    # *rating_4* updates
    if t >= 0.0 and rating_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_4.tStart = t
        rating_4.frameNStart = frameN  # exact frame index
        rating_4.setAutoDraw(True)
    # *rating_5* updates
    if t >= 0.0 and rating_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_5.tStart = t
        rating_5.frameNStart = frameN  # exact frame index
        rating_5.setAutoDraw(True)
    # *rating_6* updates
    if t >= 0.0 and rating_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_6.tStart = t
        rating_6.frameNStart = frameN  # exact frame index
        rating_6.setAutoDraw(True)
    # *rating_7* updates
    if t >= 0.0 and rating_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_7.tStart = t
        rating_7.frameNStart = frameN  # exact frame index
        rating_7.setAutoDraw(True)
    # *rating_8* updates
    if t >= 0.0 and rating_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_8.tStart = t
        rating_8.frameNStart = frameN  # exact frame index
        rating_8.setAutoDraw(True)
    # *rating_9* updates
    if t >= 0.0 and rating_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_9.tStart = t
        rating_9.frameNStart = frameN  # exact frame index
        rating_9.setAutoDraw(True)
    # *rating_10* updates
    if t >= 0.0 and rating_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_10.tStart = t
        rating_10.frameNStart = frameN  # exact frame index
        rating_10.setAutoDraw(True)
    # *rating_11* updates
    if t >= 0.0 and rating_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_11.tStart = t
        rating_11.frameNStart = frameN  # exact frame index
        rating_11.setAutoDraw(True)
    # *rating_12* updates
    if t >= 0.0 and rating_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_12.tStart = t
        rating_12.frameNStart = frameN  # exact frame index
        rating_12.setAutoDraw(True)
    # *rating_13* updates
    if t >= 0.0 and rating_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_13.tStart = t
        rating_13.frameNStart = frameN  # exact frame index
        rating_13.setAutoDraw(True)
    # *rating_14* updates
    if t >= 0.0 and rating_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_14.tStart = t
        rating_14.frameNStart = frameN  # exact frame index
        rating_14.setAutoDraw(True)
    
    # *exposure_text2* updates
    if t >= 0.0 and exposure_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_text2.tStart = t
        exposure_text2.frameNStart = frameN  # exact frame index
        exposure_text2.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    response = event.getKeys(keyList=['p'])
    if 'p' in response:
        p_sound.play()
    
    # *exposure_text3* updates
    if t >= 0.0 and exposure_text3.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_text3.tStart = t
        exposure_text3.frameNStart = frameN  # exact frame index
        exposure_text3.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exposureComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exposure"-------
for thisComponent in exposureComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
exposure_sound.stop()  # ensure sound has stopped at end of routine

# the Routine "exposure" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ready"-------
t = 0
readyClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
readyComponents = [text_ready1, key_resp_8]
for thisComponent in readyComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ready"-------
while continueRoutine:
    # get current time
    t = readyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_ready1* updates
    if t >= 0.0 and text_ready1.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_ready1.tStart = t
        text_ready1.frameNStart = frameN  # exact frame index
        text_ready1.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ready"-------
for thisComponent in readyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ready" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
listening_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('sounds2.csv'),
    seed=None, name='listening_trials')
thisExp.addLoop(listening_trials)  # add the loop to the experiment
thisListening_trial = listening_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisListening_trial.rgb)
if thisListening_trial != None:
    for paramName in thisListening_trial.keys():
        exec(paramName + '= thisListening_trial.' + paramName)

for thisListening_trial in listening_trials:
    currentLoop = listening_trials
    # abbreviate parameter names if possible (e.g. rgb = thisListening_trial.rgb)
    if thisListening_trial != None:
        for paramName in thisListening_trial.keys():
            exec(paramName + '= thisListening_trial.' + paramName)
    
    # ------Prepare to start Routine "listening_exp"-------
    t = 0
    listening_expClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    listening_sound.setSound(sounds2, secs=-1)
    listening_hard_soft.reset()
    listening_colorless_Colorful.reset()
    listening_dull_dharp.reset()
    listening_heavy_lightweight.reset()
    listening_complex_simple.reset()
    listening_cold_warm.reset()
    listening_dim_bright.reset()
    listening_mixed_pure.reset()
    listening_strong_weak.reset()
    listening_full_empty.reset()
    listening_rough_smooth.reset()
    listening_thick_thin.reset()
    listening_scattered_compact.reset()
    key_resp_9 = event.BuilderKeyResponse()
    # keep track of which components have finished
    listening_expComponents = [listening_sound, listening_hard_soft, listening_colorless_Colorful, listening_dull_dharp, listening_heavy_lightweight, listening_complex_simple, listening_cold_warm, listening_dim_bright, listening_mixed_pure, listening_strong_weak, listening_full_empty, listening_rough_smooth, listening_thick_thin, listening_scattered_compact, listening_text1, key_resp_9, listening_text2]
    for thisComponent in listening_expComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "listening_exp"-------
    while continueRoutine:
        # get current time
        t = listening_expClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop listening_sound
        if t >= 0.0 and listening_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_sound.tStart = t
            listening_sound.frameNStart = frameN  # exact frame index
            listening_sound.play()  # start the sound (it finishes automatically)
        if event.getKeys(keyList=["p"]): 
            listening_sound.play() 
        # *listening_hard_soft* updates
        if t >= 0.0 and listening_hard_soft.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_hard_soft.tStart = t
            listening_hard_soft.frameNStart = frameN  # exact frame index
            listening_hard_soft.setAutoDraw(True)
        # *listening_colorless_Colorful* updates
        if t >= 0.0 and listening_colorless_Colorful.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_colorless_Colorful.tStart = t
            listening_colorless_Colorful.frameNStart = frameN  # exact frame index
            listening_colorless_Colorful.setAutoDraw(True)
        # *listening_dull_dharp* updates
        if t >= 0.0 and listening_dull_dharp.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_dull_dharp.tStart = t
            listening_dull_dharp.frameNStart = frameN  # exact frame index
            listening_dull_dharp.setAutoDraw(True)
        # *listening_heavy_lightweight* updates
        if t >= 0.0 and listening_heavy_lightweight.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_heavy_lightweight.tStart = t
            listening_heavy_lightweight.frameNStart = frameN  # exact frame index
            listening_heavy_lightweight.setAutoDraw(True)
        # *listening_complex_simple* updates
        if t >= 0.0 and listening_complex_simple.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_complex_simple.tStart = t
            listening_complex_simple.frameNStart = frameN  # exact frame index
            listening_complex_simple.setAutoDraw(True)
        # *listening_cold_warm* updates
        if t >= 0.0 and listening_cold_warm.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_cold_warm.tStart = t
            listening_cold_warm.frameNStart = frameN  # exact frame index
            listening_cold_warm.setAutoDraw(True)
        # *listening_dim_bright* updates
        if t >= 0.0 and listening_dim_bright.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_dim_bright.tStart = t
            listening_dim_bright.frameNStart = frameN  # exact frame index
            listening_dim_bright.setAutoDraw(True)
        # *listening_mixed_pure* updates
        if t >= 0.0 and listening_mixed_pure.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_mixed_pure.tStart = t
            listening_mixed_pure.frameNStart = frameN  # exact frame index
            listening_mixed_pure.setAutoDraw(True)
        # *listening_strong_weak* updates
        if t >= 0.0 and listening_strong_weak.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_strong_weak.tStart = t
            listening_strong_weak.frameNStart = frameN  # exact frame index
            listening_strong_weak.setAutoDraw(True)
        # *listening_full_empty* updates
        if t >= 0.0 and listening_full_empty.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_full_empty.tStart = t
            listening_full_empty.frameNStart = frameN  # exact frame index
            listening_full_empty.setAutoDraw(True)
        # *listening_rough_smooth* updates
        if t >= 0.0 and listening_rough_smooth.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_rough_smooth.tStart = t
            listening_rough_smooth.frameNStart = frameN  # exact frame index
            listening_rough_smooth.setAutoDraw(True)
        # *listening_thick_thin* updates
        if t >= 0.0 and listening_thick_thin.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_thick_thin.tStart = t
            listening_thick_thin.frameNStart = frameN  # exact frame index
            listening_thick_thin.setAutoDraw(True)
        # *listening_scattered_compact* updates
        if t >= 0.0 and listening_scattered_compact.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_scattered_compact.tStart = t
            listening_scattered_compact.frameNStart = frameN  # exact frame index
            listening_scattered_compact.setAutoDraw(True)
        
        # *listening_text1* updates
        if t >= 0.0 and listening_text1.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_text1.tStart = t
            listening_text1.frameNStart = frameN  # exact frame index
            listening_text1.setAutoDraw(True)
        
        # *key_resp_9* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *listening_text2* updates
        if t >= 0.0 and listening_text2.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_text2.tStart = t
            listening_text2.frameNStart = frameN  # exact frame index
            listening_text2.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in listening_expComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "listening_exp"-------
    for thisComponent in listening_expComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    listening_sound.stop()  # ensure sound has stopped at end of routine
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_hard_soft.response', listening_hard_soft.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_colorless_Colorful.response', listening_colorless_Colorful.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_dull_dharp.response', listening_dull_dharp.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_heavy_lightweight.response', listening_heavy_lightweight.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_complex_simple.response', listening_complex_simple.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_cold_warm.response', listening_cold_warm.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_dim_bright.response', listening_dim_bright.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_mixed_pure.response', listening_mixed_pure.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_strong_weak.response', listening_strong_weak.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_full_empty.response', listening_full_empty.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_rough_smooth.response', listening_rough_smooth.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_thick_thin.response', listening_thick_thin.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_scattered_compact.response', listening_scattered_compact.getRating())
    # the Routine "listening_exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'listening_trials'

# get names of stimulus parameters
if listening_trials.trialList in ([], [None], None):
    params = []
else:
    params = listening_trials.trialList[0].keys()
# save data for this loop
listening_trials.saveAsExcel(filename + '.xlsx', sheetName='listening_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text_thanks]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_thanks* updates
    if t >= 0.0 and text_thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_thanks.tStart = t
        text_thanks.frameNStart = frameN  # exact frame index
        text_thanks.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_thanks.status == STARTED and t >= frameRemains:
        text_thanks.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
