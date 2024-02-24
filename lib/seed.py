#!/usr/bin/env python3

from classes.user import User
from classes.__init__ import CONN, CURSOR

def seed_database():
    User.create_table()


seed_database()
print("Seeded database")