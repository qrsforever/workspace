#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Babies
import math
import thinkstats
import Cdf
import Pmf
import myplot

def m3(l,dbg=False):

	m3 = 0
	if isinstance(l, list):
		n = len(l)
		mean = thinkstats.Mean(l)
		m3_l = [pow(x-mean,3) for x in l]
		m3 = float(sum(m3_l))/n
	elif isinstance(l, Pmf.Pmf):
		mean = l.Mean()
		for x, p in l.Items():
			m3 += pow(x-mean,3)*p 
	elif isinstance(l, Cdf):		
		m3 = l.cubed_variance()
	else:
		raise Exception('input parameter type is wrong')
	
	if dbg:
		print('m3: %4.2f' % m3)
	return m3

def skewness(l):
	''' m3 / m2 ^(3/2)
	    accept list, Pmf, Cdf as parameter
	'''
	var = 0 
	if isinstance(l, list):
		var = thinkstats.Var(l)
	elif isinstance(l, Pmf.Pmf):
		var= l.Var()
	elif isinstance(l, Cdf.Cdf):
		var = Cdf.Var()
	else:
		raise Exception('input parameter type is wrong')
	return m3(l)/pow(var, 1.5)

def pearson_skewness(l):
	''' 3(mean - median)/sigma
	'''
	cdf = None
	if isinstance(l, list):
		cdf = Cdf.MakeCdfFromList(l)
	elif isinstance(l, Pmf.Pmf):
		cdf = Cdf.MakeCdfFromPmf(l)
	elif isinstance(l, Cdf.Cdf):
		cdf = l
	else:
		raise Exception('input parameter type is wrong')
		
	mean = cdf.Mean()
	median = cdf.Percentile(50)
	sigma = math.sqrt(cdf.Var())		
	return 3.0*(mean - median)/sigma

def observe_data(l, name=None, show=False):	
	cdf = pmf = None
	if isinstance(l, list):
		cdf = Cdf.MakeCdfFromList(l,name+' cdf')
		pmf = Pmf.MakePmfFromList(l, name+' pmf')
	elif isinstance(l, Pmf.Pmf):
		pmf = l
		cdf = Cdf.MakeCdfFromPmf(l)
		if name is None: name = pmf.name 
	elif isinstance(l, Cdf.Cdf):
		cdf = l
		if name is None: name = cdf.name 
	else:
		raise Exception('input parameter type is wrong')

	v_25, median, v_75 = cdf.Percentile(25), cdf.Percentile(50), cdf.Percentile(75)
	mean = cdf.Mean()
	print('%s: 1/4:%4.2f(%4.2f), 1/2:%4.2f(mean-median:%4.2f), mean:%4.2f, 3/4:%4.2f(%4.2f)' % \
	      (name, v_25, median-v_25, median, mean-median, mean, v_75,v_75-median))
	
	if show:
		if pmf is not None:
			myplot.Pmf(pmf)	
			myplot.Show()
		myplot.Cdf(cdf)
		myplot.Show()

def show_skewness(l=None, name=None):
	print('%s skewness:%4.2f, p skewness:%4.2f' % \
	        (name, skewness(l), pearson_skewness(l)))
	observe_data(l, name)


def example():
	baby_1st, baby_rest, babies = Babies.PartitionBabies()

	l_wt = Babies.GetWightList(babies)
	show_skewness(l_wt,'weight')

	l_preg = Babies.GetPregnacyList(babies)
	show_skewness(l_preg,'pregnancy')
	
