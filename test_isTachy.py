from user_class import User
from server_methods import *
import pytest
import numpy as np

# Additional testing for exceptions is not necessary here because this function
# can only be called on an object and does not take anyinputs other than
# itself.


@pytest.mark.parametrize('mid, age, expect', [

    (60, 20, False),
    (101, 20, True),
    (152, 1, True),
    (101, 2, False),
    (1140, 3, True),
    (101, 3, False),
    (120, 13, True),
    (101, 12, False),
    (60, 6, False),
    (134, 6, True),


])
def test_isTachy(mid, age, expect):
    myval = isTachy(mid, age)

    assert myval == expect
