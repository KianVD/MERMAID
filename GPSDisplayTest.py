import folium

#create map
m = folium.Map(location=[32.78171, -117.24964],tiles="OpenStreetMap", zoom_start=13) #Cartodb Positron
#add group and pin
group_1 = folium.FeatureGroup("Buoys").add_to(m)
folium.Marker([32.78171, -117.24964], tooltip="Buoy1",icon=folium.Icon("red")).add_to(group_1)
#layer control option
folium.LayerControl().add_to(m)
#save to html
m.save("my_map.html")
