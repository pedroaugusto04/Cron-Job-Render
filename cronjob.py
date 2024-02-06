import requests

api_url = 'https://hackathon-orange.onrender.com/ping'

try:
    response = requests.get(api_url)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error in API request. Status Code: {response.status_code}")

except requests.RequestException as e:
    print(f"Error in API request: {e}")
