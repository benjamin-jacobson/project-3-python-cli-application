#!/usr/bin/env python3

from classes.user import User
from classes.vendor import Vendor
from classes.appointment import Appointment
from classes.__init__ import CONN, CURSOR

def seed_database():

    #User table
    User.drop_table()
    User.create_table()

    # Creating seed data
    u1 = User.create("Machelangelo",1)
    u2 = User.create("Leonardo",1)
    u1 = User.create("Donatello",1)
    u2 = User.create("Rafael",1)
    u2 = User.create("Professor X",2)
    u2 = User.create("Wolverine",2)

    print(User.get_all_objects())

    # Vendor
    Vendor.drop_table()
    Vendor.create_table()
    v1 = Vendor.create("Library", 1)
    v2 = Vendor.create("Museum", 1)
    v3 = Vendor.create("Kens Artisan Pizza", 2)
    v4 = Vendor.create("Quarterworld", 2)

    print(Vendor.get_all_objects())

    # Appointment

    Appointment.drop_table()
    Appointment.create_table()

    a1 = Appointment.create(u1, v3, "in person", 2024) # user, vendor, appointment_type, appointment_year
    a1 = Appointment.create(u1, v3, "in person", 2024) # user, vendor, appointment_type, appointment_year
    a1 = Appointment.create(u1, v3, "in person", 2023) # user, vendor, appointment_type, appointment_year
    a1 = Appointment.create(u1, v3, "in person", 2022) # user, vendor, appointment_type, appointment_year

    print(Appointment.get_all_data_in_appointments_database_table())

    # Closing database connection
    CONN.close()
seed_database()
print("Seeded database")