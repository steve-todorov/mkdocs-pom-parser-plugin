import unittest
from pathlib import Path
import http.client


class TestMkDocsBase(unittest.IsolatedAsyncioTestCase):
    host = '0.0.0.0'
    port = '18001'

    def assertFileContent(self, page: Path):
        self.assertTrue(page.exists(), "{page} does not exist, it should")
        contents = page.read_text()
        self.assertIsNotNone(contents)
        self.assertTrue(page.name in contents)
        self.assertTrue('POM_MODEL_VERSION=4.0.0' in contents)
        self.assertTrue('POM_GROUP_ID=org.example' in contents)
        self.assertTrue('POM_ARTIFACT_ID=mkdocs-pom-parser-plugin' in contents)
        self.assertTrue('POM_PACKAGING=jar' in contents)
        self.assertTrue('POM_VERSION=1.0.0-SNAPSHOT' in contents)
        self.assertTrue('POM_NAME=mkdocs-pom-parser-plugin name' in contents)
        self.assertTrue('POM_DESCRIPTION=Some description' in contents)
        self.assertTrue('POM_URL=https://github.com' in contents)
        self.assertTrue('POM_SCM_CONNECTION=scm:git:git://github.com' in contents)

    def assertHttpContent(self, route: str):
        page_name = route.split("/")[-1]
        print("Connecting to " + self.host + ':' + self.port + '/' + route.lstrip("/"))

        client = http.client.HTTPConnection(self.host + ':' + self.port)
        client.request("GET", route)
        response = client.getresponse()
        print(self.host + ':' + self.port + '/' + route.lstrip("/"), response.status, response.reason)

        self.assertEqual(response.status, 200, "Should have found page " + self.host + ':' + self.port + '/' + route.lstrip("/"))

        contents = response.read().decode('utf-8')
        client.close()

        self.assertIsNotNone(contents)
        self.assertTrue(page_name in contents)
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
