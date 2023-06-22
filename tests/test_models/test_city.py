<<<<<<< HEAD
#!/usr/bin/python3
"""City Test Module"""
import unittest

from tests.test_models.test_base_model import test_basemodel, STORAGE_TYPE
from models.city import City


class test_City(test_basemodel):
    """City test class"""

    def __init__(self, *args, **kwargs):
        """Initialize the test class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test state_id"""
        new = self.value()
        new.state_id = ""
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test name"""
        new = self.value()
        new.name = ""
        self.assertEqual(type(new.name), str)

    @unittest.skipUnless(STORAGE_TYPE == "db", "Testing for file storage")
    def test_save(self):
        """ Testing save """

        from tests.test_models.defaults import DefaultInstances

        DEFAULTS = DefaultInstances()

        i = self.value(name="test", state_id=DEFAULTS.state_id)
        i.save()
        conn = self._create_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM cities WHERE id = %s", (i.id,))
        self.assertTrue(cur.fetchone())
        cur.close()
        conn.close()

    @unittest.skipUnless(STORAGE_TYPE == "db", "Testing for file storage")
    def test_city_place_relationship(self):
        """Test that the relationship between city and place works properly"""
        from tests.test_models.defaults import DefaultInstances
        from models.place import Place

        DEFAULTS = DefaultInstances()

        new_city = self.value(name="City-Places", state_id=DEFAULTS.state_id)
        new_place = Place(
            city_id=new_city.id, user_id=DEFAULTS.user_id, name="Place-City",
            number_rooms=3, number_bathrooms=3,
            max_guest=4, price_by_night=300
        )
        new_city.save()
        new_place.save()

        self.assertTrue(new_city.places[0] is new_place)
        self.assertTrue(new_city is new_place.cities)
=======
#!/usr/bin/python3
"""test for city"""
import unittest
import os
from os import getenv
from models.city import City
from models.base_model import BaseModel
import pep8


class TestCity(unittest.TestCase):
    """this will test the city class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.city

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """checking for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """chekcing if City have attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """test if City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_City(self):
        """test if the save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
>>>>>>> 181945a9fa091810aa8f79eca1a4ca9e61bb6afd
