 # -*- coding: utf-8 -*-
#This scipt contain sample codes for encoding support in Beautiful Soup
from bs4 import BeautifulSoup

#without encoding specified

html_markup = """<p> The Spanish language is written using the Spanish alphabet, which is the Latin alphabet  with one additional letter, eñe ?ñ?, for a total of 27 letters.</p>
"""
soup = BeautifulSoup(html_markup,"lxml")
print(soup.p.string)

#with utf-8

soup = BeautifulSoup(html_markup,"lxml",from_encoding="utf-8")
print(soup.prettify())

#with latin-1
soup = BeautifulSoup(html_markup,"lxml",from_encoding="latin-1")
print(soup.prettify())

#original encoding

html_markup = """
<html>
<meta http-equiv="Content-Type" content="text/html;charset=ISO8859-2"/>
<p>cédille (from French), is a hook or tail ( ž )  added under certain letters as a diacritical mark to modify their pronunciation
</p>"""
soup = BeautifulSoup(html_markup,"lxml") 
print(soup.original_encoding)


#using specific encoding in output

print(soup.prettify("ISO8859-2"))

#using encode

print(soup.p.encode())


#encode using specific encoding 

print(soup.encode("ISO-8859-2"))
