# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 18:51:22 2016

@author: Reuben
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        assert type(other) == type(self)
        if self.getX() == other.getX() and self.getY() == other.getY():
        
            return True
        else:
            return False
        
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'