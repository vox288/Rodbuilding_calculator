import unittest
from utils.blank_separator import BlankSeparator

# to run test use  python -m tests.test_blank_separator  from main directory

class TestBlankSeparator(unittest.TestCase):

    def setUp(self):
        self.rod = BlankSeparator(210, 7)
        print("normal setup")

    def test_calc_reelseat(self):
        self.assertEqual(self.rod.calc_reel_seat(), 31.29)

    def test_calc_start_ring(self):
        self.assertEqual(self.rod.calc_start_ring(), 50.4)
    
    def test_calc_ringed_section(self):
        self.assertEqual(self.rod.calc_ringed_section(), 128.31)
    
    def test_calc_ring_positions(self):
        calculated = self.rod.calc_ring_positions().values()
        expected = {2: 11.59, 3: 15.74, 4: 21.39, 5: 29.05, 6: 39.46, 7: 53.6}.values()
        generator = (item for item in expected)
        for val in calculated:
            self.assertAlmostEqual(val, next(generator), 1)

    def test_scale_ring_positions(self):
        calculated = self.rod.scale_ring_positions().values()
        expected = {
            ('Ring', 1): 0.0, ('Ring', 2): 8.71, ('Ring', 3): 11.82,
            ('Ring', 4): 16.07, ('Ring', 5): 21.82, ('Ring', 6): 29.64,
            ('Ring', 7): 40.26
                    }.values()
        generator = (item for item in expected)
        for val in calculated:
            self.assertAlmostEqual(val, next(generator), 1)


class TestBlankBeparator_A(unittest.TestCase):

    def setUp(self):
        self.rod = BlankSeparator(-210, 7)
        print("setup A: ValueError checking the lenght")

    def test_calc_reelseat_A(self):
        with self.assertRaises(ValueError):
             self.rod.calc_reel_seat()

    def test_calc_start_ring_A(self):
        with self.assertRaises(ValueError):
             self.rod.calc_start_ring()

    def test_calc_ringed_section_A(self):
        with self.assertRaises(ValueError):
             self.rod.calc_ringed_section()

    def test_calc_ring_positions_A(self):
        with self.assertRaises(ValueError):
             self.rod.calc_ring_positions()

    def test_scale_ring_positions_A(self):
        with self.assertRaises(ValueError):
             self.rod.scale_ring_positions()


class TestBlankSeparator_B(unittest.TestCase):

    def setUp(self):
        self.rod = BlankSeparator(0, 7)
        print("setup B: ValueError edgecase the lenght")

    def test_calc_reelseat_B(self):
        with self.assertRaises(ValueError):
             self.rod.calc_reel_seat()

    def test_calc_start_ring_B(self):
        with self.assertRaises(ValueError):
             self.rod.calc_start_ring()

    def test_calc_ringed_section_B(self):
        with self.assertRaises(ValueError):
             self.rod.calc_ringed_section()

    def test_calc_ring_positions_B(self):
        with self.assertRaises(ValueError):
             self.rod.calc_ring_positions()

    def test_scale_ring_positions_B(self):
        with self.assertRaises(ValueError):
             self.rod.scale_ring_positions()


class TestBlankSeparator_C(unittest.TestCase):

    def setUp(self):
        self.rod = BlankSeparator(None, 7)
        print("setup C: TypeError checking the lenght")

    def test_calc_reelseat_C(self):
        with self.assertRaises(TypeError):
             self.rod.calc_reel_seat()

    def test_calc_start_ring_C(self):
        with self.assertRaises(TypeError):
             self.rod.calc_start_ring()

    def test_calc_ringed_section_C(self):
        with self.assertRaises(TypeError):
             self.rod.calc_ringed_section()

    def test_calc_ring_positions_C(self):
        with self.assertRaises(TypeError):
             self.rod.calc_ring_positions()

    def test_scale_ring_positions_C(self):
        with self.assertRaises(TypeError):
             self.rod.scale_ring_positions()


class TestBlankSeparator_D(unittest.TestCase):

    def setUp(self):
        self.rod = BlankSeparator(210, 1)
        print("setup D: ValueError checking the rings")

    def test_calc_ring_positions_D(self):
        with self.assertRaises(ValueError):
             self.rod.calc_ring_positions()

    def test_scale_ring_positions_D(self):
        with self.assertRaises(ValueError):
             self.rod.scale_ring_positions()


class TestBlankSeparator_E(unittest.TestCase):

    def setUp(self):
        self.rod = BlankSeparator(210, None)
        print("setup E: TypeError checking the rings")

    def test_calc_ring_positions_E(self):
        with self.assertRaises(TypeError):
             self.rod.calc_ring_positions()

    def test_scale_ring_positions_E(self):
        with self.assertRaises(TypeError):
             self.rod.scale_ring_positions()


class TestBlankSeparator_F(unittest.TestCase):
    
    def setUp(self):
        self.rod = BlankSeparator(210, 7, None)
        print("setup F: TypeError checking the modifier")

    def test_calc_ring_positions_F(self):
        with self.assertRaises(TypeError):
             self.rod.calc_ring_positions()

    def test_scale_ring_positions_F(self):
        with self.assertRaises(TypeError):
             self.rod.scale_ring_positions()


class TestBlankSeparator_G(unittest.TestCase):
    
    def setUp(self):
        self.rod = BlankSeparator(210, 7, 0.01)
        print("setup G: ValueError checking the modifier")

    def test_calc_ring_positions_G(self):
        with self.assertRaises(ValueError):
             self.rod.calc_ring_positions()

    def test_scale_ring_positions_G(self):
        with self.assertRaises(ValueError):
             self.rod.scale_ring_positions()


if __name__ == "__main__":
    unittest.main()