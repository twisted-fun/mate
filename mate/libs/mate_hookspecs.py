import pluggy

hookspec = pluggy.HookspecMarker("mate")

@hookspec
def mate_add_modules():
    """[summary]
    """
