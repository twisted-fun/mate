import sys
from mate.modules.core import MateModule
from mate.utils.colors import red, yellow, cyan, magenta, green
from mate.utils.exceptions import mate_exception_handler, MateUndefined
from mate.config import mate_config

def show_context():
    print(magenta("Project Directory: ") + str(mate_config.project_dir))
    print(magenta("Output Directory: ") + str(mate_config.output_dir))

def show_mate():
    print(magenta("Version: ") + str(mate_config.mate_version))
    print(magenta("Author: ") + str(mate_config.mate_author))

def show_all():
    show_mate()
    show_context()

class MateShow(MateModule):

    DESCRIPTION = {
        "show": "Generic command for showing things about mate.",
    }

    @mate_exception_handler
    def execute(self, entity="all"):
        if entity == "all":
            show_all()
        elif entity == "context":
            show_context()
        elif entity == "mate":
            show_mate()
        else:
            raise MateUndefined
