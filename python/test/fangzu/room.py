#!/usr/bin/python3
# -*- coding: utf-8 -*-

class RoomInfo(object):

    """Room info class"""

    def __init__(self, place, room, area, rent):
        self.place = place
        self.room = room
        self.area = area
        self.rent = rent

    def getPlace(self):
        return self.place

    def getRoom(self):
        return self.room

    def getArea(self):
        return self.area

    def getRent(self):
        return self.rent

    def __repr__(self):
        return 'RoomInfo({0.place!r}, {0.room!r}, {0.area!r}, {0.rent!r})'.format(self)
    
    def __str__(self):
        return '({0.place!s}, {0.room!s}, {0.area!s}, {0.rent!s})'.format(self)
