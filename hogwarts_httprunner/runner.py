import jsonpath
import requests
from hogwarts_httprunner.loader import load_yaml


def extract_json_field(resp, json_field):
    value = jsonpath.jsonpath(resp.json(), json_field)
    return value[0]


def run_yaml(yaml_file):
    load_json = load_yaml(yaml_file)
    requestors = load_json["request"]
    method = requestors.pop("method")
    url = requestors.pop("url")
    resp = requests.request(method, url, **requestors)
    validators = load_json["validate"]

    for key in validators:
        if "$" in key:
            # key = "$.code"
            actual_value = extract_json_field(resp, key)
        else:
            actual_value = getattr(resp, key)      # resp.key
        expected_value = validators[key]

        assert actual_value == expected_value

    return True