#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random

def sample_expo(lam):
    return random.expovariate(lam) 

def sample_pareto(alpha,xm=1.0):
    return xm*random.paretovariate(alpha)

def sample_weibull(scale, shape):
    return random.weibullvariate(scale,shape)

def sample_normal(mu=0.0, sigma=1.0):
    return random.normalvariate(mu,sigma)

def sample_log_normal(mu=0.0, sigma=1.0):
    return random.lognormvariate(mu,sigma)

def samples(function_name, n, lam=1.0, alpha=1.0, \
        xm=1.0, scale=1.0, shape=1.0, mu=0.0, sigma=1.0):
    
    def sample():
        if function_name == 'expo':
            return sample_expo(lam)
        elif function_name == 'pareto':
            return sample_pareto(alpha,xm)
        elif function_name == 'weibull':
            return sample_weibull(scale,shape)
        elif function_name == 'normal':
            return sample_normal(mu,sigma)
        elif function_name == 'log_normal':
            return sample_log_normal(mu,sigma)
        else: 
            return sample_normal(mu,sigma)

    m = 1 # magnify factor    
    if n<10:  m = 10
    l = [sample() for i in range(m*n) if m==1 or (i>0 and i % (m-1)==0)]
    l.sort()
    return l

if __name__ == '__main__':
    fn = ['expo','pareto','weibull','normaal', 'no function']
    for f in fn:
        print(samples(f, 3))
