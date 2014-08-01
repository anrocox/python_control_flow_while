#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 23, 2014

@author: anroco

How to implement a while loop in Python?

¿Cómo implementar un ciclo while en Python?
'''

#must define the condition to evaluate and should always end with a colon.
#The while loop iterate whilst the condition is true.
#
#while expression:
#    statements

#create a integer
n = 0

#iterates whilst the value of n is less than 10
while n < 10:
    #adds 2 to value n
    n += 2
    print('the value of n is: ' + str(n))
