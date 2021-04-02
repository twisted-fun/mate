from mate import MateModule, command, add_plugins


class MateCalc(MateModule):
    @command()
    def calc_default(self):
        """Powerful calculator inspired by IDA Pro calculator."""
        return "Executing Calc."


add_plugins(modules=[MateCalc("calc")])
