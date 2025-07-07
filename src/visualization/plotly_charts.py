#!/usr/bin/env python3
"""Plotly Charts Module"""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import os

class PlotlyCharts:
    def __init__(self, theme='plotly'):
        self.theme = theme
        pio.templates.default = theme
        
    def create_bar_chart(self, data, x, y, title=None, color=None, orientation='v'):
        """
        Create a bar chart
        
        Parameters:
        -----------
        data : pd.DataFrame
            Data to plot
        x : str
            Column name for x-axis
        y : str
            Column name for y-axis
        title : str
            Chart title
        color : str
            Column name for color
        orientation : str
            'v' for vertical, 'h' for horizontal
            
        Returns:
        --------
        plotly.graph_objects.Figure
            Plotly figure
        """
        fig = px.bar(data, x=x, y=y, color=color, title=title, orientation=orientation)
        return fig
        
    def create_line_chart(self, data, x, y, title=None, color=None, line_shape='linear'):
        """
        Create a line chart
        
        Parameters:
        -----------
        data : pd.DataFrame
            Data to plot
        x : str
            Column name for x-axis
        y : str
            Column name for y-axis
        title : str
            Chart title
        color : str
            Column name for color
        line_shape : str
            Shape of the line ('linear', 'spline', etc.)
            
        Returns:
        --------
        plotly.graph_objects.Figure
            Plotly figure
        """
        fig = px.line(data, x=x, y=y, color=color, title=title, line_shape=line_shape)
        return fig
        
    def create_scatter_plot(self, data, x, y, title=None, color=None, size=None, hover_name=None):
        """
        Create a scatter plot
        
        Parameters:
        -----------
        data : pd.DataFrame
            Data to plot
        x : str
            Column name for x-axis
        y : str
            Column name for y-axis
        title : str
            Chart title
        color : str
            Column name for color
        size : str
            Column name for point size
        hover_name : str
            Column name for hover text
            
        Returns:
        --------
        plotly.graph_objects.Figure
            Plotly figure
        """
        fig = px.scatter(data, x=x, y=y, color=color, size=size, hover_name=hover_name, title=title)
        return fig
        
    def create_pie_chart(self, data, values, names, title=None, hole=0):
        """
        Create a pie chart
        
        Parameters:
        -----------
        data : pd.DataFrame
            Data to plot
        values : str
            Column name for values
        names : str
            Column name for names
        title : str
            Chart title
        hole : float
            Size of the hole (0-1, 0 for pie, >0 for donut)
            
        Returns:
        --------
        plotly.graph_objects.Figure
            Plotly figure
        """
        fig = px.pie(data, values=values, names=names, title=title, hole=hole)
        return fig
        
    def create_histogram(self, data, x, nbins=None, title=None, color=None):
        """
        Create a histogram
        
        Parameters:
        -----------
        data : pd.DataFrame
            Data to plot
        x : str
            Column name for values
        nbins : int
            Number of bins
        title : str
            Chart title
        color : str
            Column name for color
            
        Returns:
        --------
        plotly.graph_objects.Figure
            Plotly figure
        """
        fig = px.histogram(data, x=x, nbins=nbins, color=color, title=title)
        return fig
        
    def create_box_plot(self, data, x, y, title=None, color=None):
        """
        Create a box plot
        
        Parameters:
        -----------
        data : pd.DataFrame
            Data to plot
        x : str
            Column name for x-axis
        y : str
            Column name for y-axis
        title : str
            Chart title
        color : str
            Column name for color
            
        Returns:
        --------
        plotly.graph_objects.Figure
            Plotly figure
        """
        fig = px.box(data, x=x, y=y, color=color, title=title)
        return fig
        
    def create_heatmap(self, data, title=None, colorscale='Viridis'):
        """
        Create a heatmap
        
        Parameters:
        -----------
        data : pd.DataFrame
            Data to plot (should be a correlation matrix or similar)
        title : str
            Chart title
        colorscale : str
            Colorscale name
            
        Returns:
        --------
        plotly.graph_objects.Figure
            Plotly figure
        """
        fig = go.Figure(data=go.Heatmap(
            z=data.values,
            x=data.columns,
            y=data.index,
            colorscale=colorscale
        ))
        
        if title:
            fig.update_layout(title=title)
            
        return fig
        
    def save_figure(self, fig, output_path, format='html'):
        """
        Save a figure to a file
        
        Parameters:
        -----------
        fig : plotly.graph_objects.Figure
            Plotly figure to save
        output_path : str
            Path to save the figure
        format : str
            Format to save ('html', 'png', 'jpg', 'svg', 'pdf')
            
        Returns:
        --------
        bool
            True if successful
        """
        try:
            if format == 'html':
                pio.write_html(fig, file=output_path)
            else:
                pio.write_image(fig, file=output_path, format=format)
            return True
        except Exception as e:
            print(f"Error saving figure: {e}")
            return False
