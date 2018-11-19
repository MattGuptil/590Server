from user_class import User
from server_methods import *
import pytest
import numpy as np


# Additional testing for exceptions is not necessary here because this function
# can only be called on an object and does not take anyinputs other than itself


@pytest.mark.parametrize('faulty, expect', [

    (create_NewUser('hold', 1, 1, 0.0, ['str'], '1'), False),
    (60, True),
    (-20, True),
    (None, True),

])
def test_calcAvg3(faulty, expect):
    # myobj = create_NewUser('hold', 1, 1, 0.0, ['str'], '1')

    try:
        myobj = calcAv(faulty)
        myb = False
    except TypeError:
        myb = True
    finally:
        assert myb == expect


@pytest.mark.parametrize('oldhr, expect', [

    (0, 0),
    (60, 60),
    (-20, -20),

])
def test_calcAvg(oldhr, expect):
    myobj = create_NewUser('hold', oldhr, 1, 0.0, ['str'], '1')

    myobj = calcAv(myobj)

    if myobj.AvgHR == expect:
        assert True
    else:
        assert False


@pytest.mark.parametrize('oldhr, expect', [

    (0, 0),
    (60, 60),
    (-20, -20),

])
def test_calcAvg2(oldhr, expect):
    myobj = create_NewUser('hold', oldhr, 1, 0.0, ['str'], '1')
    for x in range(10):
        myobj.add_HR(oldhr)

    myobj = calcAv(myobj)

    if myobj.AvgHR == expect:
        assert True
    else:
        assert False
