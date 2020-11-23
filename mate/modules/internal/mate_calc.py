import sys
from mate.modules.core import MateModule
from mate.utils.exceptions import mate_exception_handler

def calc_default():
    print("Executing Calc.")

class MateCalc(MateModule):

    DESCRIPTION = {
        "calc": "Powerful calculator inspired by IDA Pro calculator."
    }

    INLINE_SUBMODULES = {
        "": calc_default,
    }