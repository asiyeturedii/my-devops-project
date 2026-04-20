import unittest
from app.py import app # app.py dosyamızdaki uygulamayı çağırıyoruz

class FlaskTest(unittest.TestCase):

    # Uygulama başladığında ana sayfa 200 (OK) dönüyor mu?
    def test_home_status_code(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    # Ekranda doğru yazı yazıyor mu?
    def test_home_data(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertTrue(b"DevOps Projesine Hos Geldin!" in response.data)

if __name__ == '__main__':
    unittest.main()