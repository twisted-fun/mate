import sys
import functools
from mate.utils.colors import red

def mate_exception_handler(func):
    @functools.wraps(func)
    def tmp_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            original_command = " ".join(args[0].get_path())
            extra_command = " ".join(list(args)[1:])
            print(red("Undefined {} command: \"{}\". Try \"help {}\".".format(original_command, extra_command, original_command)))
    return tmp_func

class MateUndefined(TypeError):
    pass