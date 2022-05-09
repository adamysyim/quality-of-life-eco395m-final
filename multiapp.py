import streamlit as st


class MultiApp:
    
    def __init__(self):
    
        self.streamlit_apps = []

    def add_app(self, title, func):
    
        self.streamlit_apps.append({
            'title': title,
            'function': func
        })

    def run(self):
    
        app = st.selectbox(
            'Navigation',
            self.streamlit_apps,
            format_func=lambda app: app['title'])

        app['function']()
