"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
from classes.user import User
from classes.post import Post

class User_Post(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_user_id','_post_id', '_like_date']
    # Class header title
    header = 'User Post'
    # field description for use in, for example, input form
    des = ['User Post Id','User Id', 'Post Id','Like Date']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, user_id, post_id, like_date):
        super().__init__()
        user_id = int(user_id)
        post_id = int(post_id)
        if user_id in User.lst:
            if post_id in Post.lst:
            # Object attributes
                id = User_Post.get_id(id)
                self._id = id
                self._user_id = user_id
                self._post_id = post_id
                self._like_date = like_date
                # Add the new object to the dictionary of objects
                User_Post.obj[id] = self
                # Add the id to the list of object ids
                User_Post.lst.append(id)
            else:
                print('Post',post_id,'not found')
        else:
            print('User',user_id,'not found')
            
        
    # id property getter method
    @property
    def id(self):
        return self._id
   
    
    # name property getter method
    @property
    def user_id(self):
        return self._user_id
 
    @property
    def post_id(self):
        return self._post_id
    
    @property
    def like_date(self):
        return self._like_date
   

  

