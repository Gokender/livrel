from bs4 import BeautifulSoup
import re

def fix_ampersand(data_input):
    return re.sub('&amp;',  '&', str(data_input))

def fix_exclamation(data_input):
    data_input = re.sub(' !',  '&#8239;!', data_input)
    return data_input

with open('raw_format.xhtml', 'r') as infile:
    html_doc = infile.read()

soup = BeautifulSoup(html_doc, 'html.parser')
paragraphs = soup.find_all('p')

for para in paragraphs:
    #print(para)
    para.string = fix_exclamation(para.text)#str(re.sub(' !',  '&#8239;!', para.text))
    #para.string.replace_with(v.string.replace(' !','&#8239;!'))
    #print(v)

soup_fixed = fix_ampersand(soup)

with open("output2.xhtml", "w", encoding='utf-8') as file:
    file.write(str(soup_fixed))