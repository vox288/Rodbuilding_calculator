import unittest
from PySide6.QtWidgets import QApplication
import sys

from main import Main_Window

# to run test use  python -m tests.test_main  from main directory

class TestMainWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.window = Main_Window()
        self.window.show()

    def tearDown(self):
        self.window.close()

    def test_initial_state(self):
        self.assertEqual(self.window.lenght_is_set, 1.0)
        self.assertEqual(self.window.rings_are_set, 1.0)
        self.assertEqual(self.window.modifier, 0.1)

    def test_get_ringcount(self):
        self.window.dial_ringcount.setValue(3)
        self.window._get_ringcount()
        self.assertEqual(self.window.rings_are_set, 3)
        self.assertEqual(self.window.label_output_ringcount.text(), "3 Rings")

    def test_get_rodlenght(self):
        self.window.dial_rodlenght.setValue(150)
        self.assertEqual(self.window.lenght_is_set, 150)
        self.assertEqual(self.window.label_output_rodlenght.text(), "150 cm")

    def test_get_modifier(self):
        self.window.slider_modifier.setValue(6)
        self.assertAlmostEqual(self.window.modifier, 0.06)
        self.assertEqual(self.window.label_modifier.text(), "6")


if __name__ == "__main__":
    unittest.main()