from click.testing import CliRunner
from project import cli


def test_add():
    runner = CliRunner()
    result = runner.invoke(cli.add, ["1", "2"])
    assert result.exit_code == 0
    assert result.output == "3.0\n"
