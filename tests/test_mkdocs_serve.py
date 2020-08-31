import pathlib
import subprocess
import sys
import time

from tests.test_mkdocs_base import TestMkDocsBase

mkdocsConfigFile = pathlib.Path(__file__).parent.absolute().joinpath('resources/mkdocs.yml').resolve()
mkdocsSiteDir = pathlib.Path(__file__).parent.absolute().joinpath('resources/site')

def output_reader(proc, file):
    while True:
        byte = proc.stdout.read(1)
        if byte:
            sys.stdout.buffer.write(byte)
            sys.stdout.flush()
            file.buffer.write(byte)
        else:
            break


class TestMkDocsServe(TestMkDocsBase):

    process = None

    def setUp(self) -> None:
        self.process = subprocess.Popen(['mkdocs', 'serve', '--config-file', mkdocsConfigFile, '-a', self.host + ':' + self.port], stdout=subprocess.PIPE)
        # server needs less than 1 second to generate the docs, but sleeping for 2 just in case VM is slow.
        time.sleep(2)

    def tearDown(self) -> None:
        self.process.kill()

    def test_mkdocs_index(self):
        self.assertHttpContent('/index.html')

    def test_mkdocs_another_page(self):
        self.assertHttpContent('/another-page/index.html')

