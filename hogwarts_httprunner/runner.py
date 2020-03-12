import jsonpath
import requests
from hogwarts_httprunner.loader import load_yaml


def extract_json_field(resp, json_field):
    value = jsonpath.jsonpath(resp.json(), json_field)
    return value[0]

def is_api(content):
    if not isinstance(content, dict):
        return False
    if "request" and "validate" not in content:
        return False
    return True

def is_testcases(content):
    if not isinstance(content, list):
        return False
    for item in content:
        if not is_api(item):
            return False
    return True

def is_testsuit(content):
    pass


def run_api(api_json):
    """
    {
    "request":{},
    "validate":{}
    }
    :param api_json:
    :return:
    """
    requestors = api_json["request"]
    method = requestors.pop("method")
    url = requestors.pop("url")
    resp = requests.request(method, url, **requestors)
    validators = api_json["validate"]

    for key in validators:
        if "$" in key:
            # key = "$.code"
            actual_value = extract_json_field(resp, key)
        else:
            actual_value = getattr(resp, key)      # resp.key
        expected_value = validators[key]

        assert actual_value == expected_value

    return True


def runner(yaml_file):
    loaded_content = load_yaml(yaml_file)
    result_list = []
    if is_api(loaded_content):
        result = run_api(loaded_content)
        result_list.append(result)
    elif is_testcases(loaded_content):
        for api_content in loaded_content:
            result = run_api(api_content)
            result_list.append(result)
    else:
        raise Exception("YAML format invalid {}".format(yaml_file))

    return result_list