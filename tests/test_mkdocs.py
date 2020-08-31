import pathlib

import yaml
import tempfile
import unittest

from pathlib import Path
from click.testing import CliRunner
from mkdocs.__main__ import build_command

mkdocsConfigFile = pathlib.Path(__file__).parent.absolute().joinpath('resources/mkdocs.yml').resolve()
config = yaml.load(open(mkdocsConfigFile, 'rb'), Loader=yaml.Loader)

class TestWithMkDocs(unittest.TestCase):

    def test_mkdocs(self):
        runner = CliRunner()

        with tempfile.TemporaryDirectory() as tmpdir:
            result = runner.invoke(build_command, ['--clean', '--config-file', mkdocsConfigFile, '--site-dir', tmpdir])

            print(result.output)

            self.assertEqual(result.exit_code, 0)

            index_file = Path(tmpdir) / 'index.html'
            assert index_file.exists(),  f"{index_file} does not exist, it should"
            contents = index_file.read_text()

            self.assertTrue('POM_MODEL_VERSION=4.0.0' in contents)
            self.assertTrue('POM_GROUP_ID=org.example' in contents)
            self.assertTrue('POM_ARTIFACT_ID=mkdocs-pom-parser-plugin' in contents)
            self.assertTrue('POM_PACKAGING=jar' in contents)
            self.assertTrue('POM_VERSION=1.0.0-SNAPSHOT' in contents)
            self.assertTrue('POM_NAME=mkdocs-pom-parser-plugin name' in contents)
            self.assertTrue('POM_DESCRIPTION=Some description' in contents)
            self.assertTrue('POM_URL=https://github.com' in contents)
            self.assertTrue('POM_SCM_CONNECTION=scm:git:git://github.com' in contents)

if __name__ == '__main__':
    unittest.main()
