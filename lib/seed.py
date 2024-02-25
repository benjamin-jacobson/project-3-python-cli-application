#!/usr/bin/env python3

from classes.user import User
from classes.__init__ import CONN, CURSOR

def seed_database():
    User.drop_table()
    User.create_table()

    # Creating seed data
    u1 = User.create("Mikey",14)
    u2 = User.create("Benny",27)
    print(u1)
    print(len(User.all_users))
    print(len(User.all_users_persistant))

    out = User.get_all()
    print("All rows in db:")
    print(out)

    # Closing database connection
    CONN.close()
seed_database()
print("Seeded database")