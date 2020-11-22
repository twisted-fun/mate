import sys
import os
import re
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

def parse_command(command_str):
    command_path = "/".join(command_str.split())
    # no op
    if len(command_path) == 0:
        return

    # Get all command dictionary's keys
    # Make a list of them
    # sort the list so that key with maximum length is at first place
    command_keys = list(mate_config.command.keys())
    command_keys.sort(key=len)
    for key in command_keys[::-1]:
        if command_path.startswith(key):
            command_len = len(key.split('/'))
            # remove command length from command string provided to get the args
            args = tuple(command_str.split()[command_len:])
            try:
                mate_config.command[key](*args)
            except TypeError:
                original_command = ' '.join(key.split('/'))
                extra_command = ' '.join(args)
                print(red("Undefined " + original_command + " command: \"" +
                    extra_command + "\". Try \"help " + original_command + "\"."))
            # break after first function call
            break

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
    
    # initializing plugin manager and mate modules
    pm = get_plugin_manager()
    record = MateRecord(pm.hook)
    record.add_modules()
    mate_config.module_record = record
    #print(record.modules)

    # setting up interpreter prompt
    history_file = mate_config.mate_hist
    session = PromptSession(
            history=FileHistory(history_file),
            style=None,
            wrap_lines=True,
    )

    # a nice banner
    print_banner()
    try:
        while True:
            prompt = session.prompt(
                prompt_message(),
                style=prompt_style(),
            )
            command = prompt.strip()
            # passing cmd string tokens for parsing
            record.parse_command(command.split())

    except KeyboardInterrupt:
        print(yellow("\n( ╥﹏╥) ノシ  ") + red("bye...\n"))
        sys.exit()