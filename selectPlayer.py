#!/usr/local/bin/python3
#coding: utf-8
import os, psutil, subprocess

class Player():
    def __init__(self, name, getToSong):
        self.name = name
        self.getToSong = getToSong

    def checkAndSelectPlayer(self):
        playerName = self.name
        if playerName in (p.name() for p in psutil.process_iter()):
            pidString = subprocess.check_output(["pgrep", playerName])
            pidInt = int(pidString)
            processPlayer = psutil.Process(pidInt)
            return processPlayer
        else:
            print("Couldn't find your player!")
            return

    def nameOnly(self, song):
        if song.endswith('.flac'):  # take out the .flac from the name
            song = song[:-5]
            return song
        elif song.endswith('.mp3'):  # take out the .mp3 from the name
            song = song[:-4]
            return song
        elif song.endswith('.alac'):  # take out the .alac from the name
            song = song[:-5]
            return song
        elif song.endswith('.ape'):
            song = song[:-4]
            return song

    def getSong(self):
        files = self.checkAndSelectPlayer()
        filesOpen = files.open_files()
        musicPath = filesOpen[self.getToSong].path
        song = os.path.basename(musicPath)
        song = self.nameOnly(song)
        return song