import requests

if __name__ == '__main__':
	r2 = requests.post("http://127.0.0.1:5000/heart_rate", json={"patient_id": "2", "heart_rate": 50})

	print(r2.json())