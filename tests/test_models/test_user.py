<<<<<<< HEAD
#!/usr/bin/python3
"""User test module"""
import unittest

from tests.test_models.test_base_model import test_basemodel, STORAGE_TYPE
from models.user import User


class test_User(test_basemodel):
    """Class for test User class"""

    def __init__(self, *args, **kwargs):
        """Initialize new test instance."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test first name"""
        new = self.value()
        new.first_name = ""
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test last name"""
        new = self.value()
        new.last_name = ""
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test email"""
        new = self.value()
        new.email = "test@example.com"
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test password"""
        new = self.value()
        new.password = ""
        self.assertEqual(type(new.password), str)

    @unittest.skipUnless(STORAGE_TYPE == "db", "Testing for file storage")
    def test_save(self):
        """ Testing save """
        new_user = self.value(
            email="test@example.com",
            password="testing save"
        )
        new_user.save()
        conn = self._create_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (new_user.id,))
        self.assertTrue(cur.fetchone())
        cur.close()
        conn.close()

    @unittest.skipUnless(STORAGE_TYPE == "db", "Testing for file storage")
    def test_user_place_relationship(self):
        """Test that the relationship between user and place works properly"""
        from models.place import Place
        from tests.test_models.defaults import DefaultInstances

        DEFAULTS = DefaultInstances()

        new_user = User(email="User-Place", password="password")
        new_place = Place(
            city_id=DEFAULTS.city_id, user_id=new_user.id,
            name="Place-User",
            number_rooms=3, number_bathrooms=3,
            max_guest=4, price_by_night=300
        )
        new_user.save()
        new_place.save()

        self.assertTrue(new_user.places[0] is new_place)
        self.assertTrue(new_place.user is new_user)

    @unittest.skipUnless(STORAGE_TYPE == "db", "Testing for file storage")
    def test_user_review_relationship(self):
        """Test that the relationship between user and review works properly"""
        from models.review import Review
        from tests.test_models.defaults import DefaultInstances

        DEFAULTS = DefaultInstances()

        new_user = User(email="User-Review", password="password")
        new_review = Review(
            place_id=DEFAULTS.place_id, user_id=new_user.id,
            text="Review-User",
        )
        new_user.save()
        new_review.save()

        self.assertTrue(new_user.reviews[0] is new_review)
        self.assertTrue(new_review.user is new_user)
=======
#!/usr/bin/python3
"""test for user"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """this will test the User class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kevin"
        cls.user.last_name = "Yook"
        cls.user.email = "yook00627@gmamil.com"
        cls.user.password = "secret"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_User(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_User(self):
        """checking for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes_User(self):
        """chekcing if User have attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass_User(self):
        """test if User is subclass of Basemodel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types_User(self):
        """test attribute type for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save_User(self):
        """test if the save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_User(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
>>>>>>> 181945a9fa091810aa8f79eca1a4ca9e61bb6afd
