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
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=el,
        fill_color=color_points(el), color="gray", fill_opacity = 0.7))

fg.add_child(folium.GeoJson(data=open('world.json','r', encoding="utf-8-sig").read(),
    style_function=lambda x:{ 'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 
    else 'orange'  if 10000001 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fg)
map.save("Map1.html")