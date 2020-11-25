from mate.modules.core import MateModule


def show_plugins():
    """List loaded plugins.
    """
    print("Executing Show Plugins.")


class MateShowPlugins(MateModule):

    INLINE_SUBMODULES = {
        "": show_plugins,
    }
