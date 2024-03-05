import os
import sys
import runpy
import pytest
from os import path

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from classes.user import User
from classes.vendor import Vendor
from classes.appointment import Appointment

class TestAppointment:
    '''testing lib/appointment.py'''

    def test_appointment_py_exists(self):
        assert(path.exists("lib/classes/appointment.py"))

    def test_app_py_runs(self):
        runpy.run_path("lib/classes/appointment.py")

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

    
    def test_initialized_appointment_and_create_user(self):
        '''Appointment is initialized'''
        User.drop_table()
        User.create_table()
        user_1 = User.create("Robertoss",12)
        user_2 = User.create("Michelangelo",124)

        Vendor.drop_table()
        Vendor.create_table()
        vendor_1 = Vendor.create("Twitter", 12)
        vendor_2 = Vendor.create("KensArtisanPizza", 100)

        Appointment.drop_table()
        Appointment.create_table()

        apt_1 = Appointment.create(user_1, vendor_1, "in person", 2024) # user, vendor, appointment_type, appointment_year
        apt_2 = Appointment.create(user_2, vendor_2, "in person", 2023) # user, vendor, appointment_type, appointment_year
        assert ((apt_1.user, apt_1.vendor, apt_1.appointment_type ,apt_1.appointment_year)==(user_1,vendor_1,"in person",2024))

        print(Appointment.get_all_data_in_appointments_database_table())
        print("-----")
        print(Appointment.get_all_objects())