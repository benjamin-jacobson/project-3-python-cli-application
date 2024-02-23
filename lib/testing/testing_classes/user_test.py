
# import sys
import runpy
from os import path

class TestUser:
    '''testing lib/user.py'''

    def test_user_py_exists(self):
        assert(path.exists("lib/classes/user.py"))

    def test_app_py_runs(self):
        runpy.run_path("lib/classes/user.py")