import os
import sys
import runpy
import pytest
from os import path

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from classes.vendor import Vendor

class TestVendor:
    '''testing lib/vendor.py'''

    def test_vendor_py_exists(self):
        assert(path.exists("lib/classes/vendor.py"))

    def test_app_py_runs(self):
        runpy.run_path("lib/classes/vendor.py")

    def test_has_vendor(self):
        vendor_1 = Vendor("Twitter",12)

        assert vendor_1.name == "Twitter"
        assert vendor_1.type_id == 12
        
        # Testing that an exception is raise when <2 chars per property
        with pytest.raises(Exception):
            Vendor("",12)
    
    def test_update(self):
        Vendor.drop_table()
        Vendor.create_table()
        vendor_1 = Vendor.create("Twitter", 12)
        vendor_2 = Vendor.create("Ebay", 12)
        vendor_1_new_name = "X"

        vendor_1.name = vendor_1_new_name
        vendor_1.update()

        assert((vendor_1.name,vendor_1.type_id)==(vendor_1_new_name, 12))
        assert((vendor_2.name,vendor_2.type_id)==("Ebay", 12))

    def test_find_by_id(self):
        Vendor.drop_table()
        Vendor.create_table()
        vendor_1 = Vendor.create("Twitter", 12)
        vendor_2 = Vendor.create("Ebay", 12)


        u = Vendor.find_by_id(vendor_1.id)
        assert((u.id, u.name,u.type_id)==(1,"Twitter", 12))


    def test_find_by_name(self):
        Vendor.drop_table()
        Vendor.create_table()
        vendor_1 = Vendor.create("Twitter", 12)
        vendor_2 = Vendor.create("Ebay", 12)


        u = Vendor.find_by_name(vendor_1.name)
        assert((u.id, u.name,u.type_id)==(1,"Twitter", 12))