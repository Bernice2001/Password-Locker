import random
import string


class User:
    user_list=[]
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def save_user(self):
        User.user_list.append(self)

class Credentials:
    credentials_list=[]
    def __init__(self,account,username,password):
        self.account=account
        self.username=username
        self.password=password
    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        Credentials.credentials_list.remove(self) 

    @classmethod
    
    def find_credentials(cls,account):
        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials 

    @classmethod
    
    def credentials_exist(cls, account):
        for credentials in cls.credentials_list:
            if credentials.account== account:
                return True
        return False

    @classmethod

    def display_credentials(cls):
        return cls.credentials_list

    def generate_password(stringLength = 6):
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "(|/~!.@,)#{?$[%]^}&*"
        return ''.join(random.choice(password) for i in range(stringLength))    