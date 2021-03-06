import streamlit as st

# Custom imports
from multiapp import MultiApp
from apps import news_content, sport_content, home # import your pages here

app = MultiApp()

st.markdown("""
# Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("News", news_content.app)
app.add_app("Sports", sport_content.app)
app.add_app("Home", home.app)

# The main app
app.run()
