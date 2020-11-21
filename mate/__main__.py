import sys
import os
import argparse

from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style

from mate.modules.internal.colors import red, yellow, cyan, magenta, green

from mate.commands import parse_command

from mate.__version__ import __version__
from mate.config import MateConfig

config = MateConfig()

def print_banner():
    print(green("mate " + __version__))
    print('For help, type "help".')

def prompt_style():
    style = Style.from_dict({
        # User input (default text).
        '':          '#ffffff',
        # Prompt.
        'execname': 'ansicyan',
        'bracket': '#ffffff',
        'status': '#00aa00',
        'arrow': 'ansicyan',
    })
    return style


def prompt_message():
    message = [
        ('class:execname', 'mate'),
        ('class:bracket',       ' ['),
        ('class:status',     '+'),
        ('class:bracket',    '] '),
        ('class:arrow',     '> '),
    ]

    return message

def parse_args(args):
    parse = argparse.ArgumentParser()
    parse.add_argument(
        "-V", "--version", action="version", version="%(prog)s " + __version__ 
    )
    parse.add_argument(
        "-p", "--project-dir", dest="project_dir", help="Specify root directory of a project for analysis"
    )
    parse.add_argument(
        "-o", "--output-dir", dest="output_dir", help="Specify root directory to store various result files"
    )
    parse.add_argument(
        "-s", "--socket", dest="socket", help="Provide [Protocol]Host[:Port] of a service for analysis"
    )
    return parse.parse_args(args)

def main():
    args = parse_args(sys.argv[1:])

    if args.project_dir:
        config.project_dir = args.project_dir
    if args.output_dir:
        config.output_dir = args.output_dir
    if args.socket:
        config.socket = args.socket
    
    history_file = config.mate_hist
    session = PromptSession(
            history=FileHistory(history_file),
            style=None,
            wrap_lines=True,
    )

    print_banner()
    try:
        while True:
            prompt = session.prompt(
                prompt_message(),
                style=prompt_style(),
            )
            command = prompt.strip()
            parse_command(command)

    except KeyboardInterrupt:
        print(yellow("\n( ╥﹏╥) ノシ  ") + red("bye...\n"))
        sys.exit()