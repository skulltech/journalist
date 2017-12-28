from datetime import datetime
import yaml
import argparse
import os
import sys
import subprocess



def create_directory(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

def response(question):
	answer = input('[?] {}: [y/n] '.format(question))
	if not answer or answer[0].lower() != 'y':
	    return False
	return True


with open('config.yaml') as f:
	config = yaml.safe_load(f)

home = os.path.expanduser('~')
datadir = os.path.join(home, '.journalist')

parser = argparse.ArgumentParser()
parser.add_argument('name', help='The name of the journal', type=str)
args = parser.parse_args()
name = args.name

journal_path = os.path.join(datadir, name)
if not os.path.exists(journal_path):
	print('[!] The journal {} does not exist!'.format(name))
	res	= response('Do you want to create journal {}'.format(name))
	if res:
		os.makedirs(journal_path)
	else:
		sys.exit()

date = datetime.now()
filename = date.strftime('%Y-%m-%d-%a') + '.md'
curdir = os.path.join(datadir, name, date.strftime('%Y'), date.strftime('%m'))
create_directory(curdir)
subprocess.call(['nano', os.path.join(curdir, filename)])
