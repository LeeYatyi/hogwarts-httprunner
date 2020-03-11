import requests
import unittest


class TestMubuLogin(unittest.TestCase):

    def test_get_homepage(self):
        url = "https://mubu.com"
        method = "GET"
        headers = {
            "user - agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
        }
        kwargs = {
            "headers": headers,
            "verify": False
        }
        resp = requests.request(method, url, **kwargs)
        assert resp.status_code == 200

    def test_get_login(self):
        url = "https://mubu.com/login"
        method = "GET"
        headers = {
            "user - agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
        }
        kwargs = {
            "headers": headers,
            "verify": False
        }
        resp = requests.request(method, url, **kwargs)
        assert resp.status_code == 200

    def test_get_login_password(self):
        url = "https://mubu.com/login/password"
        method = "GET"
        headers = {
            "user - agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
        }
        kwargs = {
            "headers": headers,
            "verify": False
        }
        resp = requests.request(method, url, **kwargs)
        assert resp.status_code == 200

    def test_post_submit(self):
        url = "https://mubu.com/api/login/submit"
        method = "POST"
        headers = {
            "user - agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
        }
        data = "phone=18911773181&password=leeyatyi%40123456&remember=true"
        kwargs = {
            "headers": headers,
            "data": data,
            "verify": False
        }
        resp = requests.request(method, url, **kwargs)

        assert resp.status_code == 200
        # resp_json = resp.json()
        # assert resp_json['code'] == 0

# if __name__ == '__main__':
#     TestMubuLogin().test_get_homepage()