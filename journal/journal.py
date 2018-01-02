import os
import glob
from datetime import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash



app = Flask(__name__)

def get_entries(name):
	home = os.path.expanduser('~')
	journaldir = os.path.join(home, '.journalist', name)
	if not os.path.exists(journaldir):
		return False

	entries = []
	for file in glob.glob(os.path.join(journaldir, '**', '*.md'), recursive=True):
		filename =  os.path.basename(file)
		dt = datetime.strptime(filename, '%Y-%m-%d-%a.md')
		with open(file) as f:
			contents = f.read()
		entries.append((dt, contents))

	entries.sort(key=lambda x: x[0])
	return entries


@app.route('/journalist')
def view_journal():
	name = request.args.get('name')
	entries = get_entries(name)

	text = ''
	for entry in entries:
		text = text + entry[1] + '<br><br>'
	return text
