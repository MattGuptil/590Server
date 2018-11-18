from user_class import User
from server_methods import *
import pytest
import numpy as np


@pytest.mark.parametrize('new,  expect', [

	('str', False),



	])
def test_checkNewU(new,  expect):
	myobj = create_NewUser('hold', 1, 1, 0.0, ['str', 'str'])
	myobj2 = create_NewUser('hold3', 1, 1, 0.0, ['str', 'str'])

	myUsers.append([myobj, myobj2])

	myRe = checkNewU(new)

	if myRe[0] == expect:
		assert True
	else:
		assert False

