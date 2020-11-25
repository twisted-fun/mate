from docstring_parser import parse
from mate.modules.core import MateModule
from mate.utils.colors import magenta
from mate.utils.exceptions import MateUndefined
from mate.config import mate_config


def help_default(*args):
    """Print list of commands.
    """
    if len(args) == 0:
        module = mate_config.module_record
    else:
        module = mate_config.module_record.get_module_by_path(args)
        # check if it's in default inline submodules
        if (
            module is None and args[0] in mate_config.module_record.INLINE_SUBMODULES
        ):
            module = mate_config.module_record
        if module is None:
            raise MateUndefined
        else:
            pass
    module_path = module.get_path()
    print()
    # print description of inline submodules
    for m in module.INLINE_SUBMODULES:
        doc = parse(module.INLINE_SUBMODULES[m].__doc__)
        desc = doc.short_description or "No description provided."
        cmd_path = " ".join(module_path + [m]).strip()
        print(magenta(cmd_path) + " -- " + desc)
    # print description of submodules
    for m in module.get_modules():
        doc = parse(m.INLINE_SUBMODULES[""].__doc__)
        desc = doc.short_description or "No description provided."
        cmd_path = " ".join(m.get_path()).strip()
        print(magenta(cmd_path) + " -- " + desc)
    print()


class MateHelp(MateModule):

    INLINE_SUBMODULES = {
        "": help_default,
    }
