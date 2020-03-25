# Importamos nosso app
from app import app

# Importamos a biblioteca de testes
import unittest


class TestHomeView(unittest.TestCase):

    '''
      Teste na home
    '''
    

    def setUp(self):
        my_app = app.test_client()
        self.response = my_app.get('/')
        with self.app.app_context():
            # create all tables
            db.create_all()

    # Testando http 200 ok
    def test_get(self):
        self.assertEqual(200, self.response.status_code)


    # Validando a home
    def test_content_type(self):
        self.assert_template_used('interface.html')
        self.assertIn('text/html', self.response.content_type)


class TestPrometheusView(unittest.TestCase):

    '''
      Testa retorno de métricas
    '''

    def setUp(self):
        my_app = app.test_client()
        self.response = my_app.get('/metrics')

    # Testamos se a resposta e 200 ("ok")
    def test_get(self):
        self.assertEqual(200, self.response.status_code)


    def test_content_type(self):
        self.assertIn('text/plain', self.response.content_type)

class TestTopView(unittest.TestCase):

    '''
      Testa retorno de /top
    '''

    def setUp(self):
        my_app = app.test_client()
        self.response = my_app.get('/top')

    # Testamos se a resposta e 200 ("ok")
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('application/json', self.response.content_type)

class TestTotalView(unittest.TestCase):

    '''
      Testa retorno da rota /total
    '''

    def setUp(self):
        my_app = app.test_client()
        self.response = my_app.get('/total')

    # Testamos se a resposta e 200 ("ok")
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('application/json', self.response.content_type)


class TestTweetsView(unittest.TestCase):

    '''
      Testa retorno de /tweets
    '''

    def setUp(self):
        my_app = app.test_client()
        self.response = my_app.get('/tweets')

    # Testamos se a resposta e 200 ("ok")
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('application/json', self.response.content_type)

class TestPopulateView(unittest.TestCase):

    '''
      Testa retorno de /populate
    '''

    def setUp(self):
        my_app = app.test_client()
        self.response = my_app.get('/populate')

    # Testamos se a resposta e 200 ("ok")
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    # Testamos se retona o status de sucesso
    def test_html_string_response(self):
        self.assertEqual('{"status":"success"}', self.response.data.decode('utf-8'))

    def test_content_type(self):
        self.assertIn('application/json', self.response.content_type)

if __name__ == '__main__':
    unittest.main()
