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
        # Adding self (current user) with PK as key to class attribute with all saves {}
        type(self).all_users_persistant[self.id] = self