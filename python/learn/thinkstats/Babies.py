#!/usr/bin/python3
# -*- coding: utf-8 -*-

import survey

def PartitionBabies():
    firsts, others, babies = [],[],[]

    table = survey.Pregnancies() 
    table.ReadRecords('res')

    for baby in table.records:
        if baby.outcome != 1:
            continue		
        data = (baby.prglength, baby.totalwgt_oz)
        babies.append(data)
        if baby.birthord == 1:
            firsts.append(data)
        else:
            others.append(data)

    return firsts, others, babies

def GetWightList(babies):
    return [x[1] for x in babies if x[1] != 'NA'] 	

def GetPregnacyList(babies):
    return [x[0] for x in babies if x[0] != 'NA']
