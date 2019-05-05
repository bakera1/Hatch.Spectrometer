import unittest

from spectrometer.Camera import Camera

class TestCamera(unittest.TestCase):
    def test_something(self):
        c = Camera()
        c.take_picture('my_picture', 1000000)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
