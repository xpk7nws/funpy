import unittest
from toy1.package.person import Person


class MyTestCase(unittest.TestCase):
    TEST_NAME = "foo"
    TEST_AGE = 10

    # age is an integer
    def test_person_with_int_age_is_equal(self):
        test_person = Person(MyTestCase.TEST_NAME, MyTestCase.TEST_AGE)
        self.assertEqual(test_person.age, MyTestCase.TEST_AGE)

    # age is None
    def test_person_with_none_age_is_no_age(self):
        test_person = Person(MyTestCase.TEST_NAME, None)
        self.assertEqual(test_person.age, test_person.get_no_age())

    # age is a string (or is it called a literal?)
    def test_person_with_string_age_is_no_age(self):
        test_person = Person(MyTestCase.TEST_NAME, "foo")
        self.assertEqual(test_person.age, test_person.get_no_age())

    # name is a regular string or literal
    def test_person_with_value_name_is_no_name(self):
        test_person = Person(MyTestCase.TEST_NAME, MyTestCase.TEST_NAME)
        self.assertEqual(test_person.name, MyTestCase.TEST_NAME)

    # name is None
    def test_person_with_none_name_is_no_name(self):
        test_person = Person(None, MyTestCase.TEST_AGE)
        self.assertEqual(test_person.name, test_person.get_no_name())

    # name is empty
    def test_person_with_empty_name_is_no_name(self):
        test_person = Person("", MyTestCase.TEST_AGE)
        self.assertEqual(test_person.name, test_person.get_no_name())

    # testing that Person::str has both the name and age when valid
    def test_person_str_is_equal(self):
        test_person = Person(MyTestCase.TEST_NAME, MyTestCase.TEST_AGE)
        # name and age are in the resulting str()
        self.assertTrue(MyTestCase.TEST_NAME in str(test_person))
        self.assertTrue(str(MyTestCase.TEST_AGE) in str(test_person))


if __name__ == '__main__':
    unittest.main()
