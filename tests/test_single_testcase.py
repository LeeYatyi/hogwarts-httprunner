import os
import unittest

from hogwarts_httprunner.loader import load_yaml
from hogwarts_httprunner.runner import runner


class TestSingleAPI(unittest.TestCase):

    def test_loader_single_testcae(self):
        """
        加载出来的接口请求参数与原始信息一致
        :return:
        """
        single_testcase_yaml = os.path.join(os.path.dirname(__file__), "testcases", "mubu_login.yml")
        loaded_json = load_yaml(single_testcase_yaml)
        self.assertIsInstance(loaded_json, list)
        self.assertEqual(len(loaded_json), 5)

    def test_runner_single_testcase(self):
        single_testcase_yaml = os.path.join(os.path.dirname(__file__), "testcases", "mubu_login.yml")
        result = runner(single_testcase_yaml)
        self.assertEqual(len(result), 5)


