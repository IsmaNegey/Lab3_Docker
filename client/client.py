import requests
import time

# ждем сервер (важно для Docker)
time.sleep(3)

url = "http://server:5000/greet"

data = {
    "name": "Isma"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())


#запуск
#docker -compose up --build