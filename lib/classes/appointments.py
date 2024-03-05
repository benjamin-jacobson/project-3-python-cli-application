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


    ### need to clean below and convert to appointments
    
    def save(self):
        '''
        Insert a new row into the persistant db of the current user instance.
        Update object id attibute using the primary key of the new row
        Save the object in the local dictionary using the table rows PK as dictionary key
        NOTE: used in class method create().
        '''

        sql ="""
            INSERT INTO users (username, cohort_id)
            VALUES (?, ?);

        """
        CURSOR.execute(sql, (self.username, self.cohort_id))
        CONN.commit()

        # Getting the PK from the cursor, and using as the instance id
        self.id = CURSOR.lastrowid
        print(CURSOR.lastrowid)
        # Adding self (current user) with PK as key to class attribute with all saves {}
        type(self).all_users_persistant[self.id] = self

    @classmethod
    def get_all_data_in_user_database_table(cls):
        """Return a list of data in the user table."""
        sql = """
            SELECT * FROM users;
        """
        rows = CURSOR.execute(sql).fetchall()
        return rows

    @classmethod
    def get_all_objects(cls):
        """ Return a list containing one object per table row.
            Uses instance_from_db to check or create a new dictionary item if missing in local all
        """
        sql = """
            SELECT * FROM users;
        """
        rows = CURSOR.execute(sql).fetchall()
        # print(type(rows)) # list, could convert to DF via pandas if wanted for other analytics/ai
        # For all data in SELECT statement from user, using instance_from_db method
        # that checks against local {} all_users_persistant, updates local if different
        # or creates a local {} key/value pair if missin
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def instance_from_db(cls, row):
        """Return an User object having the attribute values from the table row."""
        # Check the dictionary all_users_persistant for existing user instance using the row's primary key
        u = cls.all_users_persistant.get(row[0]) # row 0 is the PK by design
        if u:
            # ensure attributes match row values in case local instance was modified # TODO what if different?
            u.username = row[1]
            u.cohort_id = row[2]
        else:
            #
            u = cls(row[1],row[2])
            u.id = row[0]
            cls.all_users_persistant[u.id] = u
        return u

    def delete(self):
        """Delete table row corresponding to current instance ojbect.
        Delete the dictionary {} entry and reassign id attribute.
        """

        sql = """
            DELETE FROM users
            WHERE id = ?;
        """
        print(self.id)
        CURSOR.execute(sql, (self.id,)) # sneaky comma
        CONN.commit()

        # Delete the dictionary entry of instance pk
        del type(self).all_users_persistant[self.id]
        # Set id to None
        self.id = None

    def update(self):
        """Update the table row corresponding to the current instance."""
        sql="""
            UPDATE users
            SET username = ?, cohort_id = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.username, self.cohort_id,self.id))
        CONN.commit()

    @classmethod
    def find_by_id(cls,id):
        """Return User object corresponding to the table row matching the specified primary key"""
        sql="""
            SELECT *
            FROM users
            WHERE id = ?;
        """
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_username(cls,username):
        """Return User object corresponding to the table row matching the specified username"""
        sql="""
            SELECT *
            FROM users
            WHERE username = ?;
        """
        row = CURSOR.execute(sql,(username,)).fetchone()
        return cls.instance_from_db(row) if row else None