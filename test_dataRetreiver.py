from user_class import User
from server_methods import *
import pytest
import numpy as np

## Additional testing for exceptions is not necessary here because this function
## can only be called on an object and does not take anyinputs other than itself.


@pytest.mark.parametrize('mid, prp, expect', [

	('1', 'AvgHR', {"Avg Heart Rate": 0.0}),
	('1', 'HR', {"Heart Rates": np.array([1])}),
	('1', 'status', False),
	

	])
def test_dataRetreiver(mid, prp, expect):
	myobj = create_NewUser('hold', 1, 1, 0.0, ['str'], '1')
	myUsers.append(myobj)
	mydict = dataRetreiver(mid, prp)

	if prp == 'status':
		assert mydict['isTachy'] == expect
	else:
		assert mydict == expect


@pytest.mark.parametrize('mobj, em, prp, expect', [

	(create_NewUser('hold', 1, 1, 0.0, ['str'], '1'), '1', 'AvgHR', False),
	(create_NewUser('hold', 1, 1, 0.0, ['str'], '1'), '1', 'HR', False),
	(create_NewUser('hold', 1, 1, 0.0, ['str'], '2'), '2', 'status', False),
	(create_NewUser('hold', 1, 1, 0.0, ['str'], '3'), 'hold1', 'status', True),
	(create_NewUser('hold', 1, 1, 0.0, ['str'], '3'), 'hold', 'ag', True),
	(create_NewUser('hold', 1, 1, 0.0, ['str'], '4'), 'hold', 21, True),
	(create_NewUser('hold', 1, 1, 0.0, ['str'], '5'), 'hold1', [2], True),
	

	])
def test_dataRetreiver2(mobj, em, prp, expect):
	myUsers.append(mobj)
	try:
		mydict = dataRetreiver(em, prp)
		myb = False
	except ValueError:
		myb = True

	finally:
		assert myb == expect
