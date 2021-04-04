from mate.__main__ import main
from mate.__version__ import __author__, __version__
import sys


def test_mate_exec_show_mate(
    capfd,
):
    sys.argv = ["mate", "--exec", "show mate"]
    main()
    out, err = capfd.readouterr()
    assert out == "\nVersion: " + __version__ + "\n" + "Author: " + __author__ + "\n\n"
