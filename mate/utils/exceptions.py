import sys
import functools
from mate.utils.colors import red

def mate_exception_handler(func):
    @functools.wraps(func)
    def tmp_func(self, *args, **kwargs):
        try:
            retval = func(self, *args, **kwargs)
            if retval is not False:
                return True
        except TypeError:
            original_command = " ".join(self.get_path())
            extra_command = " ".join(list(args))
            print(red("Undefined {} command: \"{}\". Try \"help {}\".".format(original_command, extra_command, original_command)))
            return False
    return tmp_func

class MateUndefined(TypeError):
    pass