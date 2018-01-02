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
        entries.append((dt, contents))

    entries.sort(key=lambda x: x[0])
    return entries


def githubify(text):
    r = requests.post('https://api.github.com/markdown/raw', data=text, headers={'Content-Type': 'text/x-markdown'})
    return r.text


@app.route('/journalist')
def view_journal():
    name = request.args.get('name')
    entries = get_entries(name)

    text = ''
    for entry in entries:
        text = text + entry[1] + '<br><br>'
    text = '__Sounds__ good? I _think_ [so](https://www.google.com).'
    return render_template('journal.html', article=githubify(text))
