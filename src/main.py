"""
    Okey.I made a decision to create two classes of finder lyrics.
    The first version if based on lyrics.ovh - it`s cool free and dont require the api key. But it`s hard to find song, cause you need to know the full artist name and song
    The second version based on AZlyrics.
"""

import requests
import json
import sys
import re
import bs4

mail = 'ohv36983@cndps.com'
login = 'farahnasri'
password = 'GuAcy5Lz'
try:
    import colorama
except ImportError:
    print('The colorama is not installed.')
    sys.exit(0)

colorama.init(autoreset=True)

class seekOVH():
    def __init__(self , artist , song):
        self.artist = artist
        self.song = song

    def getLyrics(self):
        URL = 'https://api.lyrics.ovh/v1'
        head = requests.get(URL + '/' + self.artist + '/' + self.song)
        jsonObj = json.loads(head.text)
        return jsonObj

    def printLyrics(self):
        lyrDict = self.getLyrics()
        print('Hi')
        lyrics = lyrDict['lyrics']
        print(colorama.Fore.YELLOW + lyrics)


class seekXMATCH():
    def __init__(self , artist , song):
        self.artist = str(artist)
        self.song = str(song)
        self.url = 'https://www.azlyrics.com/lyrics/'
    def replace(self):
        self.artist = re.sub('[^A-Za-z0-9]+', '' , self.artist)
        self.song = re.sub('[^A-Za-z0-9]+', '' , self.song)
        return self.artist , self.song
        
    def xGetLyrics(self):
        self._data = self.replace()
        print(self._data[0])
        self.reqBody = requests.get(self.url + self._data[0] + '/' + self._data[1] + '.html')
        print(self.url + self._data[0] + '/' + self._data[1] + '.html')
        self.reqContent = bs4.BeautifulSoup(self.reqBody.text , 'html.parser')
        self.textCont = self.reqContent.select('.col-xs-12.col-lg-8.text-center')
        print(str(self.textCont[0].getText()))

if __name__ == "__main__":
    h = seekXMATCH('coldplay' , 'yellow')
    h.xGetLyrics()