import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])



def color_points(elevation):
    if elevation < 1000:
        return "orange"
    elif 1001<= elevation <= 3000:
        return "blue"
    else:
        return "green"


map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=el, icon = folium.Icon(color=color_points(el))))
map.add_child(fg)
map.save("Map1.html")