#!/usr/bin/env python3
"""Dashboard Builder Module"""
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html
import os

class DashboardBuilder:
    def __init__(self, title="Data Analysis Dashboard"):
        self.title = title
        self.figures = []
        self.layout = []
        
    def add_chart(self, fig, title=None, width=6, height=400):
        """
        Add a chart to the dashboard
        
        Parameters:
        -----------
        fig : plotly.graph_objects.Figure
            Plotly figure to add
        title : str
            Chart title
        width : int
            Width in grid units (12 is full width)
        height : int
            Height in pixels
            
        Returns:
        --------
        int
            Index of the added chart
        """
        if title:
            fig.update_layout(title=title)
            
        self.figures.append({
            'fig': fig,
            'width': width,
            'height': height
        })
        
        return len(self.figures) - 1
        
    def set_layout(self, layout):
        """
        Set the layout of the dashboard
        
        Parameters:
        -----------
        layout : list
            List of lists, each inner list represents a row
            Each item in the inner list is an index of a chart
            
        Returns:
        --------
        bool
            True if successful
        """
        # Validate layout
        for row in layout:
            for chart_idx in row:
                if chart_idx >= len(self.figures):
                    raise ValueError(f"Chart index {chart_idx} is out of range")
        
        self.layout = layout
        return True
        
    def create_dash_app(self, server=None):
        """
        Create a Dash app
        
        Parameters:
        -----------
        server : flask.Flask
            Flask server to use
            
        Returns:
        --------
        dash.Dash
            Dash app
        """
        app = dash.Dash(__name__, server=server)
        
        # Create layout
        children = [
            html.H1(self.title)
        ]
        
        if self.layout:
            # Use custom layout
            for row_idx, row in enumerate(self.layout):
                row_children = []
                for chart_idx in row:
                    chart = self.figures[chart_idx]
                    row_children.append(
                        html.Div(
                            dcc.Graph(
                                figure=chart['fig'],
                                style={'height': f"{chart['height']}px"}
                            ),
                            className=f"col-{chart['width']}"
                        )
                    )
                children.append(html.Div(row_children, className="row"))
        else:
            # Default layout: one chart per row
            for chart in self.figures:
                children.append(
                    html.Div(
                        html.Div(
                            dcc.Graph(
                                figure=chart['fig'],
                                style={'height': f"{chart['height']}px"}
                            ),
                            className=f"col-{chart['width']}"
                        ),
                        className="row"
                    )
                )
        
        app.layout = html.Div(children, className="container")
        return app
        
    def create_html_dashboard(self, output_path):
        """
        Create an HTML dashboard
        
        Parameters:
        -----------
        output_path : str
            Path to save the HTML file
            
        Returns:
        --------
        bool
            True if successful
        """
        try:
            # Create a subplot figure
            if self.layout:
                # Calculate grid dimensions
                rows = len(self.layout)
                cols = max(len(row) for row in self.layout)
            else:
                # Default layout: one chart per row
                rows = len(self.figures)
                cols = 1
                
            fig = make_subplots(rows=rows, cols=cols, subplot_titles=[chart.get('title', '') for chart in self.figures])
            
            if self.layout:
                # Use custom layout
                for row_idx, row in enumerate(self.layout):
                    for col_idx, chart_idx in enumerate(row):
                        chart_fig = self.figures[chart_idx]['fig']
                        for trace in chart_fig.data:
                            fig.add_trace(trace, row=row_idx+1, col=col_idx+1)
            else:
                # Default layout: one chart per row
                for i, chart in enumerate(self.figures):
                    chart_fig = chart['fig']
                    for trace in chart_fig.data:
                        fig.add_trace(trace, row=i+1, col=1)
            
            fig.update_layout(title=self.title, height=rows*400)
            fig.write_html(output_path)
            return True
        except Exception as e:
            print(f"Error creating HTML dashboard: {e}")
            return False
        
    def run_dash_app(self, host='0.0.0.0', port=8050, debug=False):
        """
        Run the Dash app
        
        Parameters:
        -----------
        host : str
            Host to run on
        port : int
            Port to run on
        debug : bool
            Whether to run in debug mode
            
        Returns:
        --------
        None
        """
        app = self.create_dash_app()
        app.run_server(host=host, port=port, debug=debug)
