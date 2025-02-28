# HexSoftwares-GeolocationTracker

This Python project retrieves geolocation data from an IP address and displays it on an interactive map using the Folium library. It allows users to enter an IP address (or automatically fetches the public IP) and presents detailed location information, including city, country, currency, region, and more, on a map.

Features

*Geolocation Data: Fetches city, district, country, region, continent, and currency information based on the IP address.
*Interactive Map: Displays the location on a map with a marker showing the geolocation details.
*Proxy Detection: Checks if the IP address is using a proxy.

Requirements
To run this project, you'll need to have Python 3.x installed along with the following libraries:

*requests
*folium
You can install the required libraries using pip:

pip install requests folium

Usage
Clone the repository or download the project files.

Run the script in your terminal:

python geolocation_map.py

Enter an IP address when prompted. If you don't provide one, the script will automatically fetch your public IP.

The script will retrieve the geolocation data and create an HTML file named LocationMap.html.

Open the LocationMap.html file to view the interactive map with the geolocation data.

Example
After running the script, the map will display a marker with the following details in the popup:

City
District
Country
Currency
Region
Region Name
Continent
Proxy status
Code Overview


# Code to fetch and process IP address, get geolocation data and display on a map

How It Works

IP Address Input: The user can provide an IP address or allow the program to fetch their public IP automatically using Ipify.
Geolocation API: The project uses the IP-API service to fetch geolocation data.
Folium Map: The Folium library is used to create an interactive map centered on the IP's location.
Popup Details: A popup is shown on the map marker containing the location details.
Contributing

Feel free to open issues or submit pull requests if you want to contribute or suggest improvements to this project.

