import yaml
from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup
import roman

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

"""with open('book.yaml') as infile:
    data = yaml.load(infile, Loader=yaml.FullLoader)

for key,value in data['frontmatter'].items():
    if value is not None:
        filename = '{}'
        print('')"""

def generate_bodymatter(type, page_number):

    template = env.get_template('chapter.xhtml')
    output = template.render(title='test', chapter_no=roman.toRoman(page_number))
    #print(output)
    soup = BeautifulSoup(output, 'html.parser')

    filename = 'test_book\\chapter_{}.xhtml'.format(page_number)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify()))

generate_bodymatter('chapter', 1)
#print(data)