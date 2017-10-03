# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:43:20 2017

@author: Abc
"""

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import lxml.html

class NirmaSpider(CrawlSpider):
    name = "Nirma"
    start_urls = [
        'http://nirmauni.ac.in/itnu'
    ]
    
    allowed_domains = ['www.nirmauni.ac.in']
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('a',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print(response.url)
        t = lxml.html.parse(response.url)
        item_links = t.find(".//title").text
        k=response.body.decode(response.encoding)
        #print(k)
        yield {'url':response.url,
               'title':item_links,
                'body':k,}    
       
        
    def parse_no_follow(self, response):
        print("Not")