#!/usr/bin/python3
# -*- coding: utf-8 -*-

import survey

class Baby(survey.Record):
    """Represent a baby record """

class Babies(survey.Table):
    """Represents the Babies table."""
    def __init__(self):
        survey.Table.__init__(self)
        self.startflg = False

    def GetFilename(self):
        return 'babyboom.dat'

    def GetFields(self):
        return [
                ('birthtime', 1, 8, int),
                ('gender', 9, 16, int),
                ('birthwgt', 17, 24, int),
                ('minutes', 25, 32, int)
                ]

    def Recode(self):
        pass

    def ReadRecords(self, data_dir='.', n=None):
        filename = self.GetFilename()
        self.ReadFile(data_dir, filename, self.GetFields(), Baby, n)
        self.Recode()

    def MakeRecord(self, line, fields, constructor):		
        if not self.startflg:
            self.startflg = (line.find('START DATA:') > -1)
            return None

        obj = constructor()
        for (field, start, end, cast) in fields:
            try:
                s = line[start-1:end]
                val = cast(s)
            except ValueError:
                val = 'NA'
            setattr(obj, field, val)
        return obj

    def AddRecord(self, record):
        if record is not None:
            self.records.append(record)
