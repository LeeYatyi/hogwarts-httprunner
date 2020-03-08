import requests
import unittest


class TestMubuLogin(unittest.TestCase):

    def test_get_homepage(self):
        url = "https://mubu.com"
        headers = {
            "user - agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
        }
        resp = requests.get(url, headers=headers, verify=False)
        assert resp.status_code == 200

if __name__ == '__main__':
    TestMubuLogin().test_get_homepage()