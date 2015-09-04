#!/usr/bin/env python

from crawler import Crawler
from threading import Lock

class TestCrawler(Crawler):
    def __init__(self):
        super(TestCrawler, self).__init__()
        self.process_lock = Lock()

    def process_document(self, doc):
        self.process_lock.acquire()
        print 'GET', doc.status, doc.url, doc.text
        self.process_lock.release()

c = TestCrawler()

c.add_url_filter('http://www.ryuniverse.com/blog/[\x21-\x7E]+')
c.add_url_filter('http://ryuniverse.com/blog/[\x21-\x7E]+')

c.crawl('http://www.ryuniverse.com')