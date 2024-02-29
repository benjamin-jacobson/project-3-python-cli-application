from classes.__init__ import CONN, CURSOR

from classes.user import User
from classes.vendor import Vendor

class Appointment:
    all_appointments_persistant = {}

    def __init__(self, user, vendor, appointment_type, appointment_year, id=None):
        self.id = id
        self.user = user
        self.vendor = vendor
        self.appointment_type = appointment_type
        self.appointment_year = appointment_year

    def __repr__(self):
        return (
            f"user: {self.user}," +
            f"vendor: {self.vendor}" +
            f"appointment_type: {self.appointment_type}" +
            f"appointment_year: {self.appointment_year}"
        )
    
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self,user):
        if isinstance(user,User):
            self._user = user
        else:
            raise Exception("user must be of class User.")

    @property
    def vendor(self):
        return self._vendor
    
    @vendor.setter
    def vendor(self,vendor):
        if isinstance(vendor,Vendor):
            self._vendor = vendor
        else:
            raise Exception("vendor must be of class Vendor.")

    @classmethod
    def create(cls, user, vendor, appointment_type, appointment_year):
        """ Initialize a new Appointment instance and save the object to the database """
        appointment = cls(user, vendor, appointment_type, appointment_year)
        # appointment.save()
        return appointment