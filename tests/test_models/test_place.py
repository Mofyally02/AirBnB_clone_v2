<<<<<<< HEAD
#!/usr/bin/python3
"""Place test module"""
import unittest

from tests.test_models.test_base_model import test_basemodel, STORAGE_TYPE
from models.place import Place


class test_Place(test_basemodel):
    """place test class"""

    def __init__(self, *args, **kwargs):
        """Initialize the test class"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test city_id"""
        new = self.value()
        new.city_id = ""
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test user_id"""
        new = self.value()
        new.user_id = ""
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Test name"""
        new = self.value()
        new.name = ""
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Test description"""
        new = self.value()
        new.description = ""
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Test number of rooms"""
        new = self.value()
        new.number_rooms = 3
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Testing number of bathrooms"""
        new = self.value()
        new.number_bathrooms = 3
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Testing max guest"""
        new = self.value()
        new.max_guest = 3
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Test price by night"""
        new = self.value()
        new.price_by_night = 300
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Test latitude"""
        new = self.value()
        new.latitude = 10.90
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Test longitude"""
        new = self.value()
        new.longitude = 45.55
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """Test amenity IDs"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    @unittest.skipUnless(STORAGE_TYPE == "db", "Testing for file storage")
    def test_save(self):
        """ Testing save """

        from tests.test_models.defaults import DefaultInstances

        DEFAULTS = DefaultInstances()

        i = self.value(
            city_id=DEFAULTS.city_id, user_id=DEFAULTS.user_id,
            name="Test save",
            number_rooms=3, number_bathrooms=3,
            max_guest=4, price_by_night=300
            )
        i.save()
        conn = self._create_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM places WHERE id = %s", (i.id,))
        self.assertTrue(cur.fetchone())
        cur.close()
        conn.close()

    @unittest.skipUnless(STORAGE_TYPE == "db", "Testing for file storage")
    def test_place_review_relationship(self):
        """Test the relationship between place and reviews works properly"""
        from tests.test_models.defaults import DefaultInstances
        from models.review import Review

        DEFAULTS = DefaultInstances()

        new_place = Place(
            city_id=DEFAULTS.city_id, user_id=DEFAULTS.user_id,
            name="Place-Review",
            number_rooms=3, number_bathrooms=3,
            max_guest=4, price_by_night=300
        )
        new_review = Review(
            user_id=DEFAULTS.user_id,
            text="Review-Place",
            place_id=new_place.id
        )
        new_place.save()
        new_review.save()

        self.assertTrue(new_place.reviews[0] is new_review)
        self.assertTrue(new_place is new_review.place)

    @unittest.skipUnless(STORAGE_TYPE == "db", "Testing for file storage")
    def test_place_amenity_relationship(self):
        """Test the relationship between place and amenities works properly"""
        from tests.test_models.defaults import DefaultInstances
        from models.amenity import Amenity

        DEFAULTS = DefaultInstances()

        new_place = Place(
            city_id=DEFAULTS.city_id, user_id=DEFAULTS.user_id,
            name="Place-Amenity",
            number_rooms=3, number_bathrooms=3,
            max_guest=4, price_by_night=300
        )
        new_amenity = Amenity(name="Amenity-Review")

        new_place.amenities = [new_amenity]
        new_place.save()
        new_amenity.save()

        self.assertTrue(new_place.amenities[0] is new_amenity)
        self.assertTrue(new_place is new_amenity.place_amenities[0])

        # Test that the place_amenity table was updated.
        conn = self._create_db_connection()
        cur = conn.cursor()
        cur.execute("""SELECT place_id FROM place_amenity
            WHERE amenity_id = %s""", (new_amenity.id,))
        self.assertEqual(cur.fetchone()[0], new_place.id)

        cur.close()
        conn.close()
=======
#!/usr/bin/python3
"""test for place"""
import unittest
import os
from os import getenv
from models.place import Place
from models.base_model import BaseModel
import pep8


class TestPlace(unittest.TestCase):
    """this will test the place class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.place = Place()
        cls.place.city_id = "1234-abcd"
        cls.place.user_id = "4321-dcba"
        cls.place.name = "Death Star"
        cls.place.description = "UNLIMITED POWER!!!!!"
        cls.place.number_rooms = 1000000
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 607360
        cls.place.price_by_night = 10
        cls.place.latitude = 160.0
        cls.place.longitude = 120.0
        cls.place.amenity_ids = ["1324-lksdjkl"]

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.place

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Place(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Place(self):
        """checking for docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes_Place(self):
        """chekcing if amenity have attributes"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_is_subclass_Place(self):
        """test if Place is subclass of Basemodel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_attribute_types_Place(self):
        """test attribute type for Place"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_Place(self):
        """test if the save works"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict_Place(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
>>>>>>> 181945a9fa091810aa8f79eca1a4ca9e61bb6afd
