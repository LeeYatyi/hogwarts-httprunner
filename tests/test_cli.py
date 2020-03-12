import subprocess
import unittest
import os


class TestCli(unittest.TestCase):

    def test_hoghrun_single_yaml(self):
        single_api_yaml = os.path.join(os.path.dirname(__file__), "api", "post_submit.yml")
        print(single_api_yaml)
        subprocess.run("hoghrun {}".format(single_api_yaml))