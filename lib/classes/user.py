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