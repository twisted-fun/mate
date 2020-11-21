import sys
import re
import subprocess
from mate.modules.internal.colors import red, yellow, cyan, magenta, green

def show_help():
    print("I am here to help!")

def parse_command(command):
    tokens = command.split()
    # no op
    if len(tokens) == 0:
        pass
    # check if command is meant to redirected to shell
    elif tokens[0] == "!":
        print(subprocess.getoutput(re.sub(r"^\!", "", command)))
    # check if command is actually a comment
    elif tokens[0] == "#":
        print(cyan(command))
    # Give me colors in my life
    elif tokens[0] == "ls":
        print(subprocess.getoutput(command + " --color"))
    elif tokens[0] == "pwd":
        print("Working directory " + green(subprocess.getoutput("pwd") + "."))
    # check if help is needed
    elif tokens[0] == "help" or tokens[0] == "h":
        show_help()
    else:
        print(red("Undefined command: \"" + command + "\". Try \"help\"."))