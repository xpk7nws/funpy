import unittest
from toy1.package.person import Person


class MyTestCase(unittest.TestCase):
    def test_person_with_int_age_is_equal(self):
        test_age = 10
        test_person = Person("me", test_age)
        self.assertEqual(test_person.age, test_age)

    def test_person_with_string_age_is_equal(self):
        test_person = Person("me", "foo")
        self.assertEqual(test_person.age, test_person.get_no_age())

    def test_person_with_empty_name_is_equal(self):
        test_age = 10
        test_person = Person("", test_age)
        self.assertEqual(test_person.name, test_person.get_no_name())

    def test_person_string_equal(self):
        person_name = "foo"
        person_age = 9
        test_person = Person(person_name, person_age)
        self.assertTrue(person_name in str(test_person))
        self.assertTrue(str(person_age) in str(test_person))


if __name__ == '__main__':
    unittest.main()
