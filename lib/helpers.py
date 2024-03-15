from classes.user import User
from classes.vendor import Vendor
from classes.appointment import Appointment

def helper_1():
    print("This program has user, vendors and their appointments. You can add, delete, and see information for each.")
    print("Use the menu options to use each functionality.")

def helper_2():
    print([i.username for i in User.get_all_objects()])

def helper_3():
    username = input("Enter the new username: ")
    cohort_id = input("Enter the cohort id (0 if none): ")
    print(User.create(username, cohort_id))

def helper_4():
    print("See all users:")
    print([f'{i.id}: {i.username}' for i in User.get_all_objects()])
    id_ = input("Enter the id of the username to delete: ")
    if u := User.find_by_id(id_):
        u.delete()
        print(f"Deleted user id {id_}")
    else:
        print(f"User id {id_} not found.")

def helper_5():
    print(f'Possible cohort ids: {list(set([i.cohort_id for i in User.get_all_objects()]))}')
    cohort_id = input("Enter the cohort id (0 is default): ")
    print(User.find_by_cohort(cohort_id))

def helper_6():
    print("See all current usernames:")
    print([i.username for i in User.get_all_objects()])
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

def helper_7():
    # Getting username
    print("see all current usernames:")
    print([i.username for i in User.get_all_objects()])
    username_ = input("Enter the exising username: ")
    if not User.find_by_username(username_):
        print(f"Username {username_} not found.")
    else:
        user_ = User.find_by_username(username_)

    # Getting vendor
    print("see all current vendors:")
    # print(Vendor.get_all_objects())
    print([i.name for i in Vendor.get_all_objects()])
    vendor_ = input("Enter the existing Vendor: ") 
    if not Vendor.find_by_name(vendor_):
        print(f"Vendor {vendor_} not found.")
    else:
        vendor_ = Vendor.find_by_name(vendor_)
    
    # Getting appointment type and year
    appointment_type_ = input("Enter the appointment type: ")
    appointment_year_ = input("Enter the appointment year: ")

    Appointment.create(user=user_, 
                        vendor=vendor_, 
                        appointment_type=appointment_type_, 
                        appointment_year=appointment_year_)
def helper_8():
    print([f'{i.id}: {i.name}' for i in Vendor.get_all_objects()])

def helper_9():
    name_ = input("Enter the new vendor name: ")
    type_id_ = input("Enter the type_id id (0 if none): ")
    print(Vendor.create(name_, type_id_))

def helper_10():
    print("Under construction currently...")

def helper_11():
    print([f'{i.id}: {i.name}' for i in Vendor.get_all_objects()])
    vendor_name = input("Enter the vandorname to show appointments for: ")
    v = Vendor.find_by_name(vendor_name)
    print(v.get_appointments())

def exit_program():
    print("Goodbye!")
    exit()