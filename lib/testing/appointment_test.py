import os
import sys
import runpy
import pytest
from os import path

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from classes.user import User
from classes.vendor import Vendor
from classes.appointments import Appointment

class TestAppointment:
    '''testing lib/appointment.py'''

    def test_appointment_py_exists(self):
        assert(path.exists("lib/classes/appointments.py"))

    def test_app_py_runs(self):
        runpy.run_path("lib/classes/appointments.py")

    def test_initialized_appointment(self):
        '''Appointment is initialized'''
        User.drop_table()
        User.create_table()
        user_1 = User("Roberto",12)

        Vendor.drop_table()
        Vendor.create_table()
        vendor_1 = Vendor.create("Twitter", 12)

        apt_1 = Appointment.create(user_1, vendor_1, "in person", 2024) # user, vendor, appointment_type, appointment_year
        assert ((apt_1.user,apt_1.vendor,apt_1.appointment_type,apt_1.appointment_year)==(user_1,vendor_1,"in person",2024))

    
    def test_initialized_appointment_and_table_insert(self):
        '''Appointment is initialized'''
        User.drop_table()
        User.create_table()
        user_1 = User("Roberto",12)

        Vendor.drop_table()
        Vendor.create_table()
        vendor_1 = Vendor.create("Twitter", 12)

        Appointment.drop_table()
        Appointment.create_table()

        apt_1 = Appointment.create(user_1, vendor_1, "in person", 2024) # user, vendor, appointment_type, appointment_year
        assert ((apt_1.user, apt_1.vendor, apt_1.appointment_type ,apt_1.appointment_year)==(user_1,vendor_1,"in person",2024))

