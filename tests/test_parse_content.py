import os
import unittest

from hogwarts_httprunner.loader import load_yaml
from hogwarts_httprunner.runner import runner, replace_var


class TestParseContent(unittest.TestCase):

    def test_parse_content(self):
        raw_str = "https://mubu.com/list?code=$code"
        variables_mapping = {
            "code": 0,
            "msg": "success"
        }
        replace_str = replace_var(raw_str, variables_mapping)
        self.assertEqual(replace_str, "https://mubu.com/list?code=0")

    def test_parse_content_with_no_var(self):
        raw_str = "https://mubu.com/list?code=123"
        variables_mapping = {
            "code": 0,
            "msg": "success"
        }
        replace_str = replace_var(raw_str, variables_mapping)
        self.assertEqual(replace_str, "https://mubu.com/list?code=123")