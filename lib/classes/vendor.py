from classes.__init__ import CONN, CURSOR

class Vendor:
    all_vendors_persistant = {}

    def __init__(self, name, type_id, id=None):
        self.id = id
        self.name = name
        self.type_id = type_id

    def __repr__(self):
        return (
            f"name: {self.name}," +
            f"type_id: {self.type_id}"
        )
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and (len(name)>0):
            self._name = name
        else:
            raise Exception("name must be of type string and more than 0 characters.")

    @classmethod
    def create(cls,name, type_id):
        '''Initialize a new Vendor Instance and save object to db'''
        new_vendor = cls(name,type_id)

        # Saving using to persistant db, and to class {} all_vendors_persistant
        new_vendor.save()
        return new_vendor

    @classmethod
    def create_table(cls):
        '''Create a new table to persist the attributes of Vendor instance'''
        sql = """
            CREATE TABLE IF NOT EXISTS vendors (
                id INTEGER PRIMARY KEY,
                name TEXT,
                type_id INTEGER
            );
            """
        CURSOR.execute(sql)
        CONN.commit
        #CONN.close()

    @classmethod
    def drop_table(cls):
        '''Drop persistant vendor table'''
        sql = """
        DROP TABLE IF EXISTS vendors; 
        """
        CURSOR.execute(sql)
        CONN.commit
        #CONN.close()

    def save(self):
        '''
        Insert a new row into the persistant db of the current vendor instance.
        Update object id attibute using the primary key of the new row
        Save the object in the local dictionary using the table rows PK as dictionary key
        NOTE: used in class method create().
        '''

        sql ="""
            INSERT INTO vendors (name, type_id)
            VALUES (?, ?);

        """
        CURSOR.execute(sql, (self.name, self.type_id))
        CONN.commit()

        # Getting the PK from the cursor, and using as the instance id
        self.id = CURSOR.lastrowid
        print(CURSOR.lastrowid)
        # Adding self (current vendor) with PK as key to class attribute with all saves {}
        type(self).all_vendors_persistant[self.id] = self

    @classmethod
    def get_all_data_in_vendor_database_table(cls):
        """Return a list of data in the vendor table."""
        sql = """
            SELECT * FROM vendors;
        """
        rows = CURSOR.execute(sql).fetchall()
        return rows

    @classmethod
    def get_all_objects(cls):
        """ Return a list containing one object per table row.
            Uses instance_from_db to check or create a new dictionary item if missing in local all
        """
        sql = """
            SELECT * FROM vendors;
        """
        rows = CURSOR.execute(sql).fetchall()
        # print(type(rows)) # list, could convert to DF via pandas if wanted for other analytics/ai
        # For all data in SELECT statement from vendor, using instance_from_db method
        # that checks against local {} all_vendors_persistant, updates local if different
        # or creates a local {} key/value pair if missin
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def instance_from_db(cls, row):
        """Return an Vendor object having the attribute values from the table row."""
        # Check the dictionary all_vendors_persistant for existing vendor instance using the row's primary key
        u = cls.all_vendors_persistant.get(row[0]) # row 0 is the PK by design
        if u:
            # ensure attributes match row values in case local instance was modified # TODO what if different?
            u.name = row[1]
            u.type_id = row[2]
        else:
            #
            u = cls(row[1],row[2])
            u.id = row[0]
            cls.all_vendors_persistant[u.id] = u
        return u

    def delete(self):
        """Delete table row corresponding to current instance ojbect.
        Delete the dictionary {} entry and reassign id attribute.
        """

        sql = """
            DELETE FROM vendors
            WHERE id = ?;
        """
        print(self.id)
        CURSOR.execute(sql, (self.id,)) # sneaky comma
        CONN.commit()

        # Delete the dictionary entry of instance pk
        del type(self).all_vendors_persistant[self.id]
        # Set id to None
        self.id = None

    def update(self):
        """Update the table row corresponding to the current instance."""
        sql="""
            UPDATE vendors
            SET name = ?, type_id = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.type_id,self.id))
        CONN.commit()

    @classmethod
    def find_by_id(cls,id):
        """Return Vendor object corresponding to the table row matching the specified primary key"""
        sql="""
            SELECT *
            FROM vendors
            WHERE id = ?;
        """
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls,name):
        """Return Vendor object corresponding to the table row matching the specified name"""
        sql="""
            SELECT *
            FROM vendors
            WHERE name = ?;
        """
        row = CURSOR.execute(sql,(name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def get_appointments(self):
        from classes.appointment import Appointment # avoiding circular dependency
        x = Appointment.get_all_objects()
        y = [f"{apt.appointment_year}, {apt.user.username}." for apt in x if apt.vendor.name == self.name]
        return y