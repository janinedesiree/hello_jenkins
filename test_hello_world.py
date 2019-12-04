import pytest
from Hello_World.py import *

def test_hello():
    result = hello()
    assert result == 'hello!'
