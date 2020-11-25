# pylint: disable=unused-variable
from mate.modules.internal import mate_show
from mate.config import mate_config
from mate.__version__ import __author__, __version__


def test_show_inline_submodule_mate_with_no_arguments_should_print_mate_version_and_author(capfd):
    mate_show.show_mate()
    out, err = capfd.readouterr()
    assert out == "\nVersion: " + __version__ + "\n" + "Author: " + __author__ + "\n\n"


def test_show_inline_submodule_mate_with_invalid_argument_should_print_error_in_correct_format(capfd):
    mate_config.module_record.parse_command(["show", "mate", "YOYO"])
    out, err = capfd.readouterr()
    assert out == 'Undefined show command: "YOYO". Try "help show".\n'


def test_show_submodule_plugins_with_no_arguments_should_print_dummy_message(capfd):
    mate_config.module_record.parse_command(["show", "plugins"])
    out, err = capfd.readouterr()
    assert out == "Executing Show Plugins.\n"


def test_show_submodule_plugins_with_invalid_argument_should_print_error_in_correct_format(capfd):
    mate_config.module_record.parse_command(["show", "plugins", "YOYO"])
    out, err = capfd.readouterr()
    assert out == 'Undefined show plugins command: "YOYO". Try "help show plugins".\n'
