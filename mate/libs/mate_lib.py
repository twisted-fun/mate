from mate.modules import hookimpl
from mate.modules.internal.mate_calc import MateCalc
from mate.modules.internal.mate_find import MateFind
from mate.modules.internal.mate_help import MateHelp
from mate.modules.internal.mate_show import MateShow
from mate.modules.internal.mate_plugins import MateShowPlugins


@hookimpl
def mate_add_modules():
    """Responsible to collect all modules and plugins.

    Returns:
        list: Contains MateModules to be added in MateRecord.
    """
    modules = []
    # Adding help
    modules.append(MateHelp("help"))
    # Adding show
    show = MateShow("show")
    modules.append(show)
    # Adding show plugins
    show_plugins = MateShowPlugins("plugins")
    show.add_submodule(show_plugins)
    # Adding find
    modules.append(MateFind("find"))
    # Adding calc
    modules.append(MateCalc("calc"))
    return modules
