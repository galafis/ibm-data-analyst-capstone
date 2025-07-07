#!/usr/bin/env python3
"""Data Analyst Platform"""
import pandas as pd
import plotly.express as px

class DataAnalystPlatform:
    def __init__(self):
        self.data = None
    
    def load_excel_data(self, file_path):
        self.data = pd.read_excel(file_path)
        return self.data
    
    def create_dashboard(self, data):
        fig = px.bar(data, x='category', y='value')
        return fig

if __name__ == "__main__":
    print("Data Analyst Platform initialized")
