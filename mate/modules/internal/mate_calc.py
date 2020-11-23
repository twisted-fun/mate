import sys
from mate.modules.core import MateModule
from mate.utils.exceptions import mate_exception_handler

def calc_default():
    """Powerful calculator inspired by IDA Pro calculator.
    """
    print("Executing Calc.")

class MateCalc(MateModule):

    INLINE_SUBMODULES = {
        "": calc_default,
    }