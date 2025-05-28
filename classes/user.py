"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
import datetime 
class User(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_name','_email','_signup_date','_foto']
    # Class header title
    header = 'Users'
    # field description for use in, for example, input form
    des = ['User Id','User Name', 'Email', 'Signup Date', 'Foto']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, name, email, signupdate): #falta foto
        super().__init__()
        # Object attributes
        id = User.get_id(id)
        self._id = id
        self._name = name
        self._email = email
        data_formatada = datetime.datetime.strptime(signupdate, "%d/%m/%Y")
        data=data_formatada.strftime("%Y-%m-%d")
        self._signup_date = datetime.date.fromisoformat(data)
        # Add the new object to the dictionary of objects
        #self._foto = foto
        User.obj[id] = self
        # Add the id to the list of object ids
        User.lst.append(id)
    # id property getter method
    @property
    def id(self):
        return self._id
    
    
    # name property getter method
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
        
    # dob property getter method
    @property
    def email(self):
        return self._email
    # dob property setter method
    @email.setter
    def email(self, email):
        self._email = email
        
    # signupdate property getter method
    @property
    def signup_date(self):
        return self._signup_date
    # salary property setter method
    @signup_date.setter
    def signup_date(self, signup_date):
        self._signup_date = signup_date
    # age property getter method
    
    # @property
    # def foto(self):
    #     return self._foto
    
    # @foto.setter
    # def foto(self, foto):
    #     self._foto = foto

