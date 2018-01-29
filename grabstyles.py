from lxml import html
import requests


def grab():
    page = requests.get('http://github.com')
    tree = html.fromstring(page.content)
    styles = tree.xpath('//link[@rel="stylesheet"]/@href')[:2]
    for style in styles:
        name = style.split('/')[-1].split('-')[0]
        res = requests.get(style)
        with open(name+'.css', 'wb') as f:
            f.write(res.content)

grab()
