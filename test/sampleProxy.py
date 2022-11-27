from pip._vendor import requests

if __name__ == "__main__":
    BASE_URL = "http://localhost:8080"

    response = requests.get(f"{BASE_URL}/v1/urlinfo/www.google.com")
    print(response.headers)
    print(response.status_code)
    print(response.content)
    print(response.json())