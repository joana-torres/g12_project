# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 15:45:54 2025

@author: joana
"""

# Class Person - generic version with inheritance
from classes.gclass import Gclass

class Post(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id','_date','_topic_id','_content']
    # Class header title
    header = 'Posts'
    # field description for use in, for example, input form
    des = ['Post Id','Post Date', 'Topic Id', 'Content']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, date, topic_id, content):
        super().__init__()
        # Object attributes
        id = Post.get_id(id)
        self._id = id
        self._date = date
        self._topic_id = topic_id
        self._content = content
        # Add the new object to the dictionary of objects
        Post.obj[id] = self
        # Add the id to the list of object ids
        Post.lst.append(id)
        
    # id property getter method
    @property
    def id(self):
        return self._id
    
    
    # name property getter method
    @property
    def date(self):
        return self._date
    
    # dob property getter method
    @property
    def topic_id(self):
        return self._topic_id
    
        
    # signupdate property getter method
    @property
    def content(self):
        return self._content
    # salary property setter method
    @content.setter
    def content(self, content):
        self._content = content
    # age property getter method
    
  

