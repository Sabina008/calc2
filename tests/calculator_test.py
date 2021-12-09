"""Testing the Calculator"""

import pytest

from calculator.calculator import Calculator
# This function is clled a fixture, it will be run everytime it is passed to a test.
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument

@pytest.fixture
def cl_hist():
    """This is the main the clear history method"""
    Calculator.cl_hist()

def test_cl_hist(cl_hist):
    """Testing the Clear History"""
    assert Calculator.add_number(8,2) == 10
    assert Calculator.add_number(17, 2) == 19
    assert Calculator.add_number(5, 2) == 7
    assert Calculator.add_number(23, 2) == 25
    assert Calculator.history_count() == 4
    assert Calculator.cl_hist() is True
    assert Calculator.history_count() == 0
    
def test_calculator_add(cl_hist):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(2, 6) == 8
    assert Calculator.add_number(2, 9) == 11
    assert Calculator.add_number(4, 8) == 12
    assert Calculator.add_number(6, 2) == 8
    assert Calculator.history_count() == 4
    assert Calculator.get_last_cal_add_hist() == 8

def test_get_last_calculation_result(cl_hist):
    """Testing last result of the calculator"""
    assert Calculator.add_number(9, 3) == 12
    assert Calculator.add_number(10, 8) == 18
    assert Calculator.get_last_cal_add_hist() == 18
    
def test_count_history(cl_hist):
    """Testing the count history of the calculator"""
    assert Calculator.history_count() == 0
    assert Calculator.add_number(9, 2) == 11
    assert Calculator.add_number(2, 6) == 8
    assert Calculator.history_count() == 2

def test_get_first_calculation_result(cl_hist):
    """Testing first result of the calculator"""
    assert Calculator.add_number(23, 2) == 25
    assert Calculator.add_number(7, 2) == 9
    assert Calculator.get_first_cal_add_hist() == 25

def test_calculator_subtract(cl_hist):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(3, 2) == 1
    assert Calculator.subtract_number(10, 2) == 8
    assert Calculator.subtract_number(15, 5) == 10
    
def test_calculator_division(cl_hist):
    """ tests division of two numbers"""
    assert Calculator.divide_numbers(25, 5) == 5
    assert Calculator.divide_numbers(12, 2) == 6
    assert Calculator.divide_numbers(8, 2) == 4

def test_calculator_multiply(cl_hist):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(2, 3) == 6
    assert Calculator.multiply_numbers(4,5) == 20
    assert Calculator.multiply_numbers(9,5) == 45
    
