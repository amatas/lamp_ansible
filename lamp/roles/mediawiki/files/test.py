import unittest
import requests

TEST_SERVER="192.168.50.11"

class mediawiki_test(unittest.TestCase):
    def test_root(self):
        r = requests.get('http://' + TEST_SERVER, verify=False)
        self.assertEquals(r.status_code, 200)

    def test_redirect(self):
        r = requests.get('http://' + TEST_SERVER, verify=False)
        self.assertEquals(r.history[0].status_code, 301)
        self.assertEquals(r.url, 'http://' + TEST_SERVER + '/wiki/index.php/Main_Page')

    def test_content(self):
        r = requests.get('http://' + TEST_SERVER, verify=False)
        self.assertEquals(r.history[0].status_code, 301)
        self.assertEquals(r.url, 'http://' + TEST_SERVER + '/wiki/index.php/Main_Page')
        self.assertTrue('MediaWiki has been successfully installed.' in r.content)

if __name__ == '__main__':
    unittest.main()
