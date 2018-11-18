from user_class import User
from server_methods import *
import pytest
import numpy as np

## Additional testing for exceptions is not necessary here because this function
## can only be called on an object and does not take anyinputs other than itself.


@pytest.mark.parametrize('em, prp, expect', [

	('hold', 'AvgHR', {"Heart Rates": 0.0}),
	('hold', 'HR', {"Heart Rates": np.array([1])}),
	('hold', 'age', {"Heart Rates": 1}),
	

	])
def test_dataRetreiver(em, prp, expect):
	myobj = create_NewUser('hold', 1, 1, 0.0, ['str'])
	myUsers.append(myobj)
	mydict = dataRetreiver(em, prp)

	assert mydict == expect


@pytest.mark.parametrize('mobj, em, prp, expect', [

	(create_NewUser('hold', 1, 1, 0.0, ['str']), 'hold', 'AvgHR', False),
	(create_NewUser('hold', 1, 1, 0.0, ['str']), 'hold', 'HR', False),
	(create_NewUser('hold', 1, 1, 0.0, ['str']), 'hold', 'age', False),
	(create_NewUser('hold', 1, 1, 0.0, ['str']), 'hold1', 'age', True),
	(create_NewUser('hold', 1, 1, 0.0, ['str']), 'hold', 'ag', True),
	(create_NewUser('hold', 1, 1, 0.0, ['str']), 'hold', 21, True),
	(create_NewUser('hold', 1, 1, 0.0, ['str']), 'hold1', [2], True),
	

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