import requests

url = "http://localhost:5000/api"
response = requests.request("GET", url)
test_response = response.text


if test_response == "success":
    print("Unit Test Success")

else:
    raise AssertionError
