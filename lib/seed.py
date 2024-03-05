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
    u1 = User.create("Mikey",14)
    u2 = User.create("Benny",27)
    print(u1)
    print(len(User.all_users))
    print(len(User.all_users_persistant))

    out = User.get_all_data_in_user_database_table()
    print("All rows in db:")
    print(out)

    out = User.get_all_objects()
    print(f"All rows in db and local {out}:")
    print(f"Just local {User.all_users_persistant}")

    print(u2)
    print("---")
    u2.delete()

    print(f"Testing deleting user 2:{u2} ")
    out = User.get_all_objects()
    print("All rows in db and local {}:")
    print(out)

    # Vendor
    Vendor.drop_table()
    Vendor.create_table()
    vendor_1 = Vendor.create("Twitter", 234)
    vendor_2 = Vendor.create("Ebay", 222)


    # Another seed test with appointments too

    User.drop_table()
    User.create_table()
    user_1 = User("Robertoss",12)

    Vendor.drop_table()
    Vendor.create_table()
    vendor_1 = Vendor.create("Twitter", 12)

    Appointment.drop_table()
    Appointment.create_table()

    apt_1 = Appointment.create(user_1, vendor_1, "in person", 2024) # user, vendor, appointment_type, appointment_year
    assert ((apt_1.user, apt_1.vendor, apt_1.appointment_type ,apt_1.appointment_year)==(user_1,vendor_1,"in person",2024))

    print(Appointment.get_all_data_in_appointments_database_table())


    # Closing database connection
    CONN.close()
seed_database()
print("Seeded database")