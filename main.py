import http
import random
from getpass import getpass
import atexit
from time import sleep

import requests
from skpy import Skype, SkypeAuthException

from SwSpotify import spotify, SpotifyNotRunning


def is_internet_connected():
    url = "http://www.google.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("Seems connection has been dropped")
        return False


def get_random_smiley():
    smileys = ["(dotdmale)", "(headphones)", "(malthe)", "(stormtrooper)", "(steveaoki)", "(panda)", "(rockchick)"]
    return random.choice(smileys)


def login_skype():
    try:
        skype = Skype(tokenFile=".tokens-app")
    except SkypeAuthException as e:
        user_name = str(input("Enter a Skype username: "))
        password = getpass("Enter a Skype password: ")
        skype = Skype(user_name, password, ".tokens-app")
    return skype


def get_spotify_mood():
    try:
        title, artist = spotify.current()
    except SpotifyNotRunning as e:
        print(e)
        return " "
    else:
        return title + " from " + artist


if __name__ == '__main__':
    last_track = ""
    while True:
        if last_track != get_spotify_mood():
            last_track = get_spotify_mood()
            if is_internet_connected():
                login_skype().setMood(get_random_smiley() + " " + last_track)
            else:
                last_track = " "
            print(last_track)
        sleep(4)


def exit_handler():
    print("goodbye")
    try:
        login_skype().setMood(" ")
    except Exception as e:
        print(e)


atexit.register(exit_handler)
