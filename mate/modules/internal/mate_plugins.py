from mate import MateModule, command, add_plugins


class MateShowPlugins(MateModule):
    @command()
    def show_plugins(self):
        """List loaded plugins."""
        return "Executing Show Plugins."


# add_plugins(MateShowPlugins())
