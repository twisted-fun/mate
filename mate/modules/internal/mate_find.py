from mate.modules.core import MateModule


def find_default():
    """Generic command to find various artifacts."""
    print("Executing Find.")


class MateFind(MateModule):

    INLINE_SUBMODULES = {
        "": find_default,
    }
