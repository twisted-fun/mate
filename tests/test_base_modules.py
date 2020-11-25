# pylint: disable=unused-variable
from pathlib import Path
from mate.config import mate_config


def test_base_module_pwd_with_no_arguments_should_print_cwd(capfd):
    mate_config.module_record.parse_command(["pwd"])
    out, err = capfd.readouterr()
    assert out == "Working directory: " + str(Path.cwd()) + "\n"


def test_base_module_pwd_with_invalid_argument_should_print_error_in_correct_format(capfd):
    mate_config.module_record.parse_command(["pwd", "YOYO"])
    out, err = capfd.readouterr()
    assert out == 'Undefined command: "YOYO". Try "help".\n'
