def get_test_code(base_name):
    return f"""
import pytest
from StenLib.{base_name} import *

def test_sample():
    assert True
"""
