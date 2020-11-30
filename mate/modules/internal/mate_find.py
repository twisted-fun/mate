from mate.modules.core import MateModule, command


class MateFind(MateModule):
    @command()
    def find_default(self):
        """Generic command to find various artifacts."""
        return "Executing Find."
