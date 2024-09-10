import requests

# URL of the Python script to download
url = "https://raw.githubusercontent.com/UniDCYT/Egirl/main/AiEgirl.py"

# Fetch the script from the URL
response = requests.get(url)
script_content = response.text

# Save the script to a file
with open("AiEgirl.py", "w") as file:
    file.write(script_content)

# Execute the script
exec(script_content)
