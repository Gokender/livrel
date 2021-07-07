from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup
import roman
import os

def generate_chapter(part_id, chapter_id, filepath, with_part):
    """
    Generate chapter
    """

    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)

    if with_part:
        template = env.get_template('part_chapter.xhtml')
    else:
        template = env.get_template('chapter.xhtml')
    
    if chapter_id == 1:
        chapter_id_roman = 'Premier'
    else:
        chapter_id_roman = roman.toRoman(chapter_id)

    title = '{} - {}'.format(roman.toRoman(chapter_id), 'test_title')

    output = template.render(title=title,
                             part_id=part_id,
                             chapter_id=chapter_id,
                             chapter_id_roman=chapter_id_roman,
                             chapter_title='test_title')

    #filename = 'alexandre-dumas_les-trois-mousquetaires\chapter_1_1.xhtml'
    print('    - {}'.format(filepath))

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(output)




for key,value in data['bodymatter'].items():
    if value is not None:
        print(key,value)




print('_____ Generation of the bodymatter _____')
if data['bodymatter']['part'] is not None: #TODO: DELETE

    if data['bodymatter']['part'] != len(data['bodymatter']['chapter']):
        print('ERROR')

    for part_id in range(data['bodymatter']['part']):

        nb_part = data['bodymatter']['part']

        for chapter_id in range(data['bodymatter']['chapter'][part_id]):
            
            nb_chapter = data['bodymatter']['chapter'][part_id]

            filename = 'chapter_{}_{}.xhtml'.format(str(part_id+1).zfill(len(str(part_id))), str(chapter_id+1).zfill(len(str(nb_chapter))))
            filepath = os.path.join('dist', book_directory_name, filename)

            if data['bodymatter']['part'] == 1:
                with_part = False
            else:
                with_part= True
            
            generate_chapter(part_id+1, chapter_id+1, filepath, with_part)