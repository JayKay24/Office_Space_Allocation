import unittest

class LivingSpaceTest(unittest.TestCase):
    def setUp(self):
        self.living_space = LivingSpace("Black")

    def testLivingSpaceHasMaxNum4(self):
        self.assertEqual(self.living_space.max_num, 4)

    def testLivingSpaceHasNameAttribute(self):
        self.assertEqual(self.living_space.name, "Black")

class CreateLivingSpaceTests(unittest.TestCase):
    def setUp(self):
        self.name = "Red"

    def testCreateLivingSpace(self):
        self.living_space = create_living_space(self.name)
        self.assertEqual(self.living_space.name, "Red")

if __name__ == "__main__":
	unittest.main()