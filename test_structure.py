import unittest

import structure

class StructureTestCase(unittest.TestCase):
    def setUp(self):
        self.struc = structure.LivrelStructure()
    
    def tearDown(self):
        pass
        #print('Nettoyage !')
 
    def test_get_text_directory(self):
        element = self.struc.get_text_directory()
        self.assertEqual(element, 'dist\\alexandre-dumas_les-trois-mousquetaires\\OPS\\text')
    
    def test_get_css_directory(self):
        element = self.struc.get_css_directory()
        self.assertEqual(element, 'dist\\alexandre-dumas_les-trois-mousquetaires\\OPS\\css')
    
    def test_get_images_directory(self):
        element = self.struc.get_images_directory()
        self.assertEqual(element, 'dist\\alexandre-dumas_les-trois-mousquetaires\\OPS\\images')
 

if __name__ == '__main__':
    unittest.main()