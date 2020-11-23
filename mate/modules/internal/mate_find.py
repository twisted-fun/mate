import sys
from mate.modules.core import MateModule
from mate.utils.exceptions import mate_exception_handler

def find_default():
    """Generic command to find various artifacts.
    """
    print("Executing Find.")

class MateFind(MateModule):

    INLINE_SUBMODULES = {
        "": find_default,
    }