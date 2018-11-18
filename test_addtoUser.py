from user_class import User
from server_methods import *
import pytest
import numpy as np

@pytest.mark.parametrize('new, new1, new2, expect, expect1, expect2', [

	(2, 21, ['str2'], np.array([1, 2]), 21, ['str', 'str', 'str2'])



	])
def test_addtoUser(new, new1, new2, expect, expect1, expect2):
	myobj = create_NewUser('hold', 1, 1, 0.0, ['str', 'str'], '1')

	mynobj = addto_User(myobj, new, new2)

	if mynobj.time == expect2:
		assert True
	else:
		assert False

	try:
		np.testing.assert_equal(myobj.HR, expect)
	except AssertionError:
		assert False


@pytest.mark.parametrize('new, new1, new2, expect3', [

	(2, 21, ['str2'], False),
	('str', 21, ['str2'], True),
	(2, 'str', ['str2'], False),
	(2, 21, 'str', True),
	([2], [21], 1, True),
	(2.0, 21.0, ['str2'], True),


	])
def test_addtoUser2(new, new1, new2, expect3):
	myobj = create_NewUser('hold', 1, 1, 0.0, ['str', 'str'], '1')

	try:
		mynobj = addto_User(myobj, new, new2)
		myb =False
	except TypeError:
		myb = True
	finally:
		assert myb == expect3