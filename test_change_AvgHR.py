from user_class import User
from server_methods import create_NewUser
import pytest
import numpy as np

@pytest.mark.parametrize('oldahr, newahr', [

	(0.0, 10.0),
	(-1.0, -20.0),
	(0.0, 0.0),

	])
def test_changeavgHR(oldahr, newahr):
	myobj = create_NewUser('hold', 0, 1, oldahr, ['str'], '1')

	myobj.change_AvgHR(newahr)

	if myobj.AvgHR == newahr:
		assert True
	else:
		assert False

	


@pytest.mark.parametrize('oldahr, newahr, expect', [

	(0.0, 10, True),
	(-1.0, -20, True),
	(0.0, 0, True),
	(0.0, 'str', True),
	(0.0, 0.0, False),
	(0.0, [1], True),
	(0.0, (1, 0), True),
	(0.0, np.array([1, 2]), True),
	(0.0, None, True),

	])
def test_changeAvgHR2(oldahr, newahr, expect):
	myobj = create_NewUser('hold', 1, 1, oldahr, ['str'], '1')

	try:
		myobj.change_AvgHR(newahr)
		myb = False
	except TypeError:
		myb = True
	finally:
		assert myb == expect
