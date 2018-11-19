import requests

if __name__ == '__main__':
    r2 = requests.post(
        "http://127.0.0.1:5000/heart_rate/interval_average",
        json={
            "patient_id": "2",
            "heart_rate_average_since": "2017-03-09 11:00:36.372339"})

    print(r2.json())
