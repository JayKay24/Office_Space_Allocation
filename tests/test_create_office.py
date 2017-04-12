import unittest

class CreateOfficeTests(unittest.TestCase):
    def setUp(self):
        self.name = "Blue"

    def testCreateOffice(self):
        self.office = create_office(self.name)
        self.assertEqual(self.office.name, "Blue")

if __name__ == "__main__":
	unittest.main()