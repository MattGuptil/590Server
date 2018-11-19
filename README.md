# 590Server
Code for Web Services Assignment


VM:
  http://vcm-7280.vm.duke.edu:5000
Run:
    If server is not running already, then run server.py. This is the Flask server. 
    If it is running then simply use normal requests from flask request library to POST and GET.
   
Notes:
    If you enter incorrect fields or values you will get a TypeError. At this point server should not crash. Simply edit
    the fields that were incorrect and rerun your POST script.
    You will also get a TypeError if you try to create a user with the same patient id. PATIENT IDs MUST BE UNIQUE. 
    
    The file server.py contains all the flask functions as well as all the helper functions that it uses. There is a separate file
    call server_methods that has the same methods as server.py but server_methods is called for unit tests.
    
    Tests are spread out for each function there are like 111 tests. There are 2 functions that are not tested these are emailTac and validate_request. emailTac is tested through testserver2.py and testmyserver.py. This is because this is a sendgrid function and I can not verify programatically so I did it manually. validate_request is not tested because this code was taken from Suyash's server implementation that was demonstrated in class. Furthermore this function uses the flask requests objects and we don't need to test the flask stuff.
    
 Also emails will be sent when patient properly goes tachycardic, so watch for the emails only when you knowingly push the HR up.
 
 Sphinx docstring thing is all created so it should work fine. If if does not email me. I have a working html version, but I heard some people were having trouble opening theirs up so you never know.
 
URLS:
  POST
  http://vcm-7280.vm.duke.edu:5000/new_patient
  http://vcm-7280.vm.duke.edu:5000/heart_rate
  http://vcm-7280.vm.duke.edu:5000/heart_rate/interval_average
  
  GET
  http://vcm-7280.vm.duke.edu:5000/status/<patient_id>
  http://vcm-7280.vm.duke.edu:5000/heart_rate/average/<patient_id>
  http://vcm-7280.vm.duke.edu:5000/heart_rate/<patient_id>
  
