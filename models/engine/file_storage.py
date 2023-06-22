#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
<<<<<<< HEAD
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

=======
    """This class manages storage of hbnb models in JSON format"""

    # NB: Better to have two file paths.
    #     One for testing and the other for development so as not to
    #     lose data when testing as it overwrites existing file.
>>>>>>> 1512bbc73944390258cdb9d8055800254a97323e
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
<<<<<<< HEAD
        """Return a dictionary of instantiated objects in __objects.

        If a cls is specified, returns a dictionary of objects of that type.
        Otherwise, returns the __objects dictionary.
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
=======
        """Returns a dictionary of models currently in storage or of a
        specific class if given.

        Args:
            cls (class): Class to return all models of it. Defaults to None.
        """

        if cls:
            # Getting class objects without dictionary comprehension.
            # cls_objects = {}
            # for key, value in FileStorage.__objects.items():
            #     if isinstance(value, cls):
            #         cls_objects[key] = value
            # return cls_objects

            return {
                key: value
                for key, value in FileStorage.__objects.items()
                if isinstance(value, cls)
            }
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.__class__.__name__ + "." + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
>>>>>>> 1512bbc73944390258cdb9d8055800254a97323e
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
<<<<<<< HEAD
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Call the reload method."""
        self.reload()
=======
        """Deletes obj from __objects if it's inside.

        Args:
            obj (object): Object to delete. Defaults to None.
        """

        if obj and obj in FileStorage.__objects.values():
            key = f"{obj.__class__.__name__}.{obj.id}"
            del FileStorage.__objects[key]
            self.save()
>>>>>>> 1512bbc73944390258cdb9d8055800254a97323e
