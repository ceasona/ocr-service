import os
import sys
import yaml

__dir__ = os.path.dirname(os.path.abspath(__file__))


def load_conf():
    config_file = os.path.join(__dir__, 'ocr_service.yaml')
    if not config_file:
        print("Error: Config file is not found")
        sys.exit(-1)
    with open(config_file, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config


conf = load_conf()

