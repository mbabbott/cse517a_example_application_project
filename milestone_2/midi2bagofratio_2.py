# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 22:10:24 2018

@author: Carter
"""

import mido
import numpy as np
import os

def analyzeMidi(midiPath):
    
    mid = mido.MidiFile(midiPath)
   
    
    bagOfNotes = np.zeros(12)
    totalNoteCount = 0
    
    for i, track in enumerate(mid.tracks):
        #print('Track {}: {}'.format(i, track.name))
        for msg in track:
            try:
                message = str(msg)
                if (message[:7] == "note_on"):
                    #print(message)
                    
                    noteValIndex = message.find("note=")+5
                    if (noteValIndex >= 5):     
                        totalNoteCount = totalNoteCount+1
                        rawnoteval = int(message[noteValIndex:noteValIndex+2])
                        modnoteval = rawnoteval%12
                        
                        bagOfNotes[modnoteval] = bagOfNotes[modnoteval] +1
                        totalNoteCount = totalNoteCount+1
                    
                    else:
                        print("ERROR: note not properly read")
            except AttributeError:
                print('UnknownMetaMessage excepted')            
    ratioBag = bagOfNotes/totalNoteCount
    return ratioBag


#shape = (13, 34) #Dmidi

key = 1; #change this to use the other dataset

#directory = 'C:\\Users\\Carter\\Documents\\School\\Machine Learning\\Project\\AllMIDI\\'  
if key == 1:
    directory = 'C:\\Users\\Carter\\Documents\\School\\Machine Learning\\Project\\Part2GP\\midi_new\\Gmidi\\'
else:
    directory = 'C:\\Users\\Carter\\Documents\\School\\Machine Learning\\Project\\Part2GP\\midi_new\\Dmidi\\'  

midiCount = 0
for filename in os.listdir(directory):
    if filename.endswith(".mid") or filename.endswith(".MID"):
        midiCount = midiCount+1

shape = (13, midiCount)
dataset = np.zeros(shape)
midiCount = 0

for filename in os.listdir(directory):
    if filename.endswith(".mid") or filename.endswith(".MID"):
        #print(os.path.join(directory, filename))
        path = directory + filename
        print("Analyzing:", filename, "file#", midiCount)
        
        #filenameInt = re.sub('[^0-9]','', filename)
        try:
            dataset[:12, midiCount] = analyzeMidi(directory+filename)
        
            #dataset[12, midiCount] = filenameInt #for any key
            
            if key == 1:
                dataset[12, midiCount] = 1 #for G major
            else:
                dataset[12, midiCount] = 0 #for D major
            
        except IndexError:
            print('piece not analyzed, index error encountered')
            
        midiCount = midiCount+1     
        
        continue
    else:
        print(filename, "is not a midi file!")
        continue
    
#np.savetxt('bachDataset.csv', dataset, delimiter=",")
if key == 1:
    np.savetxt('gKeyData.csv', dataset, delimiter=",")
else:
    np.savetxt('dKeyData.csv', dataset, delimiter=",")
