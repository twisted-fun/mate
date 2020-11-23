import sys
import re
import subprocess
import itertools

from mate.utils.colors import red, yellow, cyan, magenta, green
from mate.utils.exceptions import MateUndefined, mate_exception_handler


class MateModule:

    # Used by help module
    DESCRIPTION = {}

    def __init__(self, module_name):
        self.submodules = []
        self.module_name = module_name
        self.parent = None
    
    def get_name(self):
        return self.module_name
    
    def print_description(self):
        paths = self.get_paths()
        # remove "mate" from paths to match with description key values
        wanted = []
        for path in paths:
            wanted.append(" ".join(path))
        print()
        for cmd in sorted(self.DESCRIPTION):
            if cmd not in wanted:
                continue
            desc = self.DESCRIPTION[cmd]
            print(magenta(cmd) + " -- " + desc)
        print()

    def get_modules(self):
        """
        Returns:
            [list]: [Returns list of submodule in the module]
        """
        return self.submodules
    
    def add_submodule(self, module):
        module.parent = self
        self.submodules.append(module)
        # append description of submodule in parent
        self.DESCRIPTION = {**self.DESCRIPTION, **module.DESCRIPTION}
    
    def get_submodules_names(self):
        if self.submodules != []:
            return [submodule.get_name() for submodule in self.submodules]
        else:
            return []

    def get_path(self):
        """[Calculates path of current module]

        Returns:
            [list]: [First element of the list is starting point of path and last element is current module itself]
        """
        path = [self.get_name()]
        tmp_module = self
        while tmp_module.parent is not None:
            tmp_module = tmp_module.parent
            path.append(tmp_module.get_name())
        return path[::-1][1:]

    def get_paths(self):
        """Returns path of itself and paths of its immediate submodules
        """
        paths = [self.get_path()]
        for submodule in self.submodules:
            paths.append(submodule.get_path())
        return paths

    def get_all_paths(self):
        paths = [self.get_path()]
        if self.submodules != []:
            for submodule in self.submodules:
                paths += submodule.get_all_paths()
        return paths

    def match_submodule(self, module_name):
        if self.submodules != []:
            for module in self.submodules:
                if module.get_name() == module_name:
                    return module
        return None
    
    def match_path(self, path):
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
                  
    def execute(self):
        pass


class MateRecord(MateModule):

    def __init__(self, module_name, hook):
        self.hook = hook
        # invoke MateModule's init
        super().__init__(module_name)

    def add_modules(self):
        results = self.hook.mate_add_modules()
        all_modules = list(itertools.chain(*results))
        for module in all_modules:
            self.add_submodule(module)
    
    def match_module_by_name(self, module_name):
        if self.submodules != []:
            for module in self.submodules:
                if module.get_name() == module_name:
                    return module
        return None

    def get_module_by_path(self, path):
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
        """[parse and execute command from command tokens provided]

        Args:
            cmd_tokens ([list]): [tokenized command string]
        """
        if len(cmd_tokens) == 0:
            return True
        else:
            for module in self.get_modules():
                path = module.match_path(cmd_tokens)
                if path != []:
                    module_to_exec = self.get_module_by_path(path)
                    params = tuple(cmd_tokens[len(path):])
                    return module_to_exec.execute(*params)
            invalid_command = " ".join(cmd_tokens)
            print(red("Undefined command: \"{}\". Try \"help\".".format(invalid_command)))
            return False
