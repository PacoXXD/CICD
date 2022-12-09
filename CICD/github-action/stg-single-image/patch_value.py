import ruamel.yaml
import sys
from ruamel.yaml.util import load_yaml_guess_indent

CHART_NAME = sys.argv[1]
DOCKER_TAG = sys.argv[2]
MAIN_CHART_NAME = sys.argv[3]

file_name = "stg/{0}/values.yaml".format(MAIN_CHART_NAME)

config, ind, bsi = load_yaml_guess_indent(open(file_name), preserve_quotes=True)

instances = config[CHART_NAME]
instances['image']['tag'] = DOCKER_TAG

ruamel.yaml.round_trip_dump(config, open(file_name, 'w'),
                            indent=ind,
                            block_seq_indent=bsi)
