import unittest

class CreateLivingSpaceTests(unittest.TestCase):
    def setUp(self):
        self.name = "Red"

    def testCreateLivingSpace(self):
        self.living_space = create_living_space(self.name)
        self.assertEqual(self.living_space.name, "Red")

if __name__ == "__main__":
	main()