from user_class import User
from server_methods import create_NewUser
import pytest
import numpy as np

## Additional testing for exceptions is not necessary here because this function
## can only be called on an object and does not take anyinputs other than itself.


@pytest.mark.parametrize('oldhr, expect', [

	(0, 0),
	(60, 60),
	(-20, -20),
	

	])
def test_calcAvg(oldhr, expect):
	myobj = create_NewUser('hold', oldhr, 1, 0.0, ['str'])

	myobj.calc_AvgHR()

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
	myobj = create_NewUser('hold', oldhr, 1, 0.0, ['str'])
	for x in range(10):
		myobj.add_HR(oldhr)

	myobj.calc_AvgHR()

	if myobj.AvgHR == expect:
		assert True
	else:
		assert False