from datetime import datetime
import yaml
import argparse
import os
import sys



def create_directory(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)


with open('config.yaml') as f:
	config = yaml.safe_load(f)

home = os.path.expanduser('~')
datadir = os.path.join(home, '.journalist')

parser = argparse.ArgumentParser()
parser.add_argument('name', help='The name of the journal', type=str)
args = parser.parse_args()


journal_path = os.path.join(datadir, name)
if not os.path.exists(journal_path):
	res = input('The journal {} does not exist. Do you want to create it >: ')
	if y in res:
		os.makedirs(journal_path)
	else:
		sys.exit()
