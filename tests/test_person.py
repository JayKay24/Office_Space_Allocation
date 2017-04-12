import unittest

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.guy = Person("James", "Kinyua", "Fellow")
        
    def testPersonHasName(self):
        self.assertEqual(self.guy.firstName, "James")

    def testPersonHasStatus(self):
        self.assertEqual(self.guy.status, "Fellow")

if __name__ == "__main__":
	unittest.main()