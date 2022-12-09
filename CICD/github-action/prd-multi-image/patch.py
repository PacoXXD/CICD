import ruamel.yaml
import sys
from ruamel.yaml.util import load_yaml_guess_indent

CHART_NAME = sys.argv[1]
IMAGE_NAMES = sys.argv[2]
DOCKER_TAG = sys.argv[3]
VERSION = sys.argv[4]
MAIN_CHART_NAME = sys.argv[5]

file_name = "prd/{0}/values.yaml".format(MAIN_CHART_NAME)
requirement_file_name = "prd/{0}/requirements.yaml".format(MAIN_CHART_NAME)

config, ind, bsi = load_yaml_guess_indent(open(file_name), preserve_quotes=True)

instances = config[CHART_NAME]

images = IMAGE_NAMES.split(',')
for image in images:
    instances['image'][image]['tag'] = DOCKER_TAG

ruamel.yaml.round_trip_dump(config, open(file_name, 'w'),
                            indent=ind,
                            block_seq_indent=bsi)

config, ind, bsi = load_yaml_guess_indent(
    open(requirement_file_name), preserve_quotes=True)

for i in config['dependencies']:
    if i['name'] == CHART_NAME:
        i['version'] = VERSION

ruamel.yaml.round_trip_dump(config, open(requirement_file_name, 'w'),
                            indent=ind,
                            block_seq_indent=bsi)