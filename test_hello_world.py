import pytest
from Hello_World.py import *

#if this doesnt work imma cry :(

def test_hello():
    result = hello()
    assert result == 'hello!'
