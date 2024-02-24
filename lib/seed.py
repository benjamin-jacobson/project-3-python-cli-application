#!/usr/bin/env python3

from classes.user import User
from classes.__init__ import CONN, CURSOR

def seed_database():
    User.drop_table()
    User.create_table()

    # Closing database connection
    CONN.close()
seed_database()
print("Seeded database")