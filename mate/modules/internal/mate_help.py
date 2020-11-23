import sys
import shlex
from mate.modules.core import MateModule
from mate.utils.exceptions import mate_exception_handler, MateUndefined
from mate.config import mate_config

def help_default(*args):
    if len(args) == 0:
        mate_config.module_record.print_description()
    else:
        module = mate_config.module_record.get_module_by_path(args)
        if module is None:
            raise MateUndefined
        else:
            module.print_description()

class MateHelp(MateModule):

    DESCRIPTION = {
        "help": "Print list of commands."
    }

    INLINE_SUBMODULES = {
        "": help_default,
    }
    
