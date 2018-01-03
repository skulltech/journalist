# journalist
App to write journal digitally. 

[![PyPI version](https://badge.fury.io/py/journalist.svg)](https://badge.fury.io/py/journalist)

## Features

- Write your journal using _Markdown_ in your favorite text-editor.
- Stores written journals in a comprehensive directory structure.
- View the journals (_Markdown_ rendered in _HTML_) in browser.

# Installation

Install it using `pip`
```console
pip install journalist
```

# Usage 

```console
sumit at HAL9000 in ~ 
$ python3 journalist.py -h
usage: journalist.py [-h] {write,view} name

positional arguments:
  {write,view}  Task to do
  name          The name of the journal

optional arguments:
  -h, --help    show this help message and exit
```

## Usage Examples

### Writing journal

Journals are stored in the directory `~/.journalist` in the following structure.

```console
.journalist
└── journalname
     └── YYYY
        └── MM
            └── YYYY-MM-DD-Day.md
```

For example, an example `~/.Journalist` directory may contain
```console
sumit@HAL9000:pts/0->/home/sumit (0) 
> tree .journalist 
.journalist
├── personal
│   ├── 2017
│   │   └── 12
│   │       └── 2017-12-28-Thu.md
│   └── 2018
│       └── 01
└── technical
    ├── 2017
    │   └── 12
    │       ├── 2017-12-28-Thu.md
    │       └── 2017-12-29-Fri.md
    └── 2018
        └── 01
            └── 2018-01-03-Wed.md

10 directories, 4 files
```

To write in a the journal _personal_, type in the following...
```console
sumit at HAL9000 in ~
$ python3 journalist.py write personal
```

- If any journal named _personal_ already exists, it will open up the relevant `.md` file corresponding to the system date (creating it if it doesn't exist).
- If any journal named _personal_ doesn't exist, it will prompt the user if they want to create a new journal. If they agree, it will do so and open the corresponding `.md` file as described above.

The _markdown_ file will be opened in the editor mentioned in the `config.yaml` file (default is `nano`). If you change it to something else, make sure an file named `filename.md` can be opened using that editor by typing `editor filename.md` in the terminal.

### Viewing journal

```console
sumit at HAL9000 in ~ 
$ python3 journalist.py view personal 
[*] Starting Journalist viewer webapp...
[*] View this journal at http://127.0.0.1:5000/journalist?name=personal
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Opening the [URL](http://127.0.0.1:5000/journalist?name=personal) http://127.0.0.1:5000/journalist?name=personal in the browser would show us the journal entries rendered in HTML.
