import unittest

class LivingSpaceTest(unittest.TestCase):
    def setUp(self):
        self.living_space = LivingSpace("Black")

    def testLivingSpaceHasMaxNum4(self):
        self.assertEqual(self.living_space.max_num, 4)

    def testLivingSpaceHasNameAttribute(self):
        self.assertEqual(self.living_space.name, "Black")

if __name__ == "__main__":
	unittest.main()