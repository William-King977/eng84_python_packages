import requests


# Used to check the weather based on a latitude and longitude
def weather_checker(response):
    # Put response into a dictionary with json().
    response_dict = response.json()
    result_dict = response_dict["result"]

    longitude = result_dict["longitude"]
    latitude = result_dict["latitude"]

    url_arg = f"https://www.metaweather.com/api/location/search/?lattlong={latitude},{longitude}"
    response = requests.get(url_arg)

    # Fetch woeid needed for getting the weather.
    result_list = response.json()
    location_dict = result_list[0]
    woeid = location_dict["woeid"]

    # Get the weather with the woeid
    url_weather = f"https://www.metaweather.com/api/location/{woeid}"
    response = requests.get(url_weather)
    result = response.json()
    print(result) # Need to fetch the weather from the results.



# Asks for a postcode and checks if it's valid
while True:
    postcode = input("Enter a postcode (without a space): ")
    if postcode.lower() == "exit":
        break

    # Create a request
    url = "http://api.postcodes.io/postcodes/"
    url_arg = url + postcode
    response = requests.get(url_arg)

    if not response:
        print("This postcode is invalid.")
    else:
        weather_checker(response)


