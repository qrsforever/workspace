#!/usr/bin/python3
# -*- coding: utf-8 -*-

# l-1: 可复用性较差,  没有返回
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1

fab(5)

print("-------1------ ")

# l-2: 内存占用
def fab2(max): 
   n, a, b = 0, 0, 1 
   L = [] 
   while n < max: 
       L.append(b) 
       a, b = b, a + b 
       n = n + 1 
   return L

for n in fab2(5):
    print(n)

print("-------2------ ")

# l-3: 自己实现迭代, 不简洁
class fab3(object): 
 
   def __init__(self, max): 
       self.max = max 
       self.n, self.a, self.b = 0, 0, 1 
 
   def __iter__(self): 
       return self 
 
   def __next__(self): 
       if self.n < self.max: 
           r = self.b 
           self.a, self.b = self.b, self.a + self.b 
           self.n = self.n + 1 
           return r 
       raise StopIteration()

for n in fab3(5):
    print(n)
    
print("-------3------ ")

# l-4: yield 版本, fab4是方法, fab4(n)是实例generator
def fab4(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for n in fab4(5):
    print(n)
