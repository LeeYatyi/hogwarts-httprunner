import requests
from hogwarts_httprunner.loader import load_yaml


def run_yaml(yaml_file):
    load_json = load_yaml(yaml_file)
    requestors = load_json["request"]
    method = requestors.pop("method")
    url = requestors.pop("url")
    resp = requests.request(method, url, **requestors)
    validators = load_json["validate"]

    for key in validators:
        actual_value = getattr(resp, key)      # resp.key
        expected_value = validators[key]

        assert actual_value == expected_value
    return True

    return resp