import os
import glob
from datetime import datetime
from flask import Flask, request, render_template
import requests



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
        entries.append({'datetime': dt, 'date': dt.strftime('%A. %b %d, %Y'), 'shortdate': dt.strftime('%Y-%m-%d'), 'content': githubify(contents)})

    entries.sort(key=lambda x: x['datetime'])
    return entries


def githubify(text):
    r = requests.post('https://api.github.com/markdown/raw', data=text, headers={'Content-Type': 'text/x-markdown'})
    return r.text


@app.route('/journalist')
def view_journal():
    name = request.args.get('name')
    entries = get_entries(name)
    return render_template('journal.html', name=name, entries=entries)
