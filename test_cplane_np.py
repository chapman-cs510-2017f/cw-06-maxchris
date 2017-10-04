#!/usr/bin/env python3

# Name: Maksym Solodovskyi & Chris Watkins
# Student ID: 2299101 & 1450263
# Email:  solodovs@chapman.edu & watki115@mail.chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 6
###

import numpy as np
from cplane_np import ArrayComplexPlane
def f(x):
    return x+2
 
def test_cplane1():
    P = ArrayComplexPlane(1,2,2,1,2,2)
    np.testing.assert_array_equal(P.refresh(), np.reshape(np.array([(1+1*1j), (2+1*1j),(1+2*1j), (2+2*1j)]),(2,2)))
    
def test_cplane2():
    P = ArrayComplexPlane(1,2,2,1,2,2)
    P.refresh()
    np.testing.assert_array_equal(P.apply(f),np.reshape(np.array([(3+1*1j), (4+1*1j), (3+2*1j),(4+2*1j)]),(2,2)))

def test_cplane3():
    P = ArrayComplexPlane(1,2,2,1,2,2)
    P.refresh()
    P.apply(f)
    np.testing.assert_array_equal(P.zoom(1,3,3,1,3,3), np.reshape(np.array([(3+1*1j),(4+1*1j),(5+1*1j), (3+2*1j), (4+2*1j),(5+2*1j), (3+3*1j), (4+3*1j), (5+3*1j)]),(3,3)))
    
def test_cplane4():
    P = ArrayComplexPlane(2,3,2,2,3,2)
    np.testing.assert_array_equal(P.refresh(), np.reshape(np.array([(2+2*1j), (3+2*1j),(2+3*1j), (3+3*1j)]),(2,2)))
    
def test_cplane5():
    P = ArrayComplexPlane(2,3,2,2,3,2)
    P.refresh()
    np.testing.assert_array_equal(P.apply(f),np.reshape(np.array([(4+2*1j), (5+2*1j), (4+3*1j),(5+3*1j)]),(2,2)))

def test_cplane6():
    P = ArrayComplexPlane(2,3,2,2,3,2)
    P.refresh()
    P.apply(f)
    np.testing.assert_array_equal(P.zoom(4,5,2,4,5,2), np.reshape(np.array([(6+4*1j), (7+4*1j), (6+5*1j),(7+5*1j)]),(2,2)))