import unittest
from mock import MagicMock
from lib.class_name import ClassName

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
