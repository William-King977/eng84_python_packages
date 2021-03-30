import requests


class WeatherChecker():

    # Initialise URLs for the APIs used.
    def __init__(self):
        self.weather_url = "https://www.metaweather.com/api/"
        self.postcode_url = "http://api.postcodes.io/postcodes/"

    # Check if a postcode is valid by sending a request.
    def is_postcode_valid(self, postcode):
        full_postcode_url = self.postcode_url + postcode
        response = requests.get(full_postcode_url)
        if response:
            return True
        else:
            return False

    # Returns the longitude and latitude based on the postcode.
    def postcode_to_longitude_latitude(self, postcode):
        full_postcode_url = self.postcode_url + postcode
        response = requests.get(full_postcode_url)

        # Put response into a dictionary with json().
        response_dict = response.json()
        result_dict = response_dict["result"]

        return result_dict["longitude"], result_dict["latitude"]

    # Displays the weather using longitude and latitude. Makes use of the
    # woeid version of this method to display the weather.
    def display_weather_longlat(self, longitude, latitude):
        url_arg = self.weather_url + f"location/search/?lattlong={latitude},{longitude}"
        response = requests.get(url_arg)

        # Fetch woeid needed for getting the weather.
        result_list = response.json()
        # Gets the closest location to the long/lat.
        location_dict = result_list[0]
        woeid = location_dict["woeid"]

        # Display the weather with woeid method.
        self.display_weather_woeid(woeid)

    # Displays the weather based on the woeid.
    def display_weather_woeid(self, woeid):
        # Get the weather with the woeid.
        url_weather = self.weather_url + f"location/{woeid}"
        response = requests.get(url_weather)
        result = response.json()

        # Output the weather for the next few days.
        weather_dict = result["consolidated_weather"]
        for item in weather_dict:
            print(f"Weather: {item['weather_state_name']}, Date: {item['applicable_date']}")


if __name__ == "__main__":
    # Asks for a postcode and checks the weather for that area.
    while True:
        postcode = input("Enter a postcode (without a space): ")
        if postcode.lower() == "exit":
            break

        # Create a weather checker object
        wc = WeatherChecker()

        # Validate the postcode, then display the weather if it is valid.
        if wc.is_postcode_valid(postcode):
            longitude, latitude = wc.postcode_to_longitude_latitude(postcode)
            wc.display_weather_longlat(longitude, latitude)
        else:
            print("This postcode is invalid.")


