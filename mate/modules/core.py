import sys
import re
import pathlib
import subprocess
import itertools

from mate.utils.colors import red, yellow, cyan, magenta, green
from mate.utils.exceptions import MateUndefined, mate_exception_handler

# TODO: Change classes internal function name to have underscore in the beginning
class MateModule:
    """Base class for all mate's modules.

    Returns:
        MateModuleObject: Returns a module object that is easily pluggable into mate.
    """

    # Dictionary to keep track of inline submodules of a MateModule.
    INLINE_SUBMODULES = {
        #"":node_function # for default action on module
        #"node_name": node_function,
    }

    def __init__(self, module_name):
        """Initializes MateModule object.

        Args:
            module_name (string): Name of MateModule.
        """
        self.submodules = []
        self.module_name = module_name
        self.parent = None
    
    def get_name(self):
        """Get module name.

        Returns:
            string: Module name of current MateModule.
        """
        return self.module_name

    # TODO: Change get_modules to get_submodules
    def get_modules(self):
        """Returns submodules.

        Returns:
            list: Contains submodules of current MateModule.
        """
        return self.submodules
    
    def add_submodule(self, module):
        """Proper way to add submodule to a MateModule.

        Args:
            module (MateModule): Submodule to be added.
        """
        module.parent = self
        self.submodules.append(module)
    
    def get_submodules_names(self):
        """Get names of immediate submodules.

        Returns:
            list: Contains names of immediate submodules.
        """
        if self.submodules != []:
            return [submodule.get_name() for submodule in self.submodules]
        else:
            return []

    def get_path(self):
        """Calculates path of current module.

        Returns:
            list: First element of the list is starting point of path and last element is current module itself.
        """
        path = [self.get_name()]
        tmp_module = self
        while tmp_module.parent is not None:
            tmp_module = tmp_module.parent
            path.append(tmp_module.get_name())
        return path[::-1][1:]

    def get_paths(self):
        """Returns path of itself and paths of its immediate submodules.

        Returns:
            list: Contains paths calculated.
        """
        paths = [self.get_path()]
        for submodule in self.submodules:
            paths.append(submodule.get_path())
        return paths

    def get_all_paths(self):
        """Returns path of itself and paths of all submodules by going recursive.

        Returns:
            list: Contains paths calculated.
        """
        paths = [self.get_path()]
        if self.submodules != []:
            for submodule in self.submodules:
                paths += submodule.get_all_paths()
        return paths

    # TODO: Change this function name to get_submodule_by_name
    def match_submodule(self, module_name):
        """Matches provided module name with it's submodules.

        Args:
            module_name (string): Name of a MateModule that is submodule to current module.

        Returns:
            MateModule: Return the submodule that matches with the name provided.
        """
        if self.submodules != []:
            for module in self.submodules:
                if module.get_name() == module_name:
                    return module
        return None
    
    # TODO: Convert this functionality into get_submodule_by_path
    def match_path(self, path):
        """Matches provided path with submodule's paths and returns most matched submodule's path.

        Args:
            path (list): List of string that is matched against submodule's paths.

        Returns:
            path: Returns most matched submodule's path.
        """
        if self.parent == None:
            ret_path = []
        else:
            ret_path = self.parent.get_path()
        self_path = self.get_path()
        if self_path == path[:len(self_path)]:
            ret_path = self_path
        for module in self.get_modules():
            module_path = module.get_path()
            if module_path == path[:len(module_path)]:
                ret_path = module.match_path(path)
                break
        return ret_path
    
    @mate_exception_handler
    def execute(self, inline_submodule_name, *args):
        """Executor of inline submodules.

        Args:
            inline_submodule_name (string): Name of inline submodule.
            args (tuple): Tuple that contains arguments of inline submodule.
        """
        self.INLINE_SUBMODULES[inline_submodule_name](*args)

def ls_default(*args):
    """Satisfies your command line itch.
    """
    ls_args = " ".join(args)
    print(subprocess.getoutput("ls " + ls_args + " --color"))

def pwd_default(*args):
    """Prints current working directory.
    """
    print(magenta("Working directory: ") + str(pathlib.Path.cwd()))

def sh_default(*args):
    """Interface to shell.
    """
    sh_args = " ".join(args)
    print(subprocess.getoutput(sh_args))

class MateRecord(MateModule):
    """Keep track of all modules in mate.
    """

    # Mate's default inline submodules.
    INLINE_SUBMODULES = {
        "ls": ls_default,
        "pwd": pwd_default,
        "sh": sh_default,
    }

    def __init__(self, module_name, hook):
        """Initializes ModuleRecord and adds a hook for plugin registrations.

        Args:
            module_name (string): Name of ModuleRecord object.
            hook (_HookRelay): Hook that is used for plugin registration.
        """
        self.hook = hook
        # invoke MateModule's init
        super().__init__(module_name)

    def add_modules(self):
        """Loads all modules and plugins dynamically from hook.
        """
        results = self.hook.mate_add_modules()
        all_modules = list(itertools.chain(*results))
        for module in all_modules:
            self.add_submodule(module)

    # TODO: Fix get_module_by_path function. Currently it matches with module_name, not with module's path
    def get_module_by_path(self, path):
        """Returns the submodule with the exact path that is provided.

        Args:
            path (list): List that contains module names in a specific order.

        Returns:
            MateModule: Submodule that matched the path.
        """
        tmp_module = self
        for node in path:
            for module in tmp_module.get_modules():
                if node == module.get_name():
                    tmp_module = module
                    break
        if tmp_module == self:
            return None
        return tmp_module

    def parse_command(self, cmd_tokens):
        """Parse and execute command from command tokens provided.

        Args:
            cmd_tokens (list): Tokenized command string.
        """
        if len(cmd_tokens) == 0:
            return True
        else:
            for module in self.get_modules():
                path = module.match_path(cmd_tokens)
                if path != []:
                    module_to_exec = self.get_module_by_path(path)
                    inline_submodule_name = "".join(cmd_tokens[len(path):len(path)+1])
                    if inline_submodule_name not in module_to_exec.INLINE_SUBMODULES:
                        inline_submodule_name = ""
                        params = tuple(cmd_tokens[len(path):])
                    else:
                        params = tuple(cmd_tokens[len(path)+1:])
                    return module_to_exec.execute(inline_submodule_name, *params)
            
            if cmd_tokens[0] in self.INLINE_SUBMODULES:
                self.INLINE_SUBMODULES[cmd_tokens[0]](*cmd_tokens[1:])
                return True
            invalid_command = cmd_tokens[0]
            print(red("Undefined command: \"{}\". Try \"help\".".format(invalid_command)))
            return False
