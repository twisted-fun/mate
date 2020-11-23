import sys
from mate.modules.core import MateModule
from mate.utils.colors import red, yellow, cyan, magenta, green
from mate.utils.exceptions import mate_exception_handler, MateUndefined
from mate.config import mate_config

def show_context():
    """Shows current running context.
    """
    print()
    print(magenta("Project Directory: ") + str(mate_config.project_dir))
    print(magenta("Output Directory: ") + str(mate_config.output_dir))
    print()

def show_mate():
    """Shows mate's details.
    """
    print()
    print(magenta("Version: ") + str(mate_config.mate_version))
    print(magenta("Author: ") + str(mate_config.mate_author))
    print()

def show_all():
    """Shows everything.
    """
    print()
    print(magenta("Version: ") + str(mate_config.mate_version))
    print(magenta("Author: ") + str(mate_config.mate_author))
    print(magenta("Project Directory: ") + str(mate_config.project_dir))
    print(magenta("Output Directory: ") + str(mate_config.output_dir))
    print()

def show_default():
    """Generic command for showing things about mate.
    """
    print("Executing Show.")

class MateShow(MateModule):

    INLINE_SUBMODULES = {
        "": show_default,
        "all": show_all,
        "mate": show_mate,
        "context": show_context,
    }
