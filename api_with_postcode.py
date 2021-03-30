# API for postcode.io
import requests

url = "http://api.postcodes.io/postcodes/"
postcode = "AL51QN"

url_arg = url + postcode
print(url_arg)

# Check its status
response = requests.get(url_arg)
print(response.status_code)

# Put response into a dictionary with json().
response_dict = response.json()
result_dict = response_dict["result"]
# print(type(response_dict))

# Accessing dictionary
for key, val in result_dict.items():
    print(key, val)

# Accessing contents
# print(response.content)
# print(response.headers.keys())
# print(response.encoding.isdigit())
# print(response.is_redirect)







