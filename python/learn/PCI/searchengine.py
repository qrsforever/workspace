#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib import request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Create a list of words to ignore
ignorewords=set(['the','of','to','and','a','in','is','it'])

class crawler:
    # Initialize the crawler with the name of database
    def __init__(self, dbname):
        pass

    def __del__(self):
        pass

    def dbcommit(self):
        pass

    # Auxilliary function for getting an entry id and adding
    # it if it's not present
    def getentryid(self,table,field,value,createnew=True):
        return None

    # Index an individual page
    def addtoindex(self, url, soup):
        print('Indexing %s' % url)

    # Extract the text from an HTML page (no tags)
    def gettextonly(self, soup):
        return None

    # Separate the words by any non-whitespace character
    def separatewords(self, text):
        return None

    # Return true if this url is already indexed
    def isindexed(self, url):
        return False

    # Add a link between two pages
    def addlinkref(self, urlFrom, urlTo, linkText):
        pass

    # Create the database tables
    def createindextables(self):
        pass

    # Starting with a list of pages, do a breadth
    # first search to the given depth, indexing pages
    # as we go
    def crawl(self, pages, depth = 2):
        for i in range(depth):
            newpages = {}
            for page in pages:
                try:
                    c = request.urlopen(page)
                except:
                    print("Could not open %s" % page)
                    continue
                try:
                    soup = BeautifulSoup(c.read(), "html.parser")
                    self.addtoindex(page, soup)
                    links = soup('a')
                    for link in links:
                        if ('href' in dict(link.attrs)):
                            url = urljoin(page, link['href'])
                            print(url)
                            if url.find("'") != -1: continue
                            url = url.split('#')[0]  # remove location portion
                            if url[0:4] == 'http' and not self.isindexed(url):
                                newpages[url] = 1
                            linkText = self.gettextonly(link)
                            self.addlinkref(page, url, linkText)
                    self.dbcommit()
                except Exception as e:
                    print(e)
                    print("Could not parse page %s" % page)

            pages = newpages

def main():
    mycrawler = crawler('')
    pages = ["https://en.wikipedia.org/wiki/Python_(programming_language)"]
    mycrawler.crawl(pages,depth=2)

if __name__ == "__main__":
    main()
