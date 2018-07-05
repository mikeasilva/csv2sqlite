
from csv2sqlite.cli import main


def test_main():
    assert main([]) == 0
