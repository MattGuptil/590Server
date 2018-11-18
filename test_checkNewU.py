from user_class import User
from server_methods import *
import pytest
import numpy as np


@pytest.mark.parametrize('new,  expect', [

	('str', False),
	('1', True),
	('2', True)



	])
def test_checkNewU(new,  expect):
	myobj = create_NewUser('hold', 1, 1, 0.0, ['str', 'str'], '1')
	myobj2 = create_NewUser('hold3', 1, 1, 0.0, ['str', 'str'], '2')

	myUsers.append(myobj)
	myUsers.append(myobj2)
	
	myRe = checkNewU(new)

	if myRe[0] == expect:
		assert True
	else:
		assert False



@pytest.mark.parametrize('new,  expect', [

	('str', False),
	('hold', False),
	('hold3', False),
	(1, True),
	(1.0, True),
	(None, True),
	(['hold3'], True),



	])
def test_checkNewU2(new,  expect):
	myobj = create_NewUser('hold', 1, 1, 0.0, ['str', 'str'], '1')
	myobj2 = create_NewUser('hold3', 1, 1, 0.0, ['str', 'str'], '1')

	myUsers.append(myobj)
	myUsers.append(myobj2)
	
	try:
		myRe = checkNewU(new)
		myb = False
	except TypeError:
		myb = True
	finally:
		assert myb == expect

