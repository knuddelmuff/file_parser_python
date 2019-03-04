import platform
import os

def openFolder():
    # Check what operating system (OS) the user is using
    if platform.system() == "Darwin": #Mac OSX
        os.system("open .")
    elif platform.system() == "Windows":
        os.system("start .")