from bs4 import BeautifulSoup

with open('3_mousquetaires.html', 'r') as infile:
    html_doc = infile.read()

soup = BeautifulSoup(html_doc, 'html.parser')

sections = soup.find_all('section', attrs={'data-mw-section-id':'-1'})

links_chapter = sections[2].find_all('a')
print(len(links_chapter))

for link_chapter in links_chapter:
    id_chapter = link_chapter.get('href').lstrip('#')
    #print(id_chapter)

    chapter_content = soup.find_all('div', attrs={'id':id_chapter})
    #print(chapter_content)
    #print(len(chapter_content))
    #chapter = chapter_content.find('section', attrs={'data-mw-section-id':'-2'})

    #print(chapter)

chapter_content = soup.find('div', attrs={'id':'calibre_link-55'})
print(chapter_content)