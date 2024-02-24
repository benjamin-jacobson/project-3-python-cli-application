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