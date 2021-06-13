# pylint: disable=unused-variable
import pytest
from mate.modules.internal import mate_help
from mate.config import mate_config


@pytest.fixture(scope="module")
def base_module_names():
    record = mate_config.module_record
    base_module_names = (
        list(record.INLINE_SUBMODULES.keys()) + record.get_submodules_names()
    )
    return base_module_names


@pytest.fixture(scope="module")
def show_module_names():
    show = mate_config.module_record.get_module_by_path(["show"])
    show_module_names = (
        list(show.INLINE_SUBMODULES.keys()) + show.get_submodules_names()
    )
    return show_module_names


@pytest.fixture(scope="function")
def cmd_names_in_help_with_no_args():
    out = mate_config.module_record.parse_command(["help"], shouldPrint=False)
    return [line for line in list(out) if line != ""]


@pytest.fixture(scope="function")
def cmd_names_in_help_with_show():
    out = mate_config.module_record.parse_command(["help", "show"], shouldPrint=False)
    return [line for line in list(out) if line != ""]


@pytest.fixture(scope="function")
def cmd_names_in_help_with_show_all():
    out = mate_config.module_record.parse_command(
        ["help", "show", "all"], shouldPrint=False
    )
    return [line for line in list(out) if line != ""]


def test_help_default_with_no_arguments_should_print_only_one_word_commands(
    cmd_names_in_help_with_no_args,
):
    # Asserting that command column values are only one word
    for cmd_column_value in cmd_names_in_help_with_no_args:
        assert " " not in cmd_column_value


def test_help_default_with_no_arguments_should_print_all_base_commands(
    base_module_names, cmd_names_in_help_with_no_args
):
    # Asserting that all modules have been covered by help
    assert sorted(base_module_names) == cmd_names_in_help_with_no_args


def test_help_default_with_more_than_zero_arguments_should_print_only_self_and_all_submodules(
    show_module_names, cmd_names_in_help_with_show
):
    should_be_command_column = [
        "show " + module_name if module_name != "" else "show"
        for module_name in show_module_names
    ]
    assert sorted(should_be_command_column) == cmd_names_in_help_with_show


def test_help_default_with_leaf_module_should_show_only_their_help(
    cmd_names_in_help_with_show_all,
):
    assert cmd_names_in_help_with_show_all == ["show all"]


# def test_help_show_plugins_with_invalid_argument_should_print_error_in_correct_format(
#     capfd,
# ):
#     mate_config.module_record.parse_command(["help", "show", "plugins", "YOYO"])
#     out, err = capfd.readouterr()
#     assert out == 'Undefined show plugins command: "YOYO". Try "help show plugins".\n'
