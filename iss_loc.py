import requests, json
from pprint import pprint
r = requests.get("http://api.open-notify.org/iss-now.json")
t = r.text
j = json.loads(t)

lat = j["iss_position"]["latitude"]
lon = j["iss_position"]["longitude"]

r_map = requests.get("https://api.opencagedata.com/geocode/v1/json?q={}+{}&key=bd49a407c01541c78557e1d80beb115b".format(lat,lon))
plot = r_map.text
plot_p = json.loads(plot)

p_country = plot_p["results"][0]["formatted"]

print("The ISS is currently above: {} ".format(p_country))
