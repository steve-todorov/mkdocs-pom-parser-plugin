import subprocess
import time

from tests.test_mkdocs_base import TestMkDocsBase


class TestMkDocsServe(TestMkDocsBase):
    process = None

    def setUp(self) -> None:
        self.process = subprocess.Popen(
            ['mkdocs', 'serve', '--config-file', self.mkdocsConfigFile, '-a', self.host + ':' + self.port],
            stdout=subprocess.PIPE, cwd=self.mkdocsBasePath)
        # server needs less than 1 second to generate the docs, but sleeping for 2 just in case VM is slow.
        time.sleep(2)

    def tearDown(self) -> None:
        self.process.kill()

    def test_mkdocs_index(self):
        self.assertHttpContent('/index.html')

    def test_mkdocs_another_page(self):
        self.assertHttpContent('/another-page/index.html')
