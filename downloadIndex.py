#!/usr/bin/python

__author__ = 'kevin'



import urllib2
import sys
from HTMLParser import HTMLParser
import subprocess


class IndexParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.download_list = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            if '.pdf' in attrs[0][1]:
                self.download_list.append(attrs[0][1])
    def get_list(self):
        return self.download_list


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        print("usage: {} http://example.com/foo/bar/".format(sys.argv[0]))
        exit(1)
    url = args[0]
    result = None
    try:
        result = urllib2.urlopen(url).read()
    except:
        print("Invalid URL")
        print("usage: {} http://example.com/foo/bar/".format(sys.argv[0]))
        exit(1)
    if not result:
        print("something broke :(")
        exit(1)
    parser = IndexParser()
    parser.feed(result)
    list = parser.get_list()
    for slide in list:
        subprocess.call("wget " + url+slide, shell=True)