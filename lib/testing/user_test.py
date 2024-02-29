import os
import sys
import runpy
import pytest
from os import path

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from classes.user import User

class TestUser:
    '''testing lib/user.py'''

    def test_user_py_exists(self):
        assert(path.exists("lib/classes/user.py"))

    def test_app_py_runs(self):
        runpy.run_path("lib/classes/user.py")

    def test_has_username(self):
        user_1 = User("Roberto",12)

        assert user_1.username == "Roberto"
        assert user_1.cohort_id == 12
        
        # Testing that an exception is raise when <4 chars per property
        with pytest.raises(Exception):
            User("Ro",12)
    
    def test_update(self):
        User.drop_table()
        User.create_table()
        user_1 = User.create("Joeyy", 12)
        user_2 = User.create("Mikey", 12)
        user_1_new_name = "blahblah"

        user_1.username = user_1_new_name
        user_1.update()

        assert((user_1.username,user_1.cohort_id)==(user_1_new_name, 12))
        assert((user_2.username,user_2.cohort_id)==("Mikey", 12))

    def test_find_by_id(self):
        User.drop_table()
        User.create_table()
        user_1 = User.create("Joeyy", 12)
        user_2 = User.create("Mikey", 12)


        u = User.find_by_id(user_1.id)
        assert((u.id, u.username,u.cohort_id)==(1,"Joeyy", 12))


    def test_find_by_username(self):
        User.drop_table()
        User.create_table()
        user_1 = User.create("Joeyy", 12)
        user_2 = User.create("Mikey", 12)


        u = User.find_by_username(user_1.username)
        assert((u.id, u.username,u.cohort_id)==(1,"Joeyy", 12))