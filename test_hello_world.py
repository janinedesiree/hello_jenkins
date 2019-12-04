import pytest
from Hello_World.py import *

#cant believe reynaldi had the 
#audacity to delete my first 
#project on jenkins

def test_hello():
    result = hello()
    assert result == 'hello!'
