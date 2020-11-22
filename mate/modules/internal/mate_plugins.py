import sys
from mate.modules.core import MateModule
from mate.utils.exceptions import mate_exception_handler

class MateShowPlugins(MateModule):

    DESCRIPTION = {
        "show plugins": "List loaded plugins."
    }

    @mate_exception_handler
    def execute(self):
        print("Executing Show Plugin.")