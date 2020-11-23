import sys
from mate.modules.core import MateModule
from mate.utils.colors import red, yellow, cyan, magenta, green
from mate.utils.exceptions import mate_exception_handler, MateUndefined
from mate.config import mate_config

def show_context():
    print()
    print(magenta("Project Directory: ") + str(mate_config.project_dir))
    print(magenta("Output Directory: ") + str(mate_config.output_dir))
    print()

def show_mate():
    print()
    print(magenta("Version: ") + str(mate_config.mate_version))
    print(magenta("Author: ") + str(mate_config.mate_author))
    print()

def show_all():
    print()
    print(magenta("Version: ") + str(mate_config.mate_version))
    print(magenta("Author: ") + str(mate_config.mate_author))
    print(magenta("Project Directory: ") + str(mate_config.project_dir))
    print(magenta("Output Directory: ") + str(mate_config.output_dir))
    print()

class MateShow(MateModule):

    DESCRIPTION = {
        "show": "Generic command for showing things about mate.",
    }

    INLINE_SUBMODULES = {
        "": show_mate,
        "all": show_all,
        "mate": show_mate,
        "context": show_context,
    }
