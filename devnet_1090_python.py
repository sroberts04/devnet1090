
# Query An API - https://jsonplaceholder.typicode.com/users
# Parse the Data
# Loop over it and run conditionals
# Run it every hour

import json, re, requests

target_host = "https://jsonplaceholder.typicode.com"
target_port = 443
target_endpoint = "/users"
user_name_to_find = "Bret"

#Query API
#Normal Get call to return the Users data

url = target_host + ":" + str(target_port) + target_endpoint
response = requests.get(url = url)

#Parse the Data
#Return the Status Code of API and the Output Body

code = response.status_code
output = response.json()

#Loop over it and run conditionals
#Given an input name -> find it in the structure

user_record = {}
user_name = ""

for user in output:
    if user.get("username") == user_name_to_find:
        user_record = user
        user_name = user["name"]

print(f"The username {user_name_to_find} is owned by the user {user_name}.")

#Run it every hour

#Here we would need another system, like linux hosting
#Assuming linux, we would need to setup a cron job, like
#0 * * * * /usr/bin/python3 /full/path/to/demo.py
