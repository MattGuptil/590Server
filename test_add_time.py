from user_class import User
from server_methods import create_NewUser
import pytest
import numpy as np


@pytest.mark.parametrize('oldtime, newtime, expect', [

    (['str'], ['str2'], ['str', 'str2']),
    (['str'], ['str3'], ['str', 'str3']),
    (['str'], ['strgadf'], ['str', 'strgadf']),

])
def test_addtime(oldtime, newtime, expect):
    myobj = create_NewUser('hold', 0, 1, 0.0, oldtime, '1')

    myobj.add_time(newtime)

    if myobj.time == expect:
        assert True
    else:
        assert False


@pytest.mark.parametrize('oldtime, newtime, expect', [

    (['str'], 10, True),
    (['str'], -20, True),
    (['str'], 0, True),
    (['str'], ['str'], False),
    (['str'], 0.0, True),
    (['str'], [1], True),
    (['str'], (1, 0), True),
    (['str'], np.array([1, 2]), True),
    (['str'], None, True),

])
def test_addtime2(oldtime, newtime, expect):
    myobj = create_NewUser('hold', 1, 1, 0.0, oldtime, '1')

    try:
        myobj.add_time(newtime)
        myb = False
    except TypeError:
        myb = True
    finally:
        assert myb == expect
