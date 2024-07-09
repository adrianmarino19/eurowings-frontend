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
    (51.5183, 7.6122),   # Dortmund (DTM)
    (51.1236, 13.7675),  # Dresden (DRS)
    (51.2895, 6.7668),   # Dusseldorf (DUS)
    (50.9792, 11.3225),  # Erfurt (ERF)
    (50.0333, 8.5706),   # Frankfurt/Main (FRA)
    (53.6304, 9.9882),   # Hamburg (HAM)
    (52.4611, 9.685),    # Hanover (HAJ)
    (48.7794, 8.0805),   # Karlsruhe/Baden-Baden (FKB)
    (50.8659, 7.1427),   # Cologne-Bonn (CGN)
    (51.4324, 12.2416),  # Leipzig/Halle (LEJ)
    (47.9881, 10.2396),  # Memmingen (FMM)
    (48.3538, 11.7861),  # Munich (MUC)
    (52.1346, 7.6848),   # Münster/Osnabrück (FMO)
    (49.4987, 11.0781),  # Nuremberg (NUE)
    (51.6141, 8.6163),   # Paderborn/Lippstadt (PAD)
    (49.2146, 7.1095),   # Saarbrücken (SCN)
    (48.6899, 9.2219),   # Stuttgart (STR)
    (54.9133, 8.3405),   # Sylt (GWT)
    
    (27.1783, 33.7994),  # Hurghada (HRG)
    (30.1219, 31.4056),  # Kairo (CAI)
    (25.5556, 34.5836),  # Marsa Alam (RMF)
    (41.4147, 19.7206),  # Tirana (TIA)
    (40.1473, 44.3959),  # Jerewan (EVN)
    (50.4592, 4.4538),   # Brüssel-Charleroi (CRL)
    (43.8246, 18.3315),  # Sarajevo (SJJ)
    (42.5696, 27.5152),  # Burgas (BOJ)
    (43.2321, 27.8251),  # Varna (VAR)
    (55.6181, 12.6561),   # Kopenhagen (CPH)
    
    (59.4133, 24.8328),   # Tallinn (TLL)
    (60.3172, 24.9633),   # Helsinki (HEL)
    (68.6073, 27.4053),   # Ivalo (IVL)
    (64.2855, 27.6924),   # Kajaani (KAJ)
    (67.701, 24.8468),    # Kittilä (Finnisch Lappland) (KTT)
    (65.9876, 29.2394),   # Kuusamo (KAO)
    (66.5648, 25.8304),   # Rovaniemi (RVN)
    (41.9236, 8.8029),    # Ajaccio (AJA)
    (42.5521, 9.4837),    # Bastia (Korsika) (BIA)
    (43.4683, -1.5233),   # Biarritz (BIQ)
    (44.8283, -0.7156),   # Bordeaux (BOD)
    (48.447, -4.4185),    # Brest (BES)
    (42.5308, 8.7932),    # Calvi (Korsika) (CLY)
    (41.5006, 9.0978),    # Figari (Korsika) (FSC)
    (50.5619, 3.0894),    # Lille (LIL)
    (43.1852, -0.0064),   # Lourdes (LDE)
    (45.7256, 5.0811),    # Lyon (LYS)
    (43.4393, 5.2214),    # Marseille (MRS)
    (43.5763, 3.963),     # Montpellier (MPL)
    (47.1532, -1.6107),   # Nantes (NTE)
    (43.6584, 7.2159),    # Nizza (NCE)
    (48.7253, 2.3592),    # Paris (ORY)
    (49.0097, 2.5479),    # Paris (CDG)
    (48.5383, 7.6282),    # Straßburg (SXB)
    (43.6293, 1.3678),     # Toulouse (TLS)
    
    (41.6692, 44.9547),   # Tiflis (TBS)
    (37.9364, 23.9475),   # Athen (ATH)
    (35.5317, 24.1497),   # Chania (Kreta) (CHQ)
    (35.3397, 25.1803),   # Heraklion (Kreta) (HER)
    (37.0683, 22.0256),   # Kalamata (KLX)
    (35.4214, 27.146),    # Karpathos (AOK)
    (40.9133, 24.6197),   # Kavala (KVA)
    (39.6019, 19.9117),   # Korfu (CFU)
    (36.7933, 27.0917),   # Kos (KGS)
    (37.4361, 25.3481),   # Mykonos (JMK)
    (38.9253, 20.7653),   # Preveza (PVK)
    (36.4054, 28.0862),   # Rhodos (RHO)
    (37.6911, 26.9117),   # Samos (SMI)
    (36.4042, 25.4793),   # Santorin (JTR)
    (40.5197, 22.9709),   # Thessaloniki (SKG)
    (39.2194, 22.7943),   # Volos (VOL)
    (37.7509, 20.8843),   # Zakynthos (ZTH)
    (52.4539, -1.748),    # Birmingham (BHX)
    (55.95, -3.3725),     # Edinburgh (EDI)
    (49.2079, -2.1956),   # Jersey (JER)
    (51.4706, -0.4619),   # London-Heathrow (LHR)
    (53.3537, -2.275),    # Manchester (MAN)
    (55.0375, -1.6917),   # Newcastle (NCL)
    (50.4406, -4.9954),   # Newquay (St. Mawgan Airport) (NQY)
    (36.2376, 43.9632),   # Erbil (EBL)
    (53.4213, -6.2701),   # Dublin (DUB)
    (63.985, -22.6056),   # Reykjavik (KEF)
    (32.0114, 34.8867),    # Tel Aviv (TLV)
    
    (41.1389, 16.7606),  # Bari (Apulien) (BRI)
    (44.5354, 11.2887),  # Bologna (BLQ)
    (40.6576, 17.947),   # Brindisi (BDS)
    (39.2515, 9.0543),   # Cagliari (Sardinien) (CAG)
    (37.4668, 15.0664),  # Catania (Sizilien) (CTA)
    (43.81, 11.2051),    # Florenz (FLR)
    (38.9054, 16.2423),  # Lamezia Terme (SUF)
    (45.6689, 9.7003),   # Mailand Bergamo (BGY)
    (45.6301, 8.7231),   # Mailand Malpensa (MXP)
    (40.8843, 14.2908),  # Neapel (NAP)
    (40.8987, 9.5176),   # Olbia (Sardinien) (OLB)
    (38.1759, 13.0904),  # Palermo (PMO)
    (43.6839, 10.3929),  # Pisa (Toskana) (PSA)
    (41.8003, 12.2389),  # Rom Fiumicino (FCO)
    (45.5053, 12.3519),  # Venedig (Marco Polo) (VCE)
    (45.3957, 10.8885),  # Verona (VRN)
    (42.5728, 21.035),   # Pristina (PRN)
    (42.5614, 18.2683),  # Dubrovnik (DBV)
    (44.8935, 13.9222),  # Pula (PUY)
    (45.2169, 14.5703),  # Rijeka (RJK)
    (43.5389, 16.298),   # Split (SPU)
    (44.1083, 15.3467),  # Zadar (ZAD)
    (45.7429, 16.0688),   # Zagreb (ZAG)
    
    (33.8209, 35.4884),   # Beirut (BEY)
    (49.6266, 6.2115),    # Luxemburg (LUX)
    (35.8575, 14.4775),   # Malta (MLA)
    (30.325, -9.4131),    # Agadir (AGA)
    (33.3675, -7.5898),   # Casablanca (CMN)
    (33.9273, -4.978),    # Fes-Saiss (FEZ)
    (31.6069, -8.0363),   # Marrakesch (RAK)
    (34.9888, -3.0282),   # Nador (NDR)
    (35.7269, -5.9169),   # Tanger (TNG)
    (42.4047, 18.7233),   # Tivat (TIV)
    (60.2934, 5.2181),    # Bergen (BGO)
    (60.2028, 11.0839),   # Oslo (OSL)
    (69.6833, 18.9189),   # Tromsø (TOS)
    (46.995, 15.4396),    # Graz (GRZ)
    (47.2602, 11.344),    # Innsbruck (Tirol) (INN)
    (48.2332, 14.1875),   # Linz (LNZ)
    (47.7933, 13.0043),   # Salzburg (SZG)
    (48.1103, 16.5697),   # Wien (VIE)
    (54.3775, 18.4661),   # Danzig (GDN)
    (50.0777, 19.7848),    # Krakau (KRK)
    
    (37.0144, -7.9659),   # Faro (FAO)
    (32.6979, -16.7745),  # Funchal (Madeira) (FNC)
    (38.7756, -9.1354),   # Lissabon (LIS)
    (41.2421, -8.6786),   # Porto (OPO)
    (46.9275, 28.9309),   # Chișinău (KIV)
    (44.5711, 26.085),    # Bukarest (Henri Coanda) (OTP)
    (21.6796, 39.1565),   # Dschidda (JED)
    (57.6628, 12.2798),   # Göteborg (GOT)
    (67.821, 20.3368),    # Kiruna (KRN)
    (59.6519, 17.9186),   # Stockholm (ARN)
    (47.59, 7.5299),      # Basel (BSL)
    (46.2381, 6.1089),    # Genf (Geneve) (GVA)
    (47.4581, 8.5555),    # Zürich (ZRH)
    (44.8184, 20.3091),   # Belgrad (BEG)
    (38.2822, -0.5582),   # Alicante (ALC)
    (41.2974, 2.0833),    # Barcelona (BCN)
    (43.3011, -2.9106),   # Bilbao (BIO)
    (28.4527, -13.8638),  # Fuerteventura (FUE)
    (38.8729, 1.3731),    # Ibiza (IBZ)
    (36.7446, -6.0601),   # Jerez de la Frontera (XRY)
    (28.9455, -13.6052),  # Lanzarote (ACE)
    (27.9319, -15.3866),  # Las Palmas/Gran Canaria (LPA)
    (36.6749, -4.4991),   # Malaga (AGP)
    (39.8626, 4.2186),    # Menorca (MAH)
    (39.5517, 2.7388),    # Palma de Mallorca (PMI)
    (28.6265, -17.7556),  # Sta. Cruz de la Palma (SPC)
    (28.0445, -16.5725),  # Teneriffa Süd (TFS)
    (39.4893, -0.4816),    # Valencia (VLC)
    
    (50.1008, 14.26),     # Prag (PRG)
    (35.7581, 10.7547),   # Monastir (MIR)
    (36.851, 10.227),     # Tunis (TUN)
    (37.0017, 35.2803),   # Adana (ADA)
    (36.8987, 30.8005),   # Antalya (AYT)
    (38.2924, 27.157),    # Izmir (ADB)
    (38.7704, 35.4954),   # Kayseri (ASR)
    (39.1131, 30.1281),   # Kütahya Zafer (KZR)
    (41.2544, 36.5673),   # Samsun Carsamba (SZF)
    (47.4369, 19.2556),   # Budapest (BUD)
    (25.2532, 55.3657),   # Dubai (DXB)
    (24.8964, 55.1614),   # Dubai-World Central (DWC)
    (34.8751, 33.6249)    # Larnaca (LCA)
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
