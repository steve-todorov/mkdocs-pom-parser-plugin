# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from mkdocs_pom_parser_plugin.parser import PomParser


class TestPomParser(unittest.TestCase):
    stringXml = '''<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>org.example</groupId>
    <artifactId>mkdocs-pom-parser-plugin</artifactId>
    <packaging>jar</packaging>
    <version>1.0.0-SNAPSHOT</version>
    <name>mkdocs-pom-parser-plugin name</name>
    <description>Some description</description>
    <url>https://github.com</url>
    <scm>
        <connection>scm:git:git://github.com</connection>
    </scm>
</project>
'''

    def test_getModelVersion(self):
        self.assertEqual('4.0.0', PomParser(self.stringXml).getModelVersion())

    def test_getGroupId(self):
        self.assertEqual('org.example', PomParser(self.stringXml).getGroupId())

    def test_getArtifactId(self):
        self.assertEqual('mkdocs-pom-parser-plugin', PomParser(self.stringXml).getArtifactId())

    def test_getPackaging(self):
        self.assertEqual('jar', PomParser(self.stringXml).getPackaging())

    def test_getVersion(self):
        self.assertEqual('1.0.0-SNAPSHOT', PomParser(self.stringXml).getVersion())

    def test_getName(self):
        self.assertEqual('mkdocs-pom-parser-plugin name', PomParser(self.stringXml).getName())

    def test_getDescription(self):
        self.assertEqual('Some description', PomParser(self.stringXml).getDescription())

    def test_getUrl(self):
        self.assertEqual('https://github.com', PomParser(self.stringXml).getUrl())

    def test_findByXpath(self):
        element = PomParser(self.stringXml).findByXpath("./groupId")
        self.assertIsNotNone(element)
        self.assertEqual('org.example', element.text)

    def test_findTextByXpath(self):
        element = PomParser(self.stringXml).findTextByXpath("./groupId")
        self.assertIsNotNone(element)
        self.assertEqual('org.example', element)

    def test_findByXpathDeep(self):
        element = PomParser(self.stringXml).findByXpath("./scm/connection")
        self.assertIsNotNone(element)
        self.assertEqual('scm:git:git://github.com', element.text)

    def test_findTextByXpathDeep(self):
        element = PomParser(self.stringXml).findTextByXpath("./scm/connection")
        self.assertIsNotNone(element)
        self.assertEqual('scm:git:git://github.com', element)


if __name__ == '__main__':
    unittest.main()
