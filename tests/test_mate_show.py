# pylint: disable=unused-variable
from mate.modules.internal import mate_show
from mate.config import mate_config
from mate.__version__ import __author__, __version__
import datetime


def test_show_inline_submodule_mate_with_no_arguments_should_print_mate_version_and_author(
    capfd,
):
    mate_config.module_record.parse_command(["show", "mate"])
    out, err = capfd.readouterr()
    assert out == "\nVersion: " + __version__ + "\n" + "Author: " + __author__ + "\n\n"


def test_show_inline_submodule_mate_with_invalid_argument_should_print_error_in_correct_format(
    capfd,
):
    mate_config.module_record.parse_command(["show", "mate", "YOYO"])
    out, err = capfd.readouterr()
    assert out == 'Undefined show mate command: "YOYO". Try "help show mate".\n'


def test_show_submodule_plugins_with_no_arguments_should_print_dummy_message(capfd):
    mate_config.module_record.parse_command(["show", "plugins"])
    out, err = capfd.readouterr()
    assert out == "No plugin found.\n"


def test_show_submodule_plugins_with_invalid_argument_should_print_error_in_correct_format(
    capfd,
):
    mate_config.module_record.parse_command(["show", "plugins", "YOYO"])
    out, err = capfd.readouterr()
    assert out == 'Undefined show plugins command: "YOYO". Try "help show plugins".\n'


def test_show_inline_submodule_context_with_no_arguments(
    capfd,
):
    mate_config.module_record.parse_command(["show", "context"])
    out, err = capfd.readouterr()
    assert (
        out
        == "\nProject Directory: "
        + str(mate_config.project_dir)
        + "\n"
        + "Output Directory: "
        + str(mate_config.output_dir)
        + "\n\n"
    )


def test_show_inline_submodule_time_with_no_arguments(
    capfd,
):
    mate_config.module_record.parse_command(["show", "time"])
    out, err = capfd.readouterr()
    assert str(datetime.datetime.now()).split(" ")[0] in out
