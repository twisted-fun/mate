import sys
import argparse
from mate.__version__ import __version__

def parse_args(args):
    parse = argparse.ArgumentParser()
    parse.add_argument(
        "-V", "--version", action="version", version="%(prog)s " + __version__ 
    )
    return parse.parse_args(args)

def main():
    args = parse_args(sys.argv[1:])
    print("hello mate")