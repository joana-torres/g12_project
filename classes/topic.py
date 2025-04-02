"""
@author: António Brito / Carlos Bragança
(2025) objective: class Person
"""
# Class Person - generic version with inheritance
from classes.gclass import Gclass
class Topic(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_topic_name','_description']
    # Class header title
    header = 'Topic'
    # field description for use in, for example, input form
    des = ['Topic Id','Topic Name', 'Description']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, topic_name, desc):
        super().__init__()
        # Object attributes
        id = Topic.get_id(id)
        self._id = id
        self._topic_name = topic_name
        self._description = desc
        # Add the new object to the dictionary of objects
        Topic.obj[id] = self
        # Add the id to the list of object ids
        Topic.lst.append(id)
        
    # id property getter method
    @property
    def id(self):
        return self._id

    @property
    def topic_name(self):
        return self._topic_name
    
    @topic_name.setter
    def topic_name(self, topic_name):
        self._topic_name = topic_name
        
    # des property getter method
    @property
    def description(self):
        return self._description
    
    # des property setter method
    @description.setter
    def description(self, description):
        self._description = description
    

