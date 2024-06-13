import streamlit as st
from PIL import Image
import os

# Define the path to the images folder
image_folder = 'images'

# Load local JPEG images from the images folder
image1 = Image.open(os.path.join(image_folder, 'logo-no-background.png'))

st.image(image1, width=200)

st.write("---")

st.write(" ### Our Product & Mission")

st.write("At Takeoff, we provide cutting-edge software that empowers airlines with the ability to predict competitors' pricing strategies. Our solution offers real-time insights into market pricing, enabling airlines to stay ahead by adapting their pricing to current market trends. By leveraging our technology, clients can develop and fine-tune their pricing strategies to maximize revenue. Our mission is to deliver the data-driven tools necessary for our clients to achieve superior pricing strategies and maintain a competitive edge in the industry.")

st.write(" ### Our Team")

st.write("Takeoff is fueled by a dynamic team of data science enthusiasts from the Data Science & AI Bootcamp at Le Wagon in Madrid. Our team consists of Adrian, Nils, and Alex. Adrian has a dual background in economics and computer science, and he is an aspiring product manager. Alex, with a degree in economics and business, is passionate about data science and its potential. Nils, the youngest member of our team, has recently finished high school and is excited to dive into the tech world. Together, our diverse backgrounds and shared enthusiasm drive the innovation and success of Takeoff.")

import streamlit as st
from PIL import Image
import os

# Define the path to the images folder
image_folder = 'images'

# Load local JPEG images from the images folder
image1 = Image.open(os.path.join(image_folder, 'Adrian_Headshot.JPEG'))
image2 = Image.open(os.path.join(image_folder, 'Alex_Headshot.JPEG'))
image3 = Image.open(os.path.join(image_folder, 'Nils_Headshot.JPEG'))

# Create three columns in Streamlit
col1, col2, col3 = st.columns(3)

# Display images in each column with optional captions
with col1:
    st.image(image1, caption='Adrian Marino', use_column_width=True)
with col2:
    st.image(image2, caption='Alexandre Büchler', use_column_width=True)
with col3:
    st.image(image3, caption='Nils Bischof', use_column_width=True)