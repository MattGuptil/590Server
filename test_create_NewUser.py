from user_class import User
from server_methods import create_NewUser
import pytest
import numpy as np


@pytest.mark.parametrize('old, expect', [

    (0, 0),

])
def test_createUser(old, expect):
    myobj = create_NewUser('hold', 1, 1, 0.0, ['str', 'str'], '1')

    if myobj.email == 'hold':
        assert True
    if myobj.HR == 1:
        assert True
    if myobj.age == 1:
        assert True
    if myobj.AvgHR == 0.0:
        assert True
    if myobj.time == ['str', 'str']:
        assert True
    if myobj.id == '1':
        assert True
    else:
        assert False


@pytest.mark.parametrize('email, HR, Age, Avg, time, mid, expect', [

    ('hold', 1, 1, 0.0, ['str'], '1', False),
    (1, 1, 1, 0.0, ['str'], '1', True),
    ('d', 's', 1, 0.0, ['str'], '1', True),
    ('d', 1, 0.0, 0.0, ['str'], '1', True),
    ('d', 1, 1.0, 1.0, ['str'], '1', True),
    ('d', 1, 1, 0.0, 1, '1', True),
    ('d', [2.0], 2.0, [1], ['str'], '1', True),
    ('d', np.array([1, 2]), 1, 1.0, ['str'], '1', True),
    ('d', 1, 1, np.array([]), ['str'], '1', True),



])
def test_createUser2(email, HR, Age, Avg, time, mid, expect):

    try:
        myobj = create_NewUser(email, HR, Age, Avg, time, mid)
        myb = False
    except TypeError:
        myb = True
    finally:
        assert myb == expect
