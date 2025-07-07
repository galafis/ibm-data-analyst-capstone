#!/usr/bin/env python3
"""Pivot Generator Module"""
import pandas as pd
import numpy as np

class PivotGenerator:
    def __init__(self, data):
        if isinstance(data, str):
            # Assume it's a file path
            self.data = pd.read_excel(data)
        elif isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise ValueError("Data must be a DataFrame or a file path")

    def create_pivot(self, index, columns, values, aggfunc='sum'):
        """
        Create a pivot table
        
        Parameters:
        -----------
        index : str or list
            Column(s) to use as index
        columns : str or list
            Column(s) to use as columns
        values : str or list
            Column(s) to aggregate
        aggfunc : str or function
            Aggregation function to use
            
        Returns:
        --------
        pd.DataFrame
            Pivot table
        """
        return pd.pivot_table(
            self.data,
            index=index,
            columns=columns,
            values=values,
            aggfunc=aggfunc
        )

    def export_to_excel(self, pivot_table, output_path, sheet_name='Pivot'):
        """
        Export pivot table to Excel
        
        Parameters:
        -----------
        pivot_table : pd.DataFrame
            Pivot table to export
        output_path : str
            Path to save the Excel file
        sheet_name : str
            Name of the sheet
            
        Returns:
        --------
        bool
            True if successful
        """
        try:
            pivot_table.to_excel(output_path, sheet_name=sheet_name)
            return True
        except Exception as e:
            print(f"Error exporting pivot table: {e}")
            return False
