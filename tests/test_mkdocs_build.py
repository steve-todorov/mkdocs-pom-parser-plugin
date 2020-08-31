import subprocess

from tests.test_mkdocs_base import TestMkDocsBase


class TestMkDocsServe(TestMkDocsBase):

    @classmethod
    def setUpClass(cls) -> None:
        process = subprocess.Popen(
            ['mkdocs', 'build', '--config-file', cls.mkdocsConfigFile, '--clean'],
            stdout=subprocess.PIPE, cwd=cls.mkdocsBasePath)
        output = process.communicate()
        print(output)
        assert process.returncode == 0, "Failed to run mkdocs build!"

    def test_mkdocs_index(self):
        self.assertFileContent(self.mkdocsSiteDir.joinpath('index.html'))

    def test_mkdocs_another_page(self):
        self.assertFileContent(self.mkdocsSiteDir.joinpath('another-page/index.html'))
