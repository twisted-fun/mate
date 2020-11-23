import sys
from mate.modules.core import MateModule
from mate.utils.exceptions import mate_exception_handler

def show_plugins():
    """List loaded plugins.
    """
    print("Executing Show Plugins.")

class MateShowPlugins(MateModule):

    INLINE_SUBMODULES = {
        "": show_plugins,
    }