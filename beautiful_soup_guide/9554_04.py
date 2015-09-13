#This script contains examples of Navigations methods in Beautiful Soup
from bs4 import BeautifulSoup
from bs4.element import NavigableString
html_markup = """<div class="ecopyramid"><ul id="producers"><li class="producerlist"><div class="name">plants</div><div class="number">100000</div></li><li class="producerlist"><div class="name">algae</div><div class="number">100000</div></li></ul></div>"""

#All producers
soup = BeautifulSoup(html_markup,"lxml")
producer_entries = soup.ul
print(producer_entries)

#first producer

first_producer = producer_entries.li
print(first_producer)

#using .contents

for tag in soup.contents:
	print(tag.name)
	
#.contents for tag object 

for child in producer_entries.contents:
	print(child)

	
#using children

for tag in soup.children:
	print(tag.name)

	
#using descendants


for tag in soup.descendants: 
    if isinstance(tag, NavigableString):
    	print(tag)
    else:
    	print(tag.name)


#using .parents

third_div = soup.find_all("div")[2]
for parent in third_div.parents:
	print(parent.name)
	
	
#using sibling

soup = BeautifulSoup(html_markup,"lxml")
first_producer = soup.find("li")
second_producer = first_producer.next_sibling
second_producer_name = second_producer.div.string
print(second_producer_name)


#previous sibling

print(second_producer.previuos_sibling)


#next element

first_producer = soup.li
print(first_producer.next_element)

#previous element

second_div = soup.find_all("div")[1]
print(second_div.previous_element)
