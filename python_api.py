# Python requests package
# Connecting to the live web using python requests api
# We will connect to www.bbc.com and check if the web is live
import requests

# Status 200 meams the website is live running
# Status 400 or 404 means not working
responses = requests.get("http://www.bbc.co.uk/")
# if responses.status_code == 200:
#     print(f"The website is up and running {responses.status_code}.")
# else:
#     print(f"Oops, something went wrong {responses.status_code}.")
#
#
# # Create a function called status code check
# # function should return the status code with an appropriate message.
# def status_code_check(website_url):
#     response = requests.get(website_url)
#     if response.status_code == 200:
#         return f"The website is up and running {response.status_code}."
#     elif response.status_code == 400 or response.status_code == 404:
#         return f"Oops, something went wrong {response.status_code}."
#     else:
#         return "This website does not exist."
#
# # Running the function
# print(status_code_check("http://www.bbc.co.uk/"))
# print(status_code_check("https://www.worldsultimatestrongman.com/"))


# Requests go one step further in simplifying this process for us
# If you use response instance in a condition expression,
# it will evaluate to True if the status code was between 200 and 4000, False otherwise
# therefore, you can simplify the last example by rewriting the if statement as above
response = requests.get("https://marvelapp.com/prototype/404/?")
if response:
    print(f"Success {response.status_code}.")
else:
    print(f"Oops, something went wrong {response}.")


