 # -*- coding: utf-8 -*-
#This script contain sample codes for different output methods in BeautifulSoup

from bs4 import BeautifulSoup
#using prettify

html_markup = """<p class="ecopyramid">
<ul id="producers">
<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>
<li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
</li>
</ul>"""
soup = BeautifulSoup(html_markup,"lxml")
print(soup.prettify())


producer_entry = soup.ul
print(producer_entry.prettify())

#using str

print(str(soup))

#using decode

print(soup.decode())

#using formatters

html_markup = """<html>
<body>&	&amp;	ampersand
¢	&cent;	cent
©	&copy;	copyright
÷	&divide;	divide
>	&gt;	greater than
				</body>
				</html>
"""
soup = BeautifulSoup(html_markup,"lxml")
print(soup.prettify())

#foramtter html

print(soup.prettify(formatter="html"))

#formatter None

print(soup.prettify(formatter=None))

#using function

def removeChara(markup):
	return markup.replace("a","")

print(soup.prettify(formatter=removeChara))

#get text

html_markup = """<p class="ecopyramid">
<ul id="producers">
<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>
<li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
</li>
</ul>"""
soup = BeautifulSoup(html_markup,"lxml")
print(soup.get_text())

#get text for removing scripts in site

import urllib2
from bs4 import BeautifulSoup
url = "http://www.packtpub.com/books"
page = urllib2.urlopen(url)
soup_packtpage = BeautifulSoup(page,"lxml")
[x.extract() for x in soup_packtpage.find_all('script')]
print(soup_packtpage.get_text())
