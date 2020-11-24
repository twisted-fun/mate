import sys
import functools
from mate.utils.colors import red

def mate_exception_handler(func):
    """Mate's fallback exception handler as a decorator.

    Args:
        func (function): Function on which decorator was specified.

    Returns:
        function: Argument function will be wrapped in a try/except and returned.
    """
    @functools.wraps(func)
    def tmp_func(self, inline_submodule_name, *args):
        try:
            retval = func(self, inline_submodule_name, *args)
            if retval is not False:
                return True
        except TypeError:
            original_command = " ".join(self.get_path())
            extra_command = args[0]
            print(red("Undefined {} command: \"{}\". Try \"help {}\".".format(original_command, extra_command, original_command)))
            return False
    return tmp_func

class MateUndefined(TypeError):
    """Because we don't want to catch all TypeErrors.

    Args:
        TypeError ([type]): [description]
    """
    pass