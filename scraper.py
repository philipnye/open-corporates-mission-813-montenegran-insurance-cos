#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scraperwiki

import json

from datetime import date
from bs4 import BeautifulSoup
import requests
#import turbotlib

import HTMLParser
h = HTMLParser.HTMLParser()

sample_date = str(date.today())
#turbotlib.log("Starting scrape...") # optional debug logging

page_url_stub="http://www.ano.me"

group_of_cover_pages=(
    {"category":"INSURANCE COMPANIES","cover_url_stub":"http://www.ano.me/en/index.php?option=com_content&view=category&layout=blog&id=44&Itemid=113"},
    {"category":"INSURANCE BROKERAGE COMPANIES","cover_url_stub":"http://www.ano.me/en/index.php?option=com_content&view=category&layout=blog&id=45&Itemid=114"},
    {"category":"INSURANCE AGENCY COMPANIES","cover_url_stub":"http://www.ano.me/en/index.php?option=com_content&view=category&layout=blog&id=46&Itemid=115"},
    {"category":"ENTREPRENEURS – INSURANCE AGENTS","cover_url_stub":"http://www.ano.me/en/index.php?option=com_content&view=category&layout=blog&id=47&Itemid=116"},
    {"category":"AGENCIES FOR ANCILLARY INSURANCE SERVICES","cover_url_stub":"http://www.ano.me/en/index.php?option=com_content&view=category&layout=blog&id=49&Itemid=117"},
    {"category":"AUTHORIZED INSURANCE AGENTS AND BROKERS","cover_url_stub":"http://www.ano.me/en/index.php?option=com_content&view=category&layout=blog&id=55&Itemid=124"}
    )

def scrape_page_contents(page_doc):
    ps = page_doc.find_all("p")            #grabs rows which hold data (exclusively)
    ps_redux=ps[:-2]            #gets rid of final two ps - which contain 'forgot your password'/'forgot your username' messages, not company data
    
    
    headings_ps=page_doc.find_all("strong")
    for heading_p in headings_ps:
        print heading_p.text

    



    # record = {
    #     'company_name': tds[0].text,
    #     'group_name': tds[1].text,
    #     'sample_date': sample_date,   # mandatory field
    #     'source_url': source_url      # mandatory field
    # }
    # print json.dumps(record) #outputs record as json
    # return


for cover_page in group_of_cover_pages:                         
    cover_response = requests.get(cover_page["cover_url_stub"])
    cover_html = cover_response.content
    cover_doc = BeautifulSoup(cover_html)
    options=cover_doc.find_all("option")      #gets the details of drop-down menus for each cover page
    options_redux=options[1:]           #ditches 'please select from drop-down list' drop-down item
    for option in options_redux:
        unescaped_URL= h.unescape(option["value"])      #grabs URLs from the drop down menus and sorts out ampersand fuck-ups
        page_url=page_url_stub+unescaped_URL
        print page_url
        page_response = requests.get(page_url)
        page_html = page_response.content
        page_doc = BeautifulSoup(page_html)
        scrape_page_contents(page_doc)