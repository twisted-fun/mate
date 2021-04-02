from mate import MateModule, command, add_plugins
import datetime


class MateShowPlugins(MateModule):
    @command()
    def show_plugins(self):
        """List loaded plugins."""
        return "Executing Show Plugins."


@command(option="time")
def show_time(self):
    return str(datetime.datetime.now())


add_plugins(modules=[MateShowPlugins("plugins"), show_time], parent="show")
