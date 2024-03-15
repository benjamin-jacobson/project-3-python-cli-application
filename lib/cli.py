from helpers import *

from classes.user import User
from classes.vendor import Vendor
from classes.appointment import Appointment
# from classes.__init__ import CONN, CURSOR


def menu():
    print("Greetings superuser! Please select an option:")
    print("0. Exit the program.")
    print("1. Tell me about the program.")
    print("2. Get all users.")
    print("3. Create a new user.")
    print("4. Delete a user.") # should add it to delete all there appointments too? BC this breaks the ORM... active flag better
    print("5. Find all users in a cohort.")
    print("6. Find all appointments for a user.")
    print("7. Create an appointment for a user.") # delete an appointment by year/vendor is a little most complex but need
    print("8. Get all vendors.")
    print("9. Create a new vendor.")
    print("10. Delete a vendor.") # should add it to delete all there appointments too? BC this breaks the ORM... active flag better
    print("11. Get a vendor's appointments.")

def main():
    while True:
        menu()
        choice = input("> ")

        if choice =="0":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice == "2":
            helper_2()
        elif choice == "3":
            helper_3()
        elif choice == "4":
            helper_4()
        elif choice =="5":
            helper_5()
        elif choice == "6":
            helper_6()
        elif choice == "7":
            helper_7()
        elif choice == "8":
            helper_8()
        elif choice == "9":
            helper_9()
        elif choice == "10":
            helper_10()
        elif choice == "11":
            helper_11()
        
        else:
            print("Invalid choice. Try again, but something different next time.")

if __name__ == "__main__":
    main()