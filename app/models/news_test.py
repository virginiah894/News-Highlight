import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test to implement news behavior
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(12,'today','politics','English','https://image.tmdb.org/t/p/w500/khsjha27hbs','Leadership',url)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news News))


if __name__ == '__main__':
    unittest.main()
