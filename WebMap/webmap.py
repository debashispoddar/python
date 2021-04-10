import folium
import pandas
map1=folium.Map(location=[38.58, -99.09] , zoom_start=6 , tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Debashis Map")

data = pandas.read_csv("vol.txt")
print(data.columns)
print(data)
lat = list(data["LAT"]) #creating a list from dataframe
lon = list(data["LON"]) #creating a list from dataframe
elev = list(data["ELEV"])
print(len(lat))
print(len(lon))

for lt,ln,el in zip(lat,lon, elev):
    fg.add_child(folium.Marker(location =[lt,ln],popup=el, icon=folium.Icon(color="green")))


map1.add_child(fg)
map1.save("Map1.html")


