import jsonpath
import requests
from requests import sessions
from hogwarts_httprunner.loader import load_yaml
import re


session = sessions.Session()
session_variables_mapping = {}
vavriable_regex_compile = re.compile(r".*\$(\w+).*")


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


def is_testsuite(content):
    pass


def replace_var(content, variables_mapping):
    matched = vavriable_regex_compile.match(content)
    if not matched:
        return content
    var_name = matched[1]
    value = variables_mapping[var_name]
    replaced_content = content.replace("${}".format(var_name), str(value))
    return replaced_content


def parse_content(content, variables_mapping):
    if isinstance(content, dict):
        parsed_content = {}
        for key, value in content.items():
            parsed_value = parse_content(value, variables_mapping)
            parsed_content[key] = parsed_value
        return parsed_content

    elif isinstance(content, list):
        parsed_content = []
        for item in content:
            parsed_item = parse_content(item, variables_mapping)
            parsed_content.append(parsed_item)
        return parsed_content

    elif isinstance(content, str):
        return replace_var(content, variables_mapping)

    else:
        return content


def run_api(api_json):
    """
    :param api_json:
                    {
                    "request":{},
                    "validate":{}
                    }
    :return:
    """
    requestors = api_json["request"]
    global session_variables_mapping
    parsed_requestors = parse_content(requestors, session_variables_mapping)
    print("parsed_request------", parsed_requestors)

    method = parsed_requestors.pop("method")
    url = parsed_requestors.pop("url")
    resp = session.request(method, url, **parsed_requestors)
    validators = api_json["validate"]

    for key in validators:
        if "$" in key:
            # key = "$.code"
            actual_value = extract_json_field(resp, key)
        else:
            actual_value = getattr(resp, key)      # resp.key
        expected_value = validators[key]

        assert actual_value == expected_value

    extractor_mapping = api_json.get("extract", {})  # 避免无extract情况
    for var_name in extractor_mapping:
        var_expr = extractor_mapping[var_name]     # code: $.code
        var_value = extract_json_field(resp, var_expr)
        session_variables_mapping[var_name] = var_value
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