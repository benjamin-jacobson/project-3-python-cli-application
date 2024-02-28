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

    out = User.get_all_data_in_user_database_table()
    print("All rows in db:")
    print(out)

    out = User.get_all_objects()
    print(f"All rows in db and local {out}:")
    print(f"Just local {User.all_users_persistant}")

    print('findbyid')
    
    print(f"vvvv: {User.find_by_id(2)}")

    print(u2)
    print("---")
    u2.delete()

    print(f"Testing deleting user 2:{u2} ")
    out = User.get_all_objects()
    print("All rows in db and local {}:")
    print(out)



    # Closing database connection
    CONN.close()
seed_database()
print("Seeded database")