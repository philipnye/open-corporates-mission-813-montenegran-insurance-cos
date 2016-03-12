#!/usr/bin/env python

import scraperwiki

import json

from datetime import date
from bs4 import BeautifulSoup
import requests
#import turbotlib
from urllib import unquote

sample_date = str(date.today())
#turbotlib.log("Starting scrape...") # optional debug logging

'''



http://ano.me/en/index.php?option=com_content&view=article&id=178&catid=44&Itemid=113
http://ano.me/en/index.php?option=com_content&view=article&id=208&catid=45&Itemid=114
http://ano.me/en/index.php?option=com_content&view=article&id=128&catid=46&Itemid=115
http://ano.me/en/index.php?option=com_content&view=article&id=230&catid=47&Itemid=116
http://ano.me/en/index.php?option=com_content&view=article&id=143&catid=49&Itemid=117
http://ano.me/en/index.php?option=com_content&view=article&id=155&catid=55&Itemid=124 #different
'''


url_stub1="http://ano.me/en/index.php?option=com_content&view=article&id="
url_stub2="&catid="
url_stub3="&Itemid="
    
i=178
j = 44
k = 113

source_url = url_stub1 + str(i) + url_stub2 + str(j) + url_stub3 + str(k)
    
response = requests.get(source_url)
html = response.content
doc = BeautifulSoup(html)

if doc.find('div', id='errorboxheader') is None:
    ps = doc.find_all("p", style = "line-height: 135%;")            #grabs rows which hold data (exclusively)
    print ps
        
    details = []
    concat_details= None
    to_save = []
        
    for p in ps:
        count=0
        #print p
        #print p.find("strong")
        if p.find("strong") is not None:
            if category is not None: #compiles all details to be saved into a list. Doesn't save on first pass, when no data has been gathered
                #print details
                concat_details='\n'.join(details)
                to_save.append([category,concat_details])
                #print to_save
            if p.text.strip()[-1] == ":": #tidies up category of information
                category = p.text.strip()[:-1]
            else:    
                category = p.text.strip()
            details = [] #ready to take new data
            #print category
        else:
            data_line = p.text.strip()
            #print data_line
            details.append(data_line) #each category can have multiple answers - saves each to a list
    concat_details='\n'.join(details)
    to_save.append([category,concat_details]) #adding last row of data to our list of data to be saved





if doc.find('div', id='errorboxheader') is None:
ps = doc.find_all("p", style = "line-height: 135%;")            #grabs rows which hold data (exclusively)
print ps
        
details = []
concat_details= None
to_save = []
        
for p in ps:_redux 
    headings_ps=ps.find_all("strong")







    count=0
    #print p
    #print p.find("strong")
    if p.find("strong") is not None:
        if category is not None: #compiles all details to be saved into a list. Doesn't save on first pass, when no data has been gathered
            #print details
            concat_details='\n'.join(details)
            to_save.append([category,concat_details])
                #print to_save
        if p.text.strip()[-1] == ":": #tidies up category of information
            category = p.text.strip()[:-1]
        else:    
            category = p.text.strip()
            details = [] #ready to take new data
            #print category
    else:
        data_line = p.text.strip()
        #print data_line
        details.append(data_line) #each category can have multiple answers - saves each to a list
concat_details='\n'.join(details)
to_save.append([category,concat_details]) #adding last row of data to our list of data to be saved
