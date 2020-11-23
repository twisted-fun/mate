import sys
from mate.modules.core import MateModule
from mate.utils.exceptions import mate_exception_handler

def find_default():
    print("Executing Find.")

class MateFind(MateModule):

    DESCRIPTION = {
        "find": "Generic command to find various artifacts."
    }

    INLINE_SUBMODULES = {
        "": find_default,
    }