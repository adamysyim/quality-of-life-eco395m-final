import streamlit as st
from multiapp import MultiApp
from apps import overview, individual, compare # import your app modules here

st.set_page_config(layout='wide')

app = MultiApp()

st.markdown("""
# Multi-Page App

This multi-page app is based on figures from www.numbeo.com

You can navigate through multiple pages to see Quality of Life Index data

""")

# Adding all the applications
app.add_app('Overview', overview.app)
app.add_app('Individual City', individual.app)
app.add_app('Comparison', compare.app)

# The main app
app.run()
