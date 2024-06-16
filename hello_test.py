import unittest
from click.testing import CliRunner
from hello import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        runner = CliRunner()
        result = runner.invoke(hello, ["--name", "Thor", "--color", "red"])
        self.assertIn("Thor", result.output)

    def test_hello_should_fail(self):
        runner = CliRunner()
        result = runner.invoke(hello, ["--name", "Thor", "--color", "red"])
        self.assertNotIn("Bob", result.output)
