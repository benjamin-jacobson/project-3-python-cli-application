#!/usr/bin/env python3

from classes.user import User
from classes.__init__ import CONN, CURSOR

def seed_database():
    User.drop_table()
    User.create_table()

    # Creating seed data
    User.create("Mikey",14)
    print(len(User.all_users))

    # Closing database connection
    CONN.close()
seed_database()
print("Seeded database")