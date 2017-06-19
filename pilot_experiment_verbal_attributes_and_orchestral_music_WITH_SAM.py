"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on Thu 01 Jun 2017 09:00:50 PM BRT
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
_thisDir = os.path.dirname(os.path.abspath("__file__")).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Data Window Experiment-SAM'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'age': u'', u'session': u'001', u'participant': u'', u'pro_experience': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName, 
    tip={'gender': 'please, put M for Male or F for Female','age':'Please, fill it with your age in years', 'participant':'Please, if you feel confortable fill it with your initials',
        'pro_experience':'Please, fill it with your years in music professional experience'})
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
    size=(1350, 700), fullscr=True, screen=0,
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
    text='Pilot Experiment\n\nOn Verbal Attributes Classification \n\nOf \n\nOrchestral Timbres',
    font='Neuropolitical',
    pos=(0, -0.05), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
#presentation_text2 = visual.TextStim(win=win, name='presentation_text2',
#    text="Press 'space' to continue",
#    font='Times New Roman',
#    pos=(0.81, -0.83), height=0.05, wrapWidth=None, ori=0, 
#    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
#    depth=-1.0);
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
presentation_continue = visual.ImageStim(
    win=win, name='presentation_continue',
    image=u'continue3.png', mask=None,
    ori=0, pos=(0.85, -0.83), size=(0.19, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
presentation_mouse = event.Mouse(win=win)
x, y = [None, None]

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
#text_instructions_14 = visual.TextStim(win=win, name='text_instructions_14',
#    text="Press 'space' to continue",
#    font='Times New Roman',
#    pos=(0.81, -0.83), height=0.05, wrapWidth=None, ori=0, 
#    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
#    depth=-3.0);
instructions1_continue = visual.ImageStim(
    win=win, name='instructions1_continue',
    image=u'continue3.png', mask=None,
    ori=0, pos=(0.85, -0.83), size=(0.19, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
instructions1_mouse = event.Mouse(win=win)
x, y = [None, None]

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
text_instructions21 = visual.TextStim(win=win, name='text_instructions21',
    text='Specific Instructions\n\nIn this survey:\n\n-> You will be presented to 33 musical audio-examples of 5 seconds duration each\n\n-> You will rate them by a set of several 5-points scales on verbal attributes and both by arousal and valence emotional states\n(e.g.: from low to high)\n',
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
    text="-> Please, after selecting your choice press the 'accept?' button to confirm your alternative.",
    font='Arial',
    pos=(-0.01, -0.37), height=0.059, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
rating = visual.RatingScale(win=win, name='rating', marker='circle', size=0.9, pos=[0.0, -0.7], low=1, high=5, labels=[''], scale='Attribute')
#text_instructions24 = visual.TextStim(win=win, name='text_instructions24',
#    text="Press 'space' to continue",
#    font='Times New Roman',
#    pos=(0.81, -0.83), height=0.05, wrapWidth=None, ori=0, 
#    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
#    depth=-4.0);
instructions2_continue = visual.ImageStim(
    win=win, name='instructions2_continue',
    image='continue3.png', mask=None,
    ori=0, pos=(0.85, -0.83), size=(0.19, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
instructions2_mouse = event.Mouse(win=win)
x, y = [None, None]

# Initialize components for Routine "instructions3"
instructions3Clock = core.Clock()
text_instructions32 = visual.TextStim(win=win, name='text_instructions32',
    text='Please make sure to carefully listen to the audio excerpts in full duration\n\nYou will first start with a training example which should allow you to familiarise yourself with the type of stimuli in the experiment.\nPlease, adjust audio intensity on training session and try to not change it during experiment.',
    font='Arial',
    pos=(0, -0.05), height=0.059, wrapWidth=None, ori=0, 
    color=[0.004,-1.000,0.004], colorSpace='rgb', opacity=1,
    depth=0.0);
text_instructions33 = visual.TextStim(win=win, name='text_instructions33',
    text='Good quality headphones or external speakers and a quiet environment are required as the survey involves listening to sound clips.',
    font='Arial',
    pos=(0.02, -0.35), height=0.059, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_instructions34 = visual.TextStim(win=win, name='text_instructions34',
    text="To begin the experiment, please press the 'Yes' button. By pressing this button, you confirm that you have read and understood the experiment instructions and give your consent for your rating data to be anonymously analysed when reporting experimental results.\n\nThe data gathered from this survey will only be used as research purpose\nPlease from now on place your headphones comfortably.",
    font='Arial',
    pos=(0, -0.71), height=0.059, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-2.0);
text_instructions31 = visual.TextStim(win=win, name='text_instructions31',
    text="These are the scales that are going to be used to evaluate the sound stimuli\n\n                                                    * Density\n                                                    * Texture\n                                                    * Brightness\n                                                    * Arousal\n                                                    * Valence\n\nPlease make sure to carefully listen to the audio excerpts in full duration\n\nYou will first start with a training example which should allow you to familiarise yourself with the type of stimuli in the experiment.\n\nTo begin the experiment, please press the 'y' key. By pressing this key, you confirm that you have read and understood the experiment instructions and give your consent for your rating data to be anonymously analysed when reporting experimental results.\n\nThe data gathered from this survey will only be used as research purpose\n\n\n\n\n\n\n",
    font='Arial',
    pos=(0, 0.0), height=0.047, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
#text_instructions35 = visual.TextStim(win=win, name='text_instructions35',
#    text="Prees 'y' to continue",
#    font='Times New Roman',
#    pos=(0.81, -0.83), height=0.05, wrapWidth=None, ori=0, 
#    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
#    depth=-2.0);
instructions3_continue = visual.ImageStim(
    win=win, name='instructions3_continue',
    image='yes.png', mask=None,
    ori=0, pos=(0.85, -0.83), size=(0.19, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
instructions3_mouse = event.Mouse(win=win)
x, y = [None, None]

# Initialize components for Routine "exposure"
exposureClock = core.Clock()
exposure_sound = sound.Sound('/home/ieysimurra/Documents/psychopy_backup/pilot/sounds/exposure.wav', secs=-1)
exposure_sound.setVolume(1)
exposure_text = visual.TextStim(win=win, name='exposure_text',
    text='Training Step',
    font='Arial',
    pos=(0.85, 0.95), height=0.071, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=1.25, pos=[-0.5, 0.7], low=1, high=5, labels=['Low', ' High'], scale='Density',showValue=False,acceptPreText='Do not Forget me')
rating_3 = visual.RatingScale(win=win, name='rating_3', marker='triangle', size=1.25, pos=[-0.5, 0.08], low=1, high=5, labels=['Low', 'High'], scale='Texture',showValue=False,acceptPreText='Do not Forget me')
rating_4 = visual.RatingScale(win=win, name='rating_4', marker='triangle', size=1.25, pos=[-0.5, -0.55], low=1, high=7, labels=['Low', 'High'], scale='Brightness',showValue=False,acceptPreText='Do not Forget me')
#exposure_text2 = visual.TextStim(win=win, name='exposure_text2',
#    text="Press 'space' to continue",
#    font='Arial',
#    pos=(0.85, -0.95), height=0.035, wrapWidth=None, ori=0, 
#    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
#    depth=-5.0);

#exposure_text3 = visual.TextStim(win=win, name='exposure_text3',
#    text="Press 'p' to play stimulus again",
#    font='Arial',
#    pos=(-0.85, -0.95), height=0.035, wrapWidth=None, ori=0, 
#    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
#    depth=-8.0);
exposure_exp_arousal5 = visual.ImageStim(
    win=win, name='exposure_exp_arousal5',
    image='arousal-5.png', mask=None,
    ori=0, pos=(0.88, 0.50), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
exposure_exp_arousal4 = visual.ImageStim(
    win=win, name='exposure_exp_arousal4',
    image='arousal-4.png', mask=None,
    ori=0, pos=(0.69, 0.50), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
exposure_exp_arousal3 = visual.ImageStim(
    win=win, name='exposure_exp_arousal3',
    image='arousal-3.png', mask=None,
    ori=0, pos=(0.50, 0.50), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
exposure_exp_arousal2 = visual.ImageStim(
    win=win, name='exposure_exp_arousal2',
    image='arousal-2.png', mask=None,
    ori=0, pos=(0.31,0.50), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
exposure_exp_arousal1 = visual.ImageStim(
    win=win, name='exposure_exp_arousal1',
    image='arousal-1.png', mask=None,
    ori=0, pos=(0.12, 0.50), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
rating_5 = visual.RatingScale(win=win, name='rating_5', marker='triangle', size=1.25, pos=[0.5, 0.35], low=1, high=5, labels=['Deactive', 'Active'], scale='',showValue=False,acceptPreText='Do not Forget me')
exposure_exp_valence5 = visual.ImageStim(
    win=win, name='exposure_exp_valence5',
    image='valence-5.png', mask=None,
    ori=0, pos=(0.88, -0.35), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
exposure_exp_valence4 = visual.ImageStim(
    win=win, name='exposure_exp_valence4',
    image='valence-4.png', mask=None,
    ori=0, pos=(0.69, -0.35), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
exposure_exp_valence3 = visual.ImageStim(
    win=win, name='exposure_exp_valence3',
    image='valence-3.png', mask=None,
    ori=0, pos=(0.50, -0.35), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
exposure_exp_valence2 = visual.ImageStim(
    win=win, name='exposure_exp_valence2',
    image='valence-2.png', mask=None,
    ori=0, pos=(0.31, -0.35), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
exposure_exp_valence1 = visual.ImageStim(
    win=win, name='exposure_exp_valence1',
    image='valence-1.png', mask=None,
    ori=0, pos=(0.12, -0.35), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
rating_6 = visual.RatingScale(win=win, name='rating_6', marker='triangle', size=1.25, pos=[0.5, -0.5], low=1, high=5, labels=['Sad', 'Cheerful'], scale='',showValue=False,acceptPreText='Do not Forget me')

exposure_continue = visual.ImageStim(
    win=win, name='exposure_continue',
    image=u'continue3.png', mask=None,
    ori=0, pos=(0.85, -0.83), size=(0.19, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
exposure_mouse = event.Mouse(win=win)
x, y = [None, None]

play_again_exposure = visual.ImageStim(
    win=win, name='play_again_exposure',
    image=u'play_again.png', mask=None,
    ori=0, pos=(-0.85, -0.83), size=(0.19, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)

# Initialize components for Routine "ready"
readyClock = core.Clock()
text_ready1 = visual.TextStim(win=win, name='text_ready1',
    text="READY?\n\n(please, click on 'Continue' Button to start experiment)\n\n\nBe Prepared and Remember: \nAudio Stimulus will be played immediately in next",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0);

ready_continue = visual.ImageStim(
    win=win, name='ready_continue',
    image=u'continue3.png', mask=None,
    ori=0, pos=(0.85, -0.83), size=(0.19, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
ready_mouse = event.Mouse(win=win)
x, y = [None, None]

# Initialize components for Routine "listening_exp"
listening_expClock = core.Clock()
listening_sound = sound.Sound('A', secs=-1)
listening_sound.setVolume(1)
listening_density = visual.RatingScale(win=win, name='listening_density', marker='triangle', size=1.25, pos=[-0.5, 0.7], low=1, high=5, labels=['Low', 'High'], scale='Density',showValue=False,acceptPreText='Do not Forget me')
listening_texture = visual.RatingScale(win=win, name='listening_texture', marker='triangle', size=1.25, pos=[-0.5, 0.08], low=1, high=5, labels=['Low', 'High'], scale='Texture',showValue=False,acceptPreText='Do not Forget me')
listening_brightness = visual.RatingScale(win=win, name='listening_brightness', marker='triangle', size=1.25, pos=[-0.5, -0.55], low=1, high=5, labels=['Low', 'High'], scale='Brightness',showValue=False,acceptPreText='Do not Forget me')
#listening_text1 = visual.TextStim(win=win, name='listening_text1',
#    text="Press 'space' to continue",
#    font='Arial',
#    pos=(0.85, -0.95), height=0.035, wrapWidth=None, ori=0, 
#    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
#    depth=-4.0);
#listening_text2 = visual.TextStim(win=win, name='listening_text2',
#    text="Press 'p' to play stimulus again",
#    font='Arial',
#    pos=(-0.85, -0.95), height=0.035, wrapWidth=None, ori=0, 
#    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
#    depth=-6.0);

listening_arousal5 = visual.ImageStim(
    win=win, name='listening_arousal5',
    image='arousal-5.png', mask=None,
    ori=0, pos=(0.88, 0.50), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
listening_arousal4 = visual.ImageStim(
    win=win, name='listening_arousal4',
    image='arousal-4.png', mask=None,
    ori=0, pos=(0.69, 0.50), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
listening_arousal3 = visual.ImageStim(
    win=win, name='listening_arousal3',
    image='arousal-3.png', mask=None,
    ori=0, pos=(0.50, 0.50), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
listening_arousal2 = visual.ImageStim(
    win=win, name='listening_arousal2',
    image='arousal-2.png', mask=None,
    ori=0, pos=(0.31,0.50), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
listening_arousal1 = visual.ImageStim(
    win=win, name='listening_arousal1',
    image='arousal-1.png', mask=None,
    ori=0, pos=(0.12, 0.50), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
rating_arousal = visual.RatingScale(win=win, name='rating_arousal', marker='triangle', size=1.25, pos=[0.5, 0.35], low=1, high=5, labels=['Deactive', 'Active'], scale='',showValue=False,acceptPreText='Do not Forget me')
listening_valence5 = visual.ImageStim(
    win=win, name='listening_valence5',
    image='valence-5.png', mask=None,
    ori=0, pos=(0.88, -0.35), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
listening_valence4 = visual.ImageStim(
    win=win, name='listening_valence4',
    image='valence-4.png', mask=None,
    ori=0, pos=(0.69, -0.35), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
listening_valence3 = visual.ImageStim(
    win=win, name='listening_valence3',
    image='valence-3.png', mask=None,
    ori=0, pos=(0.50, -0.35), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
listening_valence2 = visual.ImageStim(
    win=win, name='listening_valence2',
    image='valence-2.png', mask=None,
    ori=0, pos=(0.31, -0.35), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
listening_valence1 = visual.ImageStim(
    win=win, name='listening_valence1',
    image='valence-1.png', mask=None,
    ori=0, pos=(0.12, -0.35), size=(0.2, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
rating_valence = visual.RatingScale(win=win, name='rating_valence', marker='triangle', size=1.25, pos=[0.5, -0.5], low=1, high=5, labels=['Sad', 'Cheerful'], scale='',showValue=False,acceptPreText='Do not Forget me')

listening_count = visual.TextStim(win=win, name='listening_count',
    text='default text',
    font=u'Arial',
    pos=(0.91, 0.91), height=0.075, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-14.0);
                                  
listening_continue = visual.ImageStim(
    win=win, name='listening_continue',
    image=u'continue3.png', mask=None,
    ori=0, pos=(0.83, -0.85), size=(0.19, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
listening_mouse = event.Mouse(win=win)
x, y = [None, None]

listening_play_again_continue = visual.ImageStim(
    win=win, name='listening_play_again_continue',
    image=u'play_again.png', mask=None,
    ori=0, pos=(-0.83, -0.85), size=(0.19, 0.15),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_thanks = visual.TextStim(win=win, name='text_thanks',
    text='Thanks, done!\n\nAny questions can be sent to ieys [at] ime . usp . br\n\nwe will reply ASAP.\nThank you very much for participating.\n\n',
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
presentationComponents = [presentation_text, presentation_image, presentation_image2, presentation_continue, presentation_mouse]
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
#    if t >= 0.0 and presentation_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
#        presentation_text2.tStart = t
#        presentation_text2.frameNStart = frameN  # exact frame index
#        presentation_text2.setAutoDraw(True)
    
    # *key_resp_4* updates
#    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
#        key_resp_4.tStart = t
#        key_resp_4.frameNStart = frameN  # exact frame index
#        key_resp_4.status = STARTED
        # keyboard checking is just starting
#        event.clearEvents(eventType='keyboard')
#    if key_resp_4.status == STARTED:
#        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
#        if "escape" in theseKeys:
#            endExpNow = True
#        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
#            continueRoutine = False
    
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
        
    # *presentation_continue* updates
    if t >= 0.0 and presentation_continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        presentation_continue.tStart = t
        presentation_continue.frameNStart = frameN  # exact frame index
        presentation_continue.setAutoDraw(True)
    if presentation_mouse.isPressedIn(presentation_continue):
        continueRoutine = False
    
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
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
while any(presentation_mouse.getPressed()):
    pass                                  
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
instructions1Components = [text_instructions11, text_instructions_12, text_instructions_13, instructions1_continue, instructions1_mouse]
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
#    if t >= 0.0 and text_instructions_14.status == NOT_STARTED:
        # keep track of start time/frame for later
#        text_instructions_14.tStart = t
#        text_instructions_14.frameNStart = frameN  # exact frame index
#        text_instructions_14.setAutoDraw(True)
    
    # *key_resp_2* updates
#    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
#        key_resp_2.tStart = t
#        key_resp_2.frameNStart = frameN  # exact frame index
#        key_resp_2.status = STARTED
        # keyboard checking is just starting
#        event.clearEvents(eventType='keyboard')
#    if key_resp_2.status == STARTED:
#        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
#        if "escape" in theseKeys:
#            endExpNow = True
#        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
#            continueRoutine = False
    
    # *instructions1_continue* updates
    if t >= 0.0 and instructions1_continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions1_continue.tStart = t
        instructions1_continue.frameNStart = frameN  # exact frame index
        instructions1_continue.setAutoDraw(True)
    if instructions1_mouse.isPressedIn(instructions1_continue):
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
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
while any(instructions1_mouse.getPressed()):
    pass                                  
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
instructions2Components = [text_instructions21, text_instructions22, text_instructions23, rating, instructions2_continue, instructions2_mouse]
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
 #   if t >= 0.0 and text_instructions24.status == NOT_STARTED:
        # keep track of start time/frame for later
 #       text_instructions24.tStart = t
 #       text_instructions24.frameNStart = frameN  # exact frame index
 #       text_instructions24.setAutoDraw(True)
    
    # *key_resp_5* updates
 #   if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
 #       key_resp_5.tStart = t
 #       key_resp_5.frameNStart = frameN  # exact frame index
 #       key_resp_5.status = STARTED
        # keyboard checking is just starting
 #       event.clearEvents(eventType='keyboard')
 #   if key_resp_5.status == STARTED:
 #       theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
 #       if "escape" in theseKeys:
 #           endExpNow = True
 #       if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
 #           continueRoutine = False

    # *instructions2_continue* updates
    if t >= 0.0 and instructions2_continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions2_continue.tStart = t
        instructions2_continue.frameNStart = frameN  # exact frame index
        instructions2_continue.setAutoDraw(True)
    if instructions2_mouse.isPressedIn(instructions2_continue):
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
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
while any(instructions2_mouse.getPressed()):
    pass                                  
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
instructions3Components = [text_instructions32, text_instructions33, text_instructions34, text_instructions31, instructions3_continue, instructions3_mouse]
for thisComponent in instructions3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions3"-------
while continueRoutine:
    # get current time
    t = instructions3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
#    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
#        key_resp_6.tStart = t
#        key_resp_6.frameNStart = frameN  # exact frame index
#        key_resp_6.status = STARTED
        # keyboard checking is just starting
#        event.clearEvents(eventType='keyboard')
#    if key_resp_6.status == STARTED:
#        theseKeys = event.getKeys(keyList=['y'])
        
        # check for quit:
#        if "escape" in theseKeys:
#            endExpNow = True
#        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
#            continueRoutine = False
    
    # *text_instructions31* updates
    if t >= 0.0 and text_instructions31.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions31.tStart = t
        text_instructions31.frameNStart = frameN  # exact frame index
        text_instructions31.setAutoDraw(True)
    
    # *text_instructions35* updates
#    if t >= 0.0 and text_instructions35.status == NOT_STARTED:
        # keep track of start time/frame for later
#        text_instructions35.tStart = t
#        text_instructions35.frameNStart = frameN  # exact frame index
#        text_instructions35.setAutoDraw(True)

    # *instructions3_continue* updates
    if t >= 0.0 and instructions3_continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions3_continue.tStart = t
        instructions3_continue.frameNStart = frameN  # exact frame index
        instructions3_continue.setAutoDraw(True)
    if instructions3_mouse.isPressedIn(instructions3_continue):
        continueRoutine = False

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
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
while any(instructions3_mouse.getPressed()):
    pass                                  
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
key_resp_7 = event.BuilderKeyResponse()
p_sound = sound.Sound(u'/home/ieysimurra/Documents/psychopy_backup/pilot/sounds/exposure.wav', secs=5.0) 
rating_5.reset()
rating_6.reset()
# keep track of which components have finished
exposureComponents = [exposure_sound, exposure_text, rating_2, rating_3, rating_4, key_resp_7, exposure_exp_arousal5, exposure_exp_arousal4, exposure_exp_arousal3, exposure_exp_arousal2, exposure_exp_arousal1, rating_5, exposure_exp_valence5, exposure_exp_valence4, exposure_exp_valence3, exposure_exp_valence2, exposure_exp_valence1, rating_6, exposure_continue, exposure_mouse, play_again_exposure]
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
    
    # *exposure_text2* updates
#    if t >= 0.0 and exposure_text2.status == NOT_STARTED:
        # keep track of start time/frame for later
#        exposure_text2.tStart = t
#        exposure_text2.frameNStart = frameN  # exact frame index
#        exposure_text2.setAutoDraw(True)
    
    # *key_resp_7* updates
#    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
#        key_resp_7.tStart = t
#        key_resp_7.frameNStart = frameN  # exact frame index
#        key_resp_7.status = STARTED
        # keyboard checking is just starting
#        event.clearEvents(eventType='keyboard')
#    if key_resp_7.status == STARTED:
#        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
#        if "escape" in theseKeys:
#            endExpNow = True
#        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
#            continueRoutine = False
#    response = event.getKeys(keyList=['p'])
#    if 'p' in response:
#        p_sound.play()
    
    # *exposure_text3* updates
#    if t >= 0.0 and exposure_text3.status == NOT_STARTED:
        # keep track of start time/frame for later
#        exposure_text3.tStart = t
#        exposure_text3.frameNStart = frameN  # exact frame index
#        exposure_text3.setAutoDraw(True)
    
    # *exposure_exp_arousal5* updates
    if t >= 0.0 and exposure_exp_arousal5.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_exp_arousal5.tStart = t
        exposure_exp_arousal5.frameNStart = frameN  # exact frame index
        exposure_exp_arousal5.setAutoDraw(True)
    
    # *exposure_exp_arousal4* updates
    if t >= 0.0 and exposure_exp_arousal4.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_exp_arousal4.tStart = t
        exposure_exp_arousal4.frameNStart = frameN  # exact frame index
        exposure_exp_arousal4.setAutoDraw(True)
    
    # *exposure_exp_arousal3* updates
    if t >= 0.0 and exposure_exp_arousal3.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_exp_arousal3.tStart = t
        exposure_exp_arousal3.frameNStart = frameN  # exact frame index
        exposure_exp_arousal3.setAutoDraw(True)
    
    # *exposure_exp_arousal2* updates
    if t >= 0.0 and exposure_exp_arousal2.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_exp_arousal2.tStart = t
        exposure_exp_arousal2.frameNStart = frameN  # exact frame index
        exposure_exp_arousal2.setAutoDraw(True)
    
    # *exposure_exp_arousal1* updates
    if t >= 0.0 and exposure_exp_arousal1.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_exp_arousal1.tStart = t
        exposure_exp_arousal1.frameNStart = frameN  # exact frame index
        exposure_exp_arousal1.setAutoDraw(True)
    # *rating_5* updates
    if t >= 0.0 and rating_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_5.tStart = t
        rating_5.frameNStart = frameN  # exact frame index
        rating_5.setAutoDraw(True)
    
    # *exposure_exp_valence5* updates
    if t >= 0.0 and exposure_exp_valence5.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_exp_valence5.tStart = t
        exposure_exp_valence5.frameNStart = frameN  # exact frame index
        exposure_exp_valence5.setAutoDraw(True)
    
    # *exposure_exp_valence4* updates
    if t >= 0.0 and exposure_exp_valence4.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_exp_valence4.tStart = t
        exposure_exp_valence4.frameNStart = frameN  # exact frame index
        exposure_exp_valence4.setAutoDraw(True)
    
    # *exposure_exp_valence3* updates
    if t >= 0.0 and exposure_exp_valence3.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_exp_valence3.tStart = t
        exposure_exp_valence3.frameNStart = frameN  # exact frame index
        exposure_exp_valence3.setAutoDraw(True)
    
    # *exposure_exp_valence2* updates
    if t >= 0.0 and exposure_exp_valence2.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_exp_valence2.tStart = t
        exposure_exp_valence2.frameNStart = frameN  # exact frame index
        exposure_exp_valence2.setAutoDraw(True)
    
    # *exposure_exp_valence1* updates
    if t >= 0.0 and exposure_exp_valence1.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_exp_valence1.tStart = t
        exposure_exp_valence1.frameNStart = frameN  # exact frame index
        exposure_exp_valence1.setAutoDraw(True)
    # *rating_6* updates
    if t >= 0.0 and rating_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_6.tStart = t
        rating_6.frameNStart = frameN  # exact frame index
        rating_6.setAutoDraw(True)
 
    if exposure_mouse.isPressedIn(play_again_exposure):
        p_sound.play()
    
    # *exposure_continue* updates
    if t >= 0.0 and exposure_continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        exposure_continue.tStart = t
        exposure_continue.frameNStart = frameN  # exact frame index
        exposure_continue.setAutoDraw(True)
    if exposure_mouse.isPressedIn(exposure_continue):
        continueRoutine = False
    
    # *play_again_exposure* updates
    if t >= 0.0 and play_again_exposure.status == NOT_STARTED:
        # keep track of start time/frame for later
        play_again_exposure.tStart = t
        play_again_exposure.frameNStart = frameN  # exact frame index
        play_again_exposure.setAutoDraw(True)

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
while any(exposure_mouse.getPressed()):
    pass
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
while any(exposure_mouse.getPressed()):
    pass
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
readyComponents = [text_ready1, key_resp_8,ready_continue, ready_mouse]
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

    # *ready_continue* updates
    if t >= 0.0 and ready_continue.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready_continue.tStart = t
        ready_continue.frameNStart = frameN  # exact frame index
        ready_continue.setAutoDraw(True)
    if ready_mouse.isPressedIn(ready_continue):
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
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
while any(ready_mouse.getPressed()):
    pass                                  
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
    listening_density.reset()
    listening_texture.reset()
    listening_brightness.reset()
    key_resp_9 = event.BuilderKeyResponse()
    listening_count.setText([(listening_trials.thisN+1), 33] )
    rating_arousal.reset()
    rating_valence.reset()
    p_sound = listening_sound.play()
    # keep track of which components have finished
    listening_expComponents = [listening_sound, listening_density, listening_texture, listening_brightness, key_resp_9, listening_arousal5, listening_arousal4, listening_arousal3, listening_arousal2, listening_arousal1, rating_arousal, listening_valence5, listening_valence4, listening_valence3, listening_valence2, listening_valence1, rating_valence, listening_count, listening_continue, listening_mouse, listening_play_again_continue]
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
        # *listening_density* updates
        if t >= 0.0 and listening_density.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_density.tStart = t
            listening_density.frameNStart = frameN  # exact frame index
            listening_density.setAutoDraw(True)
        # *listening_texture* updates
        if t >= 0.0 and listening_texture.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_texture.tStart = t
            listening_texture.frameNStart = frameN  # exact frame index
            listening_texture.setAutoDraw(True)
        # *listening_brightness* updates
        if t >= 0.0 and listening_brightness.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_brightness.tStart = t
            listening_brightness.frameNStart = frameN  # exact frame index
            listening_brightness.setAutoDraw(True)
        
        # *listening_text1* updates
#        if t >= 0.0 and listening_text1.status == NOT_STARTED:
            # keep track of start time/frame for later
#            listening_text1.tStart = t
#            listening_text1.frameNStart = frameN  # exact frame index
#            listening_text1.setAutoDraw(True)
        
        # *key_resp_9* updates
#        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
#            key_resp_9.tStart = t
#            key_resp_9.frameNStart = frameN  # exact frame index
#            key_resp_9.status = STARTED
            # keyboard checking is just starting
#            event.clearEvents(eventType='keyboard')
#        if key_resp_9.status == STARTED:
#            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
#            if "escape" in theseKeys:
#                endExpNow = True
#            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
#                continueRoutine = False
        
        # *listening_text2* updates
#        if t >= 0.0 and listening_text2.status == NOT_STARTED:
            # keep track of start time/frame for later
#            listening_text2.tStart = t
#            listening_text2.frameNStart = frameN  # exact frame index
#            listening_text2.setAutoDraw(True)
#        response = event.getKeys(keyList=['p'])
#        if 'p' in response:
#            p_sound.play()
        
        # *listening_arousal5* updates
        if t >= 0.0 and listening_arousal5.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_arousal5.tStart = t
            listening_arousal5.frameNStart = frameN  # exact frame index
            listening_arousal5.setAutoDraw(True)
        
        # *listening_arousal4* updates
        if t >= 0.0 and listening_arousal4.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_arousal4.tStart = t
            listening_arousal4.frameNStart = frameN  # exact frame index
            listening_arousal4.setAutoDraw(True)
        
        # *listening_arousal3* updates
        if t >= 0.0 and listening_arousal3.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_arousal3.tStart = t
            listening_arousal3.frameNStart = frameN  # exact frame index
            listening_arousal3.setAutoDraw(True)
        
        # *listening_arousal2* updates
        if t >= 0.0 and listening_arousal2.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_arousal2.tStart = t
            listening_arousal2.frameNStart = frameN  # exact frame index
            listening_arousal2.setAutoDraw(True)
        
        # *listening_arousal1* updates
        if t >= 0.0 and listening_arousal1.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_arousal1.tStart = t
            listening_arousal1.frameNStart = frameN  # exact frame index
            listening_arousal1.setAutoDraw(True)
        # *rating_arousal* updates
        if t >= 0.0 and rating_arousal.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_arousal.tStart = t
            rating_arousal.frameNStart = frameN  # exact frame index
            rating_arousal.setAutoDraw(True)
        
        # *listening_valence5* updates
        if t >= 0.0 and listening_valence5.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_valence5.tStart = t
            listening_valence5.frameNStart = frameN  # exact frame index
            listening_valence5.setAutoDraw(True)
        
        # *listening_valence4* updates
        if t >= 0.0 and listening_valence4.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_valence4.tStart = t
            listening_valence4.frameNStart = frameN  # exact frame index
            listening_valence4.setAutoDraw(True)
        
        # *listening_valence3* updates
        if t >= 0.0 and listening_valence3.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_valence3.tStart = t
            listening_valence3.frameNStart = frameN  # exact frame index
            listening_valence3.setAutoDraw(True)
        
        # *listening_valence2* updates
        if t >= 0.0 and listening_valence2.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_valence2.tStart = t
            listening_valence2.frameNStart = frameN  # exact frame index
            listening_valence2.setAutoDraw(True)
        
        # *listening_valence1* updates
        if t >= 0.0 and listening_valence1.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_valence1.tStart = t
            listening_valence1.frameNStart = frameN  # exact frame index
            listening_valence1.setAutoDraw(True)
        # *rating_valence* updates
        if t >= 0.0 and rating_valence.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_valence.tStart = t
            rating_valence.frameNStart = frameN  # exact frame index
            rating_valence.setAutoDraw(True)
        
        # *listening_count* updates
        if t >= 0.0 and listening_count.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_count.tStart = t
            listening_count.frameNStart = frameN  # exact frame index
            listening_count.setAutoDraw(True)
#        if listening_count.status == STARTED:  # only update if drawing
#            listening_count.setText("%i/33" % (listening_trials.thisRepN) , log=False)
        
        # *listening_continue* updates
        if t >= 0.0 and listening_continue.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_continue.tStart = t
            listening_continue.frameNStart = frameN  # exact frame index
            listening_continue.setAutoDraw(True)
        if ready_mouse.isPressedIn(ready_continue):
            continueRoutine = False
        
        # *listening_play_again_continue* updates
        if t >= 0.0 and listening_play_again_continue.status == NOT_STARTED:
            # keep track of start time/frame for later
            listening_play_again_continue.tStart = t
            listening_play_again_continue.frameNStart = frameN  # exact frame index
            listening_play_again_continue.setAutoDraw(True)
        if listening_mouse.isPressedIn(listening_play_again_continue):
            p_sound.play()
        
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
    listening_trials.addData('listening_density.response', listening_density.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_texture.response', listening_texture.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('listening_brightness.response', listening_brightness.getRating())
    
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('rating_arousal.response', rating_arousal.getRating())
    # store data for listening_trials (TrialHandler)
    listening_trials.addData('rating_valence.response', rating_valence.getRating())
    # store data for listening_trials (TrialHandler)
    while any(listening_mouse.getPressed()):
        pass
    while any(listening_mouse.getPressed()):
        pass
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

