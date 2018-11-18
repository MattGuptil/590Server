import requests

if __name__ == '__main__':
	r2 = requests.post("http://127.0.0.1:5000/new_patient", json={"patient_id": "2", "attending_email": "suyash.kumar@duke.edu", "user_age": 50})

	print(r2.json())