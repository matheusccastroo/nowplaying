#!/usr/local/bin/python3
#coding: utf-8
import rumps, selectPlayer

class statusBar(rumps.App):
    def __init__(self):
        super(statusBar, self).__init__("Now Playing")
        self.menu = ["Inform player"]
        rumps.debug_mode(True)
        self.player = ""
        self.tuple = ""

    @rumps.clicked("Inform player")
    def informPlayer(self, _):
            playerName = rumps.Window(title='Inform player', message='Write the name of your desired player and the index to the opened audio file. Note: the player name you type need to be equal to the process name')
            window = playerName.run()
            if window.clicked:
                self.player = window.text.split(",")[0]
                self.tuple = int(window.text.split(",")[1])
                return

    @rumps.timer(1)
    def getMusic(self, _ ):
        if self.player == '':
            return
        else:
            objPlayer = selectPlayer.Player(self.player, self.tuple)
            song = objPlayer.getSong()
            self.title = song

if __name__ == '__main__':
    statusBar().run()