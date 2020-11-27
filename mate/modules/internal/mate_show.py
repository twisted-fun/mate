from mate.modules.core import MateModule, command
from mate.utils.colors import magenta
from mate.config import mate_config


class MateShow(MateModule):
    @command()
    def show_default(self):
        """Generic command for showing things about mate."""
        print("Executing Show.")

    @command(option="all")
    def show_all(self):
        """Shows everything."""
        print()
        print(magenta("Version: ") + str(mate_config.mate_version))
        print(magenta("Author: ") + str(mate_config.mate_author))
        print(magenta("Project Directory: ") + str(mate_config.project_dir))
        print(magenta("Output Directory: ") + str(mate_config.output_dir))
        print()

    @command(option="mate")
    def show_mate(self):
        """Shows mate's details."""
        print()
        print(magenta("Version: ") + str(mate_config.mate_version))
        print(magenta("Author: ") + str(mate_config.mate_author))
        print()

    @command(option="context")
    def show_context(self):
        """Shows current running context."""
        print()
        print(magenta("Project Directory: ") + str(mate_config.project_dir))
        print(magenta("Output Directory: ") + str(mate_config.output_dir))
        print()
