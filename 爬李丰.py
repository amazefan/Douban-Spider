# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:38:46 2017

@author: Administrator
"""

import urllib.request as urlreq
import os
import re
 
def urlread(url):
    request = urlreq.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
    response = urlreq.urlopen(request)
    html = response.read()
    return html

def lessonfind(url):
    html = urlread(url).decode('utf-8')
    lessonname= re.findall(r'/teaching/(?:\w+-?)+/',html)
    return lessonname

def filefind(url):
    html = urlread(url)
    html = html.decode('utf-8')
    pdfname = re.findall(r'/files/\w+/\w+(?:\.[0-9])?(?:-\w+)+\.pdf',html)
    pdf_ads = []
    for pdf in pdfname :
        ads = 'https://feng.li' + pdf
        pdf_ads.append(ads)
    return pdf_ads

def save_pdf(pdf_ads):
        for each in pdf_ads:
          filename = each.split('/')[-2]+each.split('/')[-1]
          with open(filename,'wb') as f:
               pdf = urlread(each)
               f.write(pdf)


def downloadpdf(folder = 'feng.li'):
    os.mkdir(folder)
    os.chdir(folder)
    
    url = 'https://feng.li/teaching/'
    lesson = lessonfind(url)[1:-1]
    for i in range(len(lesson)):
        if i >= 1:
            if lesson[i] == lesson[i-1]: pass
            else: 
                try:save_pdf(filefind('https://feng.li'+ lesson[i]))
                except: pass
        else:
            try: save_pdf(filefind('https://feng.li'+ lesson[0]))
            except: pass
        
    
    
    