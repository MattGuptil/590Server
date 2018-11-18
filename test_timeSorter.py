from user_class import User
from server_methods import *
import pytest
import numpy as np

## Additional testing for exceptions is not necessary here because this function
## can only be called on an object and does not take anyinputs other than itself.


@pytest.mark.parametrize('mid, expect', [

	('-1', {'Avg Heart Rate over your Interval': 75.5})
	

	])
def test_timeSorter(mid, expect):
	myobj = create_NewUser('hold', 0, 21, 0.0, [' '], '-1')
	myUsers.append(myobj)
	myV = addto_User(myobj, 101, ['2018-03-09 11:00:36.372339'])
	myV = addto_User(myobj, 50, ['2018-03-09 11:05:36.372339'])
	myt = datetime.datetime.strptime('2018-03-09 10:05:36.372339', "%Y-%m-%d %I:%M:%S.%f")
	mydic = timeSorter(mid, myt)

	if mydic == expect:
		assert True
	else:
		assert False
