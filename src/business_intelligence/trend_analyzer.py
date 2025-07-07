#!/usr/bin/env python3
"""Trend Analyzer Module"""
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

class TrendAnalyzer:
    def __init__(self, data=None):
        self.data = data
        
    def load_data(self, data, date_col=None, value_col=None):
        """
        Load data for trend analysis
        
        Parameters:
        -----------
        data : pd.DataFrame or str
            Data to load (DataFrame or path to file)
        date_col : str
            Column name for date
        value_col : str
            Column name for value
            
        Returns:
        --------
        bool
            True if successful
        """
        try:
            if isinstance(data, str):
                if data.endswith('.csv'):
                    self.data = pd.read_csv(data)
                elif data.endswith(('.xls', '.xlsx')):
                    self.data = pd.read_excel(data)
                else:
                    raise ValueError(f"Unsupported file format: {data}")
            else:
                self.data = data
                
            # Set index to date column if specified
            if date_col:
                # Convert date column to datetime if it's not already
                if not pd.api.types.is_datetime64_dtype(self.data[date_col]):
                    self.data[date_col] = pd.to_datetime(self.data[date_col])
                    
                # Set index
                self.data = self.data.set_index(date_col)
                
                # If value column is specified, keep only that column
                if value_col:
                    self.data = self.data[[value_col]]
                    
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
            
    def decompose_time_series(self, column=None, model='additive', period=None):
        """
        Decompose time series into trend, seasonal, and residual components
        
        Parameters:
        -----------
        column : str
            Column name to decompose (if None, use the first column)
        model : str
            Decomposition model ('additive' or 'multiplicative')
        period : int
            Period for seasonal decomposition (if None, infer from data)
            
        Returns:
        --------
        statsmodels.tsa.seasonal.DecomposeResult
            Decomposition result
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # If column is not specified, use the first column
        if column is None:
            column = self.data.columns[0]
            
        # If period is not specified, infer from data
        if period is None:
            # For monthly data, use 12
            if self.data.index.freqstr == 'M':
                period = 12
            # For quarterly data, use 4
            elif self.data.index.freqstr == 'Q':
                period = 4
            # For weekly data, use 52
            elif self.data.index.freqstr == 'W':
                period = 52
            # For daily data, use 7
            elif self.data.index.freqstr == 'D':
                period = 7
            # Default to 12
            else:
                period = 12
                
        # Decompose
        result = seasonal_decompose(self.data[column], model=model, period=period)
        
        return result
        
    def test_stationarity(self, column=None):
        """
        Test stationarity of time series
        
        Parameters:
        -----------
        column : str
            Column name to test (if None, use the first column)
            
        Returns:
        --------
        dict
            Dictionary with test results
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # If column is not specified, use the first column
        if column is None:
            column = self.data.columns[0]
            
        # Run Augmented Dickey-Fuller test
        result = adfuller(self.data[column].dropna())
        
        # Format results
        output = {
            'test_statistic': result[0],
            'p_value': result[1],
            'lags': result[2],
            'observations': result[3],
            'critical_values': result[4],
            'is_stationary': result[1] < 0.05
        }
        
        return output
        
    def calculate_moving_average(self, column=None, window=7):
        """
        Calculate moving average
        
        Parameters:
        -----------
        column : str
            Column name to calculate (if None, use the first column)
        window : int
            Window size for moving average
            
        Returns:
        --------
        pd.Series
            Moving average series
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # If column is not specified, use the first column
        if column is None:
            column = self.data.columns[0]
            
        # Calculate moving average
        ma = self.data[column].rolling(window=window).mean()
        
        return ma
        
    def calculate_exponential_smoothing(self, column=None, alpha=0.3):
        """
        Calculate exponential smoothing
        
        Parameters:
        -----------
        column : str
            Column name to calculate (if None, use the first column)
        alpha : float
            Smoothing factor (0 < alpha < 1)
            
        Returns:
        --------
        pd.Series
            Exponential smoothing series
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # If column is not specified, use the first column
        if column is None:
            column = self.data.columns[0]
            
        # Calculate exponential smoothing
        es = self.data[column].ewm(alpha=alpha).mean()
        
        return es
        
    def detect_outliers(self, column=None, method='zscore', threshold=3):
        """
        Detect outliers in time series
        
        Parameters:
        -----------
        column : str
            Column name to detect outliers (if None, use the first column)
        method : str
            Method to detect outliers ('zscore' or 'iqr')
        threshold : float
            Threshold for outlier detection
            
        Returns:
        --------
        pd.Series
            Boolean series indicating outliers
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # If column is not specified, use the first column
        if column is None:
            column = self.data.columns[0]
            
        # Detect outliers
        if method == 'zscore':
            # Z-score method
            z = (self.data[column] - self.data[column].mean()) / self.data[column].std()
            outliers = abs(z) > threshold
        elif method == 'iqr':
            # IQR method
            q1 = self.data[column].quantile(0.25)
            q3 = self.data[column].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - threshold * iqr
            upper_bound = q3 + threshold * iqr
            outliers = (self.data[column] < lower_bound) | (self.data[column] > upper_bound)
        else:
            raise ValueError(f"Unsupported method: {method}")
            
        return outliers
