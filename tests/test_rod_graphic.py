import unittest
import sys
from PySide6.QtWidgets import (QGraphicsPolygonItem,
                               QGraphicsEllipseItem, 
                               QApplication)
from utils.rod_graphic import RodGraphic

# to run test use  python -m tests.test_blank_separator  from main directory

class TestRodGraphic(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication(sys.argv)

    def setUp(self):
        self.length = 100
        self.rings = 5
        self.rod = RodGraphic(lenght=self.length, rings=self.rings)

    def test_render_blank_returns_polygon(self):
        blank = self.rod.render_blank()
        self.assertIsInstance(blank, QGraphicsPolygonItem)
        self.assertEqual(blank.polygon().count(), 3)

    def test_render_rings_yields_correct_number(self):
        rings = list(self.rod.render_rings())
        self.assertEqual(len(rings), self.rings)
        for ring in rings:
            self.assertIsInstance(ring, QGraphicsEllipseItem)

    def test_render_graphic_combines_items(self):
        scene = self.rod.render_graphic()
        items = scene.items()
        self.assertEqual(len(items), self.rings + 1)

    def test_render_rings_with_zero_rings(self):
        with self.assertRaises(ValueError):
            RodGraphic(lenght=self.length, rings=0).render_rings()
            
    def test_ring_size_increases_gradually(self):
        rod = RodGraphic(lenght=100, rings=3)
        sizes = []
        for ring in rod.render_rings():
            rect = ring.rect()
            sizes.append(rect.width())
        self.assertGreater(sizes[1], sizes[0])
        self.assertGreater(sizes[2], sizes[1])

    def test_invalid_negative_length(self):
        with self.assertRaises(ValueError):
            RodGraphic(lenght=-100, rings=3).render_graphic()


if __name__ == '__main__':
    unittest.main()
