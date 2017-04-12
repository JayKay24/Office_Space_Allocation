import unittest

class AllocateRandomPeopleToRandomOffices(unittest.TestCase):
    def setUp(self):
        create_office("Flash")
        create_office("Zoom")
        create_person("James", "Kinyua", "fellow")
        create_person("Doris", "Njihia", "fellow")


    def testPerson1OfficeNotEqualToPerson2Office(self):
        office_1 = fellows[0].office_name
        office_2 = fellows[1].office_name

if __name__ == "__main__":
	unittest.main()