import folium
import pandas

 
data = pandas.read_csv("vol.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

# %22 is " (double quote)
 
myhtml = """
Volcano2 name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
<br>
Height: %s m
"""
 
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map Debashis")
 
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=myhtml % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(locat    ion=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))

f = open("world.json", "r") 

fg.add_child(folium.GeoJson(data=open("world.json",'r', encoding='utf-8-sig').read()))
 
map.add_child(fg)
map.save("Map_html_popup_advanced1.html")