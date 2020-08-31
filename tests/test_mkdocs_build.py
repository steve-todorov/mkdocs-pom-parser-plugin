import pathlib

from click.testing import CliRunner
from mkdocs.__main__ import build_command

from tests.test_mkdocs_base import TestMkDocsBase

mkdocsConfigFile = pathlib.Path(__file__).parent.absolute().joinpath('resources/mkdocs.yml').resolve()
mkdocsSiteDir = pathlib.Path(__file__).parent.absolute().joinpath('resources/site')


class TestMkDocsServe(TestMkDocsBase):

    @classmethod
    def setUpClass(cls) -> None:
        runner = CliRunner()
        result = runner.invoke(build_command, ['--clean', '--config-file', mkdocsConfigFile])
        print(result.output)
        assert result.exit_code == 0, "Failed to run mkdocs build!"

    def test_mkdocs_index(self):
        self.assertFileContent(mkdocsSiteDir.joinpath('index.html'))

    def test_mkdocs_another_page(self):
        self.assertFileContent(mkdocsSiteDir.joinpath('another-page/index.html'))
