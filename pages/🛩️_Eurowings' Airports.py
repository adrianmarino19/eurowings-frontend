import streamlit as st
import requests

import streamlit as st
from PIL import Image
import os

# Custom CSS to style the line
st.markdown(
    """
    <style>
    .red-line {
        border: 0;
        height: 2px;
        background: red;
        background-image: linear-gradient(to right, red, #ffcccc, red);
        margin: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# # Custom CSS to style the line
# st.markdown(
#     """
#     <style>
#     .red-line {
#         border: 0;
#         height: 2px;
#         background: red;
#         margin: 10px 0;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


#####
# Define the path to the images folder
image_folder = 'images'

# Load local JPEG images from the images folder
image1 = Image.open(os.path.join(image_folder, '1.png'))

col1, col2, col3, col4, col5, col6  = st.columns(6)
with col3:
    st.image(image1, width=200)


st.write("## Eurowings' Origin and Destination Airports")

st.write("Use the interactive map below to explore")

# Custom colored line
st.markdown('<hr class="red-line">', unsafe_allow_html=True)

#Interactive Map
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster

import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# Load data (replace with your own data)
eurowings_airports = [
    (52.3667, 13.5033),  # Berlin Brandenburg (BER)
    (53.0475, 8.7867),   # Bremen (BRE)
    (50.8659, 7.1427),   # Cologne-Bonn (CGN)
    (51.5183, 7.6122),   # Dortmund (DTM)
    (51.1236, 13.7675),  # Dresden (DRS)
    (51.2895, 6.7668),   # Dusseldorf (DUS)
    (53.6304, 9.9882),   # Hamburg (HAM)
    (52.4611, 9.685),    # Hanover (HAJ)
    (48.7794, 8.0805),   # Karlsruhe/Baden-Baden (FKB)
    (51.4324, 12.2416),  # Leipzig/Halle (LEJ)
    (47.9881, 10.2396),  # Memmingen (FMM)
    (48.3538, 11.7861),  # Munich (MUC)
    (52.1346, 7.6848),   # Münster/Osnabrück (FMO)
    (49.4987, 11.0647),  # Nuremberg (NUE)
    (51.6141, 8.6163),   # Paderborn/Lippstadt (PAD)
    (49.2146, 7.1095),   # Saarbrücken (SCN)
    (48.6899, 9.2219),   # Stuttgart (STR)
    (54.9133, 8.3405),   # Sylt (GWT)
    (51.6022, 6.1422),   # Weeze (NRN)
    (47.0001, 15.4396),  # Graz (GRZ)
    (47.2602, 11.3439),  # Innsbruck (INN)
    (48.2333, 14.1875),  # Linz (LNZ)
    (47.7933, 13.0033),  # Salzburg (SZG)
    (48.1103, 16.5697),  # Vienna (VIE)
    (47.5906, 7.5299),   # Basel (BSL)
    (46.2381, 6.1096),   # Geneva (GVA)
    (47.4581, 8.5481),   # Zurich (ZRH)
    (37.9364, 23.9475),  # Athens (ATH)
    (41.2969, 2.0785),   # Barcelona (BCN)
    (41.1389, 16.7606),  # Bari (BRI)
    (37.4667, 15.0667),  # Catania (CTA)
    (42.5603, 18.261),   # Dubrovnik (DBV)
    (37.0144, -7.9659),  # Faro (FAO)
    (35.3361, 25.1803),  # Heraklion (HER)
    (38.8729, 1.3731),   # Ibiza (IBZ)
    (38.7756, -9.1354),  # Lisbon (LIS)
    (45.6301, 8.7231),   # Milan Malpensa (MXP)
    (40.8854, 14.2906),  # Naples (NAP)
    (43.6584, 7.2159),   # Nice (NCE)
    (39.5517, 2.7388),   # Palma de Mallorca (PMI)
    (41.8003, 12.2389),  # Rome Fiumicino (FCO)
    (43.5389, 16.2983),  # Split (SPU)
    (40.5197, 22.9709),  # Thessaloniki (SKG)
    (39.4916, -0.4758),  # Valencia (VLC)
    (45.5053, 12.3519),  # Venice Marco Polo (VCE)
    (45.7429, 16.0688),  # Zagreb (ZAG)
    (47.4298, 19.2611),  # Budapest (BUD)
    (44.5722, 26.1022),  # Bucharest Henri Coanda (OTP)
    (53.4273, -6.2436),  # Dublin (DUB)
    (38.2924, 27.1539),  # Izmir (ADB)
    (49.0097, 2.5479),   # Paris Charles de Gaulle (CDG)
    (50.1008, 14.2632),  # Prague (PRG)
    (43.8246, 18.3315),  # Sarajevo (SJJ)
    (51.4775, -0.4614),  # London Heathrow (LHR)
    (53.365, -2.2728),   # Manchester (MAN)
    (54.9881, -1.6194),  # Newcastle (NCL)
    (50.4406, -5.0048)   # Newquay (NQY)
]


# Create a map centered around Europe
m = folium.Map(location=[51.1657, 10.4515], zoom_start=5)

# Add marker clusters for airports
airport_cluster = MarkerCluster().add_to(m)
for coord in eurowings_airports:
    folium.Marker(coord, popup='Eurowings Airport').add_to(airport_cluster)

# Render the map using folium_static
folium_static(m)



st.sidebar.success('Select a Page')
