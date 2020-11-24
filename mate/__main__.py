import sys
import os
import re
import shlex
import pluggy
import logging
import argparse

from mate.config import config_init
config_init()
from mate.config import mate_config

from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter

from mate.libs import mate_lib, mate_hookspecs
from mate.utils.logger import log, shellLogHandler
from mate.utils.colors import red, yellow, cyan, magenta, green
from mate.modules.core import MateRecord

import mate.modules
from mate.__version__ import __version__

def get_plugin_manager():
    """Initializes plugin manager and registers plugin library.

    Returns:
        pm: plugin manager
    """
    pm = pluggy.PluginManager("mate")
    pm.add_hookspecs(mate_hookspecs)
    pm.load_setuptools_entrypoints("mate")
    pm.register(mate_lib)
    return pm

def print_banner():
    """Prints mate's banner i.e. version info.
    """
    print(green("mate " + __version__))
    print('For help, type "help".')

def prompt_style():
    """Specifies the colors of different block/classes in mate's prompt

    Returns:
        style: Style object is parsed by prompt toolkit to make prompt fancy.
    """
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
    """Creates mate's prompt design.

    Returns:
        message: Message object is parsed by prompt toolkit to create prompt.
    """
    message = [
        ('class:execname', 'mate'),
        ('class:bracket', ' ['),
        ('class:status', mate_config.prompt_status),
        ('class:bracket', '] '),
        ('class:arrow', '> '),
    ]

    return message

def set_prompt_status(status):
    """Sets state (+/-) into mate's prompt,
    which reflects whether last command was executed successfully or not

    Args:
        status ([type]): [description]
    """
    mate_config.prompt_status = status

def parse_args(args):
    """Parse command line arguments of mate.

    Args:
        args (list): List of arguments (except sys.argv[0]) passed to mate.

    Returns:
        parsed_args: Collection of arguments parsed by argparse.
    """
    parse = argparse.ArgumentParser()
    parse.add_argument(
        "-V", "--version", action="version", version="%(prog)s " + __version__ 
    )
    parse.add_argument(
        "--debug", dest="debug", default=False, action="store_true", help="Set console log level to DEBUG."
    )
    parse.add_argument(
        "-p", "--project-dir", dest="project_dir", help="Specify root directory of a project for analysis."
    )
    parse.add_argument(
        "-o", "--output-dir", dest="output_dir", help="Specify root directory to store various result files."
    )
    parse.add_argument(
        "-s", "--socket", dest="socket", help="Provide [Protocol]Host[:Port] of a service for analysis."
    )
    return parse.parse_args(args)

def main():
    """I do the actual work.
    """
    # command line arg parsing
    args = parse_args(sys.argv[1:])
    if args.debug:
        shellLogHandler.setLevel(logging.DEBUG)
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
    record = MateRecord("mate", pm.hook)
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

    auto_completer = WordCompleter([
        'help',
        'find',
        'calc',
        'show',
    ])

    log.debug("- Starting shell.")

    try:
        while True:
            prompt = session.prompt(
                prompt_message(),
                style=prompt_style(),
                completer=auto_completer,
                complete_while_typing=True
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
    except:
        log.error("Wait! What happened now...", exc_info=True)