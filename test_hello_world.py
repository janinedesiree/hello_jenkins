import pytest
from hello_world import *

#cant believe reynaldi had the 
#audacity to delete my first 
#project on jenkins

def test_hello():
    result = hello()
    assert result == 'hello!'
