from classes.__init__ import CONN, CURSOR

class User:
    all_users = []
    all_users_persistant = {}

    def __init__(self,username, cohort_id, id=None):
        self.id = id
        self.username = username
        self.cohort_id = cohort_id
        type(self).all_users.append(self)

    def __repr__(self):
        return (
            f"Username: {self.username}," +
            f"cohort_id: {self.cohort_id}"
        )
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self,username):
        if isinstance(username,str) and (len(username)>4):
            self._username = username
        else:
            raise Exception("Username must be of type string and more than 4 characters.")

    @classmethod
    def create(cls,username, cohort_id):
        '''Initialize a new User Instance and save object to db'''
        new_user = cls(username,cohort_id)

        # Saving using to persistant db, and to class {} all_users_persistant
        new_user.save()
        return new_user

    @classmethod
    def create_table(cls):
        '''Create a new table to persist the attributes of User instance'''
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                cohort_id INTEGER
            );
            """
        CURSOR.execute(sql)
        CONN.commit
        #CONN.close()

    @classmethod
    def drop_table(cls):
        '''Drop persistant user table'''
        sql = """
        DROP TABLE IF EXISTS users; 
        """
        CURSOR.execute(sql)
        CONN.commit
        #CONN.close()

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

    # TODO find_by_username() """Return User object corresponding to first table row matching specified name"""