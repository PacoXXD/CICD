#!/usr/bin/python
# -*- coding: utf-8 -*-
import ruamel.yaml
import sys
from ruamel.yaml.util import load_yaml_guess_indent

CHART_NAME=sys.argv[1]
CHART_VERSION=sys.argv[2]

chart_file_name = '.helm/{}/Chart.yaml'.format(CHART_NAME)
config, ind, bsi = load_yaml_guess_indent(
    open(chart_file_name), preserve_quotes=True)

config['version'] = CHART_VERSION

ruamel.yaml.round_trip_dump(config, open(chart_file_name, 'w'),
                            # indent=ind, # ind is always wrong
							block_seq_indent=bsi)