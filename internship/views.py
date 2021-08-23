from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
# from django.shortcuts import render_to_response
from django.urls import reverse_lazy, reverse
from django.contrib import messages
import glob
import json
from django.template import RequestContext

import requests
from bs4 import BeautifulSoup
import math
from requests.compat import quote_plus
import re
from databases.task import *


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", 
               "Accept-Encoding":"gzip, deflate", 
               "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
               "DNT":"1","Connection":"close", 
               "Upgrade-Insecure-Requests":"1"
               }

def homepage(request):
    r = requests.get(f'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en', headers=headers)
    print("yes")
    data = r.text
    soup = BeautifulSoup(data, features="html.parser")
    
    demo_program.delay()
    # # Get the url request to extract the number of results for the query.
    # r = requests.get(f'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en', headers=headers)
    # data = r.text
    # soup = BeautifulSoup(data, features="html.parser")
    # # soup=BeautifulSoup(data,'html5lib')
    
    
    # for title in soup.find_all('div', class_ = "xrnccd"):
    #     for item in title.find('article', class_ = "MQsxIb"):
    #         text_a = item.find('h3')
    #         text_link = item.find('a', class_ = 'RZIKme')
    #         text_title = title.find('h3').text
    #         # image = title.find('a').find('figure').find('img').get('src')
    #         image = title.find('a').find('figure')
    #         if image == None:
    #             pass
    #         else:
    #             image = image.find('img').get('src')
    #             if text_link == None:
    #                 pass
    #             else:
    #                 text_link = text_link.get('href')
    #                 text_link= text_link.replace("./", "news.google.com/")
    #                 if text_a==None and text_link==None:
    #                     pass
    #                 else:
    #                     print("                                                                                           ")
    #                     print("Start-----------------------------------------------------------------------------------------------------------------------------------------------")
    #                     print("Text", text_title)
    #                     print("URL", 'https://' +text_link)
    #                     print("Image", image)
    #                     print("End----------------------------------------------------------------------------------------------------")
      
        # something.delay()
    return HttpResponse("Working")