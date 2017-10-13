from lxml import html
from lxml.cssselect import CSSSelector
import requests as r
import urllib2

class SongGrabber(object):
    def __init__(self):
        self.url='http://tubidy.mobi'
        self.search_url = self.url+'/search.php?q='
        self.selector = CSSSelector('div.media-body')

    def search(self,song):
        page = r.get(self.search_url+song)
        tree = html.fromstring(page.content)
        items = []
        for i in self.selector(tree):
            items.append(i)

        return items

    def get_page(self,item):
        links = html.iterlinks(item)
        l = []
        for i in links:
            l.append(i)

        page = r.get(l[0][2])
