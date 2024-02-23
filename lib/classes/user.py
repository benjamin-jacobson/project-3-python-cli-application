class User:
    all_users = []

    def __init__(self,username):
        self.username = username
        type(self).all_users.append(self)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self,username):
        if isinstance(username,str) and (len(username)>7):
            self._username = username
        else:
            raise Exception("Username must be of type string and more than 7 characters.")