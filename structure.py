import os

import utils

class LivrelStructure:

    def __init__(self, config_path='book.yaml', debug=False):

        self.data = utils.load_conf(config_path, debug=debug)
        self.book_directory_name = '{}_{}'.format(self.data['author'].lower().replace(' ', '-'), 
                                                  self.data['title'].lower().replace(' ', '-'))
        
        if self.data['directory_path'] is not None:
            self.directory_path = os.path.join(self.data['directory_path'], self.book_directory_name)
        else:
            self.directory_path = os.path.join('dist', self.book_directory_name)

        self.frontmatter = []
        self.bodymatter = []
        self.backmatter = []

    def get_text_directory(self):
        return os.path.join(self.directory_path, 'OPS', 'text')

    def get_css_directory(self):
        return os.path.join(self.directory_path, 'OPS', 'css')

    def get_images_directory(self):
        return os.path.join(self.directory_path, 'OPS', 'images')

    def generate_directories(self):
        """
        generate_directories
        """
        print('_____ Directories generation _____')
    
        filepaths = [
            self.directory_path,
            os.path.join(self.directory_path, 'OPS'),
            self.get_text_directory(),
            self.get_images_directory(),
            self.get_css_directory()
        ]

        for filepath in filepaths:
            try:
                os.mkdir(filepath)
                print('Directory {} created'.format(filepath))
            except FileExistsError as error:
                print('Directory {} already exists'.format(filepath))

        print('----------------------------------')

#struc = LivrelStructure()
#struc.generate_directories()

