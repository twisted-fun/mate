import sys
from mate.modules.core import MateModule
from mate.utils.exceptions import mate_exception_handler

class MateFind(MateModule):
    @mate_exception_handler
    def execute(self):
        print("Executing Find.")