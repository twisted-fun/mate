from mate.modules.core import MateModule, command


class MateShowPlugins(MateModule):
    @command()
    def show_plugins(self):
        """List loaded plugins."""
        print("Executing Show Plugins.")
