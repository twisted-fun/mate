import sys
import os
import re
import shlex
import pluggy
import argparse

from mate.config import config_init
config_init()
from mate.config import mate_config

from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style

from mate.libs import mate_lib, mate_hookspecs
from mate.utils.colors import red, yellow, cyan, magenta, green
from mate.modules.core import MateRecord

import mate.modules
from mate.__version__ import __version__

def get_plugin_manager():
    pm = pluggy.PluginManager("mate")
    pm.add_hookspecs(mate_hookspecs)
    pm.load_setuptools_entrypoints("mate")
    pm.register(mate_lib)
    return pm

def print_banner():
    print(green("mate " + __version__))
    print('For help, type "help".')

def prompt_style():
    if mate_config.prompt_status == "+":
        status_color = "#00aa00"
    elif mate_config.prompt_status == "-":
        status_color = "#aa0000"
    style = Style.from_dict({
        # User input (default text).
        '':          '#ffffff',
        # Prompt.
        'execname': 'ansicyan',
        'bracket': '#ffffff',
        'status': status_color,
        'arrow': 'ansicyan',
    })
    return style


def prompt_message():
    message = [
        ('class:execname', 'mate'),
        ('class:bracket', ' ['),
        ('class:status', mate_config.prompt_status),
        ('class:bracket', '] '),
        ('class:arrow', '> '),
    ]

    return message

def set_prompt_status(status):
    mate_config.prompt_status = status

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
    # command line arg parsing
    args = parse_args(sys.argv[1:])
    if args.project_dir:
        mate_config.project_dir = args.project_dir
    if args.output_dir:
        mate_config.output_dir = args.output_dir
    if args.socket:
        mate_config.socket = args.socket
    
    # a nice banner
    print_banner()

    # initializing plugin manager and mate modules
    print("Loading modules... ", end="")
    pm = get_plugin_manager()
    record = MateRecord(pm.hook)
    record.add_modules()
    mate_config.module_record = record
    print("Done.")

    # setting up interpreter prompt
    history_file = mate_config.mate_hist
    session = PromptSession(
            history=FileHistory(history_file),
            style=None,
            wrap_lines=True,
    )

    try:
        while True:
            prompt = session.prompt(
                prompt_message(),
                style=prompt_style(),
            )
            command = prompt.strip()
            # passing cmd string tokens for parsing
            command_status = record.parse_command(shlex.split(command))
            if command_status:
                set_prompt_status("+")
            else:
                set_prompt_status("-")

    except KeyboardInterrupt:
        print(yellow("\n( ╥﹏╥) ノシ  ") + red("bye...\n"))
        sys.exit()