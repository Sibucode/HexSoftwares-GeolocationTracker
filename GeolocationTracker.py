from ipaddress import ip_address
from time import timezone
import folium
import requests
import webbrowser

ip_address = input("Enter an IP address (or press Enter to use your public IP): ").strip()
if not ip_address:
    ip_address = requests.get('http://api.ipify.org').text

try:
    response = requests.get(f'http://ip-api.com/json/{ip_address}?fields=status,message,continent,country,region,regionName,city,district,lat,lon,currency,proxy').json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    exit()


if response["status"] == "success":
    city = response["city"]
    district = response["district"]
    latitude = response["lat"]
    longitude = response["lon"]
    country = response["country"]
    currency_value = response["currency"]  
    region = response["region"]
    regionName = response["regionName"]
    continent = response["continent"]
    proxy = response["proxy"]

    # Formating the popup text
    popup_text = f"""
        City: {city} <br>
        District: {district} <br>
        Country: {country} <br>
        Currency: {currency_value} <br>
        Region: {region} <br>
        RegionName: {regionName} <br>
        Continent: {continent} <br>
        Proxy: {'Yes' if proxy else 'No'}
    """

    # Creating a map centered at the given location
    app = folium.Map(location=[latitude, longitude], zoom_start=10)

    # Adding a marker for the location with the popup
    folium.Marker(
        location=[latitude, longitude],
        popup=folium.Popup(popup_text, max_width=320),
        icon=folium.Icon(color="blue")
    ).add_to(app)

    
    file_name = "LocationMap.html"
    app.save(file_name)
    print(f"Map File successfully saved as {file_name}")
    webbrowser.open(file_name)
else:
    print("There was a problem with opening the file, please review the code")
