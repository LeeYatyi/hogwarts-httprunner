import yaml


def load_yaml(yaml_file):
    with open(yaml_file, "r") as f:
        loaded_json = yaml.load(f)
    return loaded_json

