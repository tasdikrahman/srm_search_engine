#This script contains examples for creating BeautifulSoup using string, URL and a local file
from bs4 import BeautifulSoup
import urllib2
#Creating BeautifulSoup using string.

helloworld = "<p>Hello World</p>"
soup_string = BeautifulSoup(helloworld)
print(soup_string)


#using URL
import urllib2
from bs4 import BeautifulSoup
url = "http://www.packtpub.com/books"
page = urllib2.urlopen(url)
soup_packtpage = BeautifulSoup(page)
print(soup_packtpage)


#using local file
with open("foo.html","r") as foo_file:
	soup_foo = BeautifulSoup(foo_file)

print(soup_foo)

#creating Beautiful Soup for Xml 

soup_xml = BeautifulSoup(helloworld,features= "xml")
print(soup_xml)

#Accessing tag in an HTML

html_atag = """<html><body><p>Test html a tag example</p>
<a href="http://www.packtpub.com">Home</a>
<a href="http;//www.packtpub.com/books">Books</a>
</body>
</html>"""
soup  = BeautifulSoup(html_atag,"lxml")
atag = soup.a
print(atag)


