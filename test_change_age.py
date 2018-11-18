from user_class import User
from server_methods import create_NewUser
import pytest
import numpy as np

@pytest.mark.parametrize('oldage, newage', [

	(0,10),
	(-1, -20),
	(0, 0),

	])
def test_changeage(oldage,newage):
	myobj = create_NewUser('hold', 1, oldage, 0.0, ['str'], '1')

	myobj.change_age(newage)

	if myobj.age == newage:
		assert True
	else:
		assert False

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
	myobj = create_NewUser('hold', 1, oldage, 0.0, ['str'], '1')

	try:
		myobj.change_age(newage)
		myb = False
	except TypeError:
		myb = True
	finally:
		assert myb == expect
