from getpass import getpass
from getpass import getuser
from time import sleep

from skpy import Skype, SkypeAuthException

from SwSpotify import spotify


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
        return spotify.song() + " from " + spotify.artist()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:
        sk = login_skype().setMood("(headphones) " + get_spotify_mood())
        sleep(60)
