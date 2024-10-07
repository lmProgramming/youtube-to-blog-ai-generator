import re
import unittest

class TestBlogGeneration(unittest.TestCase):
    def setUp(self):
        self.generated_blog = '''
        #Title: The Case for Legalizing Cannabis: A Closer Look at Vice President Harris's Stance

        #Content:
        In a recent discussion...
        '''

    def test_extract_title_and_content(self):
        title_match = re.search(r"#Title:\s*(.*)", self.generated_blog)
        content_match = re.search(r"#Content:\s*(.*)", self.generated_blog, re.DOTALL)

        title = title_match.group(1).strip()
        content = content_match.group(1).strip()
        
        self.assertEqual(title, 'The Case for Legalizing Cannabis: A Closer Look at Vice President Harris\'s Stance')
        self.assertEqual(content, 'In a recent discussion...')

if __name__ == '__main__':
    unittest.main()