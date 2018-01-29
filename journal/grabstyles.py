from lxml import html
import requests
import os


def grab():
    page = requests.get('http://github.com')
    tree = html.fromstring(page.content)
    styles = tree.xpath('//link[@rel="stylesheet"]/@href')[:2]

    for style in styles:
        name = style.split('/')[-1].split('-')[0]
        response = requests.get(style)

        with open(os.path.join('static', name+'.css'), 'wb') as f:
            f.write(response.content)


if __name__=='__main__':
	grab()
