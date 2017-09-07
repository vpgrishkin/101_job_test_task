import unittest

from fetch_page_no_style import remove_style


class TestRemoveStyleFunction(unittest.TestCase):
    def test_remove_style_in_single_quotes(self):
        self.assertEqual(remove_style('''
            <body>
              <p style='font-size: 12pt'>Example</p>
            </body>
            '''),
            '''
            <body>
              <p>Example</p>
            </body>
            ''')
    def test_remove_style_in_double_quotes(self):
        self.assertEqual(remove_style('''
            <body>
              <p style="font-size: 12pt">Example</p>
            </body>
            '''),
            '''
            <body>
              <p>Example</p>
            </body>
            ''')


if __name__ == "__main__":
    unittest.main()