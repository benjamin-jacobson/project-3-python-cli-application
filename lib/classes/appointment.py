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
    def create_table(cls):
        '''Create a new table to persist the attributes of User instance'''
        sql = """
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                vendor_id INTEGER,
                appointment_type TEXT,
                appointment_year INTEGER
            );
            """
        CURSOR.execute(sql)
        CONN.commit
        #CONN.close()

    @classmethod
    def drop_table(cls):
        '''Drop persistant user appointments'''
        sql = """
        DROP TABLE IF EXISTS appointments; 
        """
        CURSOR.execute(sql)
        CONN.commit
        #CONN.close()

    @classmethod
    def create(cls, user, vendor, appointment_type, appointment_year):
        """ Initialize a new Appointment instance and save the object to the database """
        appointment = cls(user, vendor, appointment_type, appointment_year)
        appointment.save()
        return appointment

    def save(self):
        '''
        Insert a new row into the persistant db of the current appointment instance.
        Update object id attibute using the primary key of the new row
        Save the object in the local dictionary using the table rows PK as dictionary key
        NOTE: used in class method create().
        '''

        sql ="""
            INSERT INTO appointments (user_id, vendor_id, appointment_type,appointment_year)
            VALUES (?, ?, ?, ?);

        """
        CURSOR.execute(sql, (self.user.id, self.vendor.id, self.appointment_type, self.appointment_year ))
        CONN.commit()

        # Getting the PK from the cursor, and using as the instance id
        self.id = CURSOR.lastrowid
        print(CURSOR.lastrowid)
        # Adding self (current appointment) with PK as key to class attribute with all saves {}
        type(self).all_appointments_persistant[self.id] = self

    @classmethod
    def get_all_data_in_appointments_database_table(cls):
        """Return a list of data in the appointments table."""
        sql = """
            SELECT * FROM appointments;
        """
        rows = CURSOR.execute(sql).fetchall()
        return rows

    ### need to clean below and convert to appointments
    @classmethod
    def get_all_objects(cls):
        """ Return a list containing one object per table row.
            Uses instance_from_db to check or create a new dictionary item if missing in local all
        """
        sql = """
            SELECT * FROM appointments;
        """
        rows = CURSOR.execute(sql).fetchall()
        # print(type(rows)) # list, could convert to DF via pandas if wanted for other analytics/ai
        # For all data in SELECT statement from appointments, using instance_from_db method
        # that checks against local {} all_appointments_persistant, updates local if different
        # or creates a local {} key/value pair if missing
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def instance_from_db(cls, row):
        """Return an Appointment object having the attribute values from the table row."""
        # Check the dictionary all_users_persistant for existing user instance using the row's primary key
        apt = cls.all_appointments_persistant.get(row[0]) # row 0 is the PK by design
        if apt:
            # ensure attributes match row values in case local instance was modified # TODO what if different?
            print(apt)
            apt.user = User.find_by_id(row[1]) # db stores the id, not the user instance, need to get it
            apt.vendor = Vendor.find_by_id(row[2]) # same as ^
            apt.appointment_type = row[3]
            apt.appointment_year = row[4]
        else:
            #
            apt = cls(User.find_by_id(row[1]),
                        Vendor.find_by_id(row[2]),
                        row[3],
                        row[4]) # same as ^
            apt.id = row[0]
            cls.all_appointments_persistant[apt.id] = apt
        return apt

    def delete(self):
        """Delete table row corresponding to current instance ojbect.
        Delete the dictionary {} entry and reassign id attribute.
        """

        sql = """
            DELETE FROM appointments
            WHERE id = ?;
        """
        print(self.id)
        CURSOR.execute(sql, (self.id,)) # sneaky comma
        CONN.commit()

        # Delete the dictionary entry of instance pk
        del type(self).all_appointments_persistant[self.id]
        # Set id to None
        self.id = None

    def update(self):
        """Update the table row corresponding to the current instance."""
        sql="""
            UPDATE appointments
            SET user_id = ?, vendor_id = ?, appointment_type = ?, appointment_year = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.user.id, self.vendor.id,self.appointment_type,self.appointment_year))
        CONN.commit()