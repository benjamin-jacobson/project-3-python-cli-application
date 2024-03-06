from helpers import (
    exit_program,
    helper_1
)
from classes.user import User
from classes.vendor import Vendor
from classes.appointment import Appointment
# from classes.__init__ import CONN, CURSOR


def menu():
    print("Greetings superuser! Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function") # TODO delete
    print("2. Get all users.")
    print("3. Create a new user.")
    print("4. Delete a user.") # should add it to delete all there appointments too? BC this breaks the ORM... active flag better
    print("5. Find all users in a cohort.")
    print("6. Find all appointments for a user.")
    print("7. Create an appointment for a user.")



def main():
    while True:
        menu()
        choice = input("> ")

        if choice =="0":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice == "2":
            print(User.get_all_objects())
        elif choice == "3":
            username = input("Enter the new username: ") # TODO make a helper
            cohort_id = input("Enter the cohort id (0 if none): ")
            print(User.create(username, cohort_id))
        elif choice == "4":
            id_ = input("Enter the id of the username to delete: ")
            if u := User.find_by_id(id_):
                u.delete()
                print(f"Deleted user id {id_}")
            else:
                print(f"User id {id_} not found.")
        elif choice =="5":
            cohort_id = input("Enter the cohort id (0 is default): ")
            print(User.find_by_cohort(cohort_id))
        elif choice == "6":
            print("see all current usernames:")
            print(User.get_all_objects())
            username_ = input("Enter the username to show appointments for: ")
            if u_ := User.find_by_username(username_):
                print(u_)
                if len(u_.get_appointments()) == 0:
                    print(f"There are no appointments for {username_} at this time.")
                else:
                    for apt in u_.get_appointments():
                        print(apt)
            else:
                print(f"Username {username_} not found.")
        else:
            print("Invalid choice. Try again, but something different next time.")

if __name__ == "__main__":
    main()


