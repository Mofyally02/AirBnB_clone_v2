<<<<<<< HEAD
#!/usr/bin/python3
"""State Test module"""
import unittest
from datetime import datetime

from tests.test_models.test_base_model import test_basemodel, STORAGE_TYPE
from models.state import State


class test_state(test_basemodel):
    """Class for testing State objects"""

    def __init__(self, *args, **kwargs):
        """Initialize a test instance"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test name"""
        new = self.value()
        new.name = ""
        self.assertTrue(isinstance(new.name, str))

    @unittest.skipUnless(STORAGE_TYPE == "db", "Testing for file storage")
    def test_save(self):
        """ Testing save """
        i = self.value(name="Save")
        i.save()
        conn = self._create_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM states WHERE id = %s", (i.id,))
        self.assertTrue(cur.fetchone())
        cur.close()
        conn.close()

    @unittest.skipUnless(STORAGE_TYPE == "db", "Testing for file storage")
    def test_state_city_relationship(self):
        """Test that the relationship between state and cities works as
        expected"""
        from models.city import City

        new_state = self.value(name="State-Cities")
        new_city = City(name="City-State", state_id=new_state.id)
        new_state.save()
        new_city.save()

        self.assertTrue(new_city is new_state.cities[0])
        self.assertTrue(new_state is new_city.state)

    @unittest.skipIf(STORAGE_TYPE == "db", "Testing for file storage")
    def test_cities_getter(self):
        """Test that the cities getter returns a list of cities with
        state_id equal to state.id"""
        from models.city import City

        new_state = State()
        new_city = City(state_id=new_state.id,
                        created_at=datetime.now().isoformat(),
                        updated_at=datetime.now().isoformat())
        new_state.save()
        new_city.save()

        self.assertTrue(new_city is new_state.cities[0])
        with self.assertRaises(AttributeError):
            new_city.state
=======
#!/usr/bin/python3
"""test for state"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """this will test the State class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.state

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_State(self):
        """checking for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes_State(self):
        """chekcing if State have attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_State(self):
        """test if State is subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_State(self):
        """test attribute type for State"""
        self.assertEqual(type(self.state.name), str)

    def test_save_State(self):
        """test if the save works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
>>>>>>> 181945a9fa091810aa8f79eca1a4ca9e61bb6afd
