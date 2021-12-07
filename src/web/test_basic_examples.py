"""
This module contains basic examples of tests
"""
import pytest
import allure


def test_success():
    """this test succeeds"""
    assert True

def test_failure():
    """this test fails"""
    assert False

def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')

def test_broken():
    raise Exception('oops')



def test_pytest_expansion():
    a = {1: 2, 3: 4}
    b = {1: 3, 3: 4}

    assert a == b


def test_failed_by_pytest_fail():
    pytest.fail("This test is failed by result of the pytest.fail() call")


def test_skipped_by_pytest_skip():
    pytest.skip("This test is skipped by result of the pytest.skip() call")

