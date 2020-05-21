# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:37:24 2019

@author: Administrator
"""

import scipy.io.wavfile
import wave 
import matplotlib.pyplot
import matplotlib.pylab
import urllib.request
import numpy

reponse = urlib.request.urlopen('http://www.nch.com.au/acm/11k16bitpcm.wav')

WAV_FILE = 'english.wav'
file = open(WAV_FILE,'wb+')
file.write(reponse.read())
file.close()

wavefile = wave.open(WAV_FILE,'r')
params = wavefile.getparams()
nchannels,sample_width,framerate,numframes = params[:4]

sample_rate,data = scipy.io.wavfile.read(WAV_FILE)


