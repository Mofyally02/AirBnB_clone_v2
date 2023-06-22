<<<<<<< HEAD
#!/usr/bin/python3
"""BaseModel Test Module"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import MySQLdb

STORAGE_TYPE = os.environ.get("HBNB_TYPE_STORAGE")


class test_basemodel(unittest.TestCase):
    """BaseModel test class."""

    def __init__(self, *args, **kwargs):
        """Initialize test_basemodel"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    @staticmethod
    def _create_db_connection():
        """create a new database connection"""
        options = {
            "host": os.environ.get("HBNB_MYSQL_HOST"),
            "user": os.environ.get("HBNB_MYSQL_USER"),
            "password": os.environ.get("HBNB_MYSQL_PWD"),
            "database": os.environ.get("HBNB_MYSQL_DB"),
        }
        return MySQLdb.connect(**options)

    def tearDown(self):
        """Remove file"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test type of instance"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test initialization with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test that an int key raises error"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(STORAGE_TYPE == "db", "Testing for database storage")
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test the str method"""
        i = self.value()
        i_dict = i.__dict__.copy()
        if "_sa_instance_state" in i_dict.keys():
            del i_dict["_sa_instance_state"]
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i_dict))

    def test_todict(self):
        """test the to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test kwargs key: value is None"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """Test id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test created_at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test updated_at"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    @unittest.skipIf(STORAGE_TYPE == "db", "Testing for file storage")
    def test_delete_method(self):
        """Test delete method"""

        new = self.value()
        new.save()
        key = self.name + "." + new.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], new.to_dict())

        new.delete()
        with open('file.json', 'r') as f:
            j = json.load(f)
            with self.assertRaises(KeyError):
                j[key]
=======
#!/usr/bin/python3
"""test for BaseModel"""
import unittest
import os
from os import getenv
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """this will test the base model class"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.base

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """chekcing if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """test if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_BaesModel(self):
        """test if the save works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """test if dictionary works"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
>>>>>>> 181945a9fa091810aa8f79eca1a4ca9e61bb6afd
