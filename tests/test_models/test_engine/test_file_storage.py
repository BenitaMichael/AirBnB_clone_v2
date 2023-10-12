#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
# import json
import models
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.dataStorage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.dataStorage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.dataStorage.all(None)

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ct = City()
        am = Amenity()
        rv = Review()
        models.dataStorage.new(bm)
        models.dataStorage.new(us)
        models.dataStorage.new(st)
        models.dataStorage.new(pl)
        models.dataStorage.new(ct)
        models.dataStorage.new(am)
        models.dataStorage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.dataStorage.all().keys())
        self.assertIn(bm, models.dataStorage.all().values())
        self.assertIn("User." + us.id, models.dataStorage.all().keys())
        self.assertIn(us, models.dataStorage.all().values())
        self.assertIn("State." + st.id, models.dataStorage.all().keys())
        self.assertIn(st, models.dataStorage.all().values())
        self.assertIn("Place." + pl.id, models.dataStorage.all().keys())
        self.assertIn(pl, models.dataStorage.all().values())
        self.assertIn("City." + ct.id, models.dataStorage.all().keys())
        self.assertIn(ct, models.dataStorage.all().values())
        self.assertIn("Amenity." + am.id, models.dataStorage.all().keys())
        self.assertIn(am, models.dataStorage.all().values())
        self.assertIn("Review." + rv.id, models.dataStorage.all().keys())
        self.assertIn(rv, models.dataStorage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.dataStorage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.dataStorage.new(None)

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ct = City()
        am = Amenity()
        rv = Review()
        models.dataStorage.new(bm)
        models.dataStorage.new(us)
        models.dataStorage.new(st)
        models.dataStorage.new(pl)
        models.dataStorage.new(ct)
        models.dataStorage.new(am)
        models.dataStorage.new(rv)
        models.dataStorage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + ct.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.dataStorage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        ct = City()
        am = Amenity()
        rv = Review()
        models.dataStorage.new(bm)
        models.dataStorage.new(us)
        models.dataStorage.new(st)
        models.dataStorage.new(pl)
        models.dataStorage.new(ct)
        models.dataStorage.new(am)
        models.dataStorage.new(rv)
        models.dataStorage.save()
        models.dataStorage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + ct.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.dataStorage.reload(None)


if __name__ == "__main__":
    unittest.main()

