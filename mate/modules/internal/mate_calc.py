from mate.modules.core import MateModule, command


class MateCalc(MateModule):
    @command()
    def calc_default(self):
        """Powerful calculator inspired by IDA Pro calculator."""
        return "Executing Calc."
