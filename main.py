import random
from getpass import getpass
import atexit
from time import sleep

from skpy import Skype, SkypeAuthException

from SwSpotify import spotify, SpotifyNotRunning


def get_random_smiley():
    smileys = ["(dotdmale)", "(headphones)", "(malthe)", "(stormtrooper)", "(steveaoki)"]
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
    else:
        return title + " from " + artist


if __name__ == '__main__':
    while True:
        login_skype().setMood(get_random_smiley() + " " + get_spotify_mood())
        sleep(60)


def exit_handler():
    print("goodbye")
    try:
        login_skype().setMood(" ")
    except Exception as e:
        print(e)


atexit.register(exit_handler)
