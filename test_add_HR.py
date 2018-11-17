from user_class import User
from server_methods import create_NewUser
import pytest
import numpy as np

@pytest.mark.parametrize('oldhr, newhr, expect', [

	(0, 10, np.array([0, 10])),
	(-1, -20, np.array([-1, -20])),
	(0, 0, np.array([0, 0])),

	])
def test_addHR(oldhr, newhr, expect):
	myobj = create_NewUser('hold', oldhr, 1, 0.0, 'str')

	myobj.add_HR(newhr)

	try:
		np.testing.assert_equal(myobj.HR, expect)
	except AssertionError:
		assert False
"""
@pytest.mark.parametrize('oldage, newage, expect', [

	(0, 10, False),
	(-1, -20, False),
	(0, 0, False),
	(0, 'str', True),
	(0, 0.0, True),
	(0, [1], True),
	(0, (1, 0), True),
	(0, np.array([1, 2]), True),

	])
def test_changeage2(oldage, newage, expect):
	myobj = create_NewUser('hold', 1, oldage, 0.0, 'str')

	try:
		myobj.change_age(newage)
		myb = False
	except TypeError:
		myb = True
	finally:
		assert myb == expect
"""
