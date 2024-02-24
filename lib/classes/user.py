from classes.__init__ import CONN, CURSOR

class User:
    all_users = []

    def __init__(self,username, cohort_id, id=None):
        self.id = id
        self.username = username
        self.cohort_id = cohort_id
        type(self).all_users.append(self)

    def __repr__(self):
        return (
            f"Username {self.username}" +
            f"cohort_id {cohort_id}"
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
        #new_user.save()
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
    