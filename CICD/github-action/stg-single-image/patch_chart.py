import ruamel.yaml
import sys
from ruamel.yaml.util import load_yaml_guess_indent

CHART_NAME = sys.argv[1]
VERSION = sys.argv[2]
MAIN_CHART_NAME = sys.argv[3]

requirement_file_name = "stg/{0}/requirements.yaml".format(MAIN_CHART_NAME)

config, ind, bsi = load_yaml_guess_indent(
    open(requirement_file_name), preserve_quotes=True)

for i in config['dependencies']:
    if i['name'] == CHART_NAME:
        i['version'] = VERSION

ruamel.yaml.round_trip_dump(config, open(requirement_file_name, 'w'),
                            indent=ind,
                            block_seq_indent=bsi)
