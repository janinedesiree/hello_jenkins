import pytest
from Hello_World.py import *

#test

def test_hello():
    result = hello()
    assert result == 'hello!'
