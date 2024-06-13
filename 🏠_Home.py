import streamlit as st
import requests

import streamlit as st
from PIL import Image
import os

# Define the path to the images folder
image_folder = 'images'

# Load local JPEG images from the images folder
image1 = Image.open(os.path.join(image_folder, 'logo-no-background.png'))

st.image(image1, width=200)

st.write("---")

st.write("## Eurowings' Origin and Destination Airports")

st.write("Use the interactive map below to explore")

st.write("---")

#Interactive Map
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster

# Load data (replace with your own data)
eurowings_origins = [(52.519, 13.406), (48.353, 11.774)]  # Example origin airports (latitude, longitude)
eurowings_destinations = [(51.289, 6.766), (41.898, 12.5)]  # Example destination airports (latitude, longitude)

# Create a map centered around Europe
m = folium.Map(location=[51.1657, 10.4515], zoom_start=5)

# Add marker clusters for origin and destination airports
origin_cluster = MarkerCluster().add_to(m)
for coord in eurowings_origins:
    folium.Marker(coord, popup='Origin Airport').add_to(origin_cluster)

destination_cluster = MarkerCluster().add_to(m)
for coord in eurowings_destinations:
    folium.Marker(coord, popup='Destination Airport').add_to(destination_cluster)

# Render the map using folium_static
folium_static(m)


st.sidebar.success('Select a Page')