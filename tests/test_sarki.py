import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.modules.sarki import Sarki

class TestSarki(unittest.TestCase):
    def test_sarki_olusturma(self):
        # Sarki nesnesinin doğru oluşup oluşmadığını test ediyoruz
        yeni_sarki = Sarki("Deneme Şarkı", "deneme.mp3")
        self.assertEqual(yeni_sarki.isim, "Deneme Şarkı")
        self.assertEqual(yeni_sarki.bilgileri_getir(), "Şu An Çalan: Deneme Şarkı")

if __name__ == '__main__':
    unittest.main()
