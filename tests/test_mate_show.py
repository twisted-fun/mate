# pylint: disable=unused-variable
from mate.modules.internal import mate_show
from mate.config import mate_config
from mate.__version__ import __author__, __version__
import datetime


def test_show_inline_submodule_mate_with_no_arguments_should_print_mate_version_and_author():
    out = mate_config.module_record.parse_command(["show", "mate"], shouldPrint=False)
    assert out == {"Version": __version__, "Author": __author__}


# def test_show_inline_submodule_mate_with_invalid_argument_should_print_error_in_correct_format(
#     capfd,
# ):
#     mate_config.module_record.parse_command(["show", "mate", "YOYO"])
#     out, err = capfd.readouterr()
#     assert out == 'Undefined show mate command: "YOYO". Try "help show mate".\n'


def test_show_submodule_plugins_with_no_arguments_should_print_dummy_message():
    out = mate_config.module_record.parse_command(
        ["show", "plugins"], shouldPrint=False
    )
    assert out == "No plugin found."


# def test_show_submodule_plugins_with_invalid_argument_should_print_error_in_correct_format(
#     capsys,
# ):
#     mate_config.module_record.parse_command(["show", "plugins", "YOYO"])
#     out, err = capsys.readouterr()
#     assert out == 'Undefined show plugins command: "YOYO". Try "help show plugins".\n'


def test_show_inline_submodule_context_with_no_arguments():
    out = mate_config.module_record.parse_command(
        ["show", "context"], shouldPrint=False
    )
    assert out == {
        "Project Directory": str(mate_config.project_dir),
        "Output Directory": str(mate_config.output_dir),
    }


def test_show_inline_submodule_time_with_no_arguments():
    out = mate_config.module_record.parse_command(["show", "time"], shouldPrint=False)
    assert str(datetime.datetime.now()).split(" ")[0] in out
