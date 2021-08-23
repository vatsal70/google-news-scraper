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
    news = News.objects.all()
    params = {
        'news': news,
        }
    return render(request, 'internship/index.html', params)
