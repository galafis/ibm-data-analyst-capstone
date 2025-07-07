#!/usr/bin/env python3
"""Forecast Engine Module"""
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

class ForecastEngine:
    def __init__(self, data=None):
        self.data = data
        self.model = None
        self.forecast = None
        
    def load_data(self, data, date_col=None, value_col=None):
        """
        Load data for forecasting
        
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
            
    def train_arima_model(self, column=None, order=(1, 1, 1)):
        """
        Train ARIMA model
        
        Parameters:
        -----------
        column : str
            Column name to forecast (if None, use the first column)
        order : tuple
            ARIMA order (p, d, q)
            
        Returns:
        --------
        statsmodels.tsa.arima.model.ARIMAResults
            Trained model
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # If column is not specified, use the first column
        if column is None:
            column = self.data.columns[0]
            
        # Train ARIMA model
        self.model = ARIMA(self.data[column], order=order)
        self.model = self.model.fit()
        
        return self.model
        
    def train_sarima_model(self, column=None, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)):
        """
        Train SARIMA model
        
        Parameters:
        -----------
        column : str
            Column name to forecast (if None, use the first column)
        order : tuple
            ARIMA order (p, d, q)
        seasonal_order : tuple
            Seasonal order (P, D, Q, s)
            
        Returns:
        --------
        statsmodels.tsa.statespace.sarimax.SARIMAXResults
            Trained model
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # If column is not specified, use the first column
        if column is None:
            column = self.data.columns[0]
            
        # Train SARIMA model
        self.model = SARIMAX(self.data[column], order=order, seasonal_order=seasonal_order)
        self.model = self.model.fit(disp=False)
        
        return self.model
        
    def train_linear_regression(self, column=None, features=None):
        """
        Train linear regression model
        
        Parameters:
        -----------
        column : str
            Column name to forecast (if None, use the first column)
        features : list
            List of feature column names (if None, use all columns except target)
            
        Returns:
        --------
        sklearn.linear_model.LinearRegression
            Trained model
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # If column is not specified, use the first column
        if column is None:
            column = self.data.columns[0]
            
        # If features are not specified, use all columns except target
        if features is None:
            features = [col for col in self.data.columns if col != column]
            
        # Train linear regression model
        X = self.data[features]
        y = self.data[column]
        
        self.model = LinearRegression()
        self.model.fit(X, y)
        
        return self.model
        
    def forecast_future(self, steps=10, column=None):
        """
        Forecast future values
        
        Parameters:
        -----------
        steps : int
            Number of steps to forecast
        column : str
            Column name to forecast (if None, use the first column)
            
        Returns:
        --------
        pd.Series
            Forecasted values
        """
        if self.model is None:
            raise ValueError("No model trained")
            
        # If column is not specified, use the first column
        if column is None:
            column = self.data.columns[0]
            
        # Forecast
        if isinstance(self.model, (ARIMA, SARIMAX)):
            # For ARIMA/SARIMA models
            self.forecast = self.model.forecast(steps=steps)
        elif isinstance(self.model, LinearRegression):
            # For linear regression models
            # This is a simplified implementation
            # In a real scenario, you would need to generate future feature values
            raise NotImplementedError("Forecasting with linear regression is not implemented")
        else:
            raise ValueError(f"Unsupported model type: {type(self.model)}")
            
        return self.forecast
        
    def evaluate_forecast(self, test_data, column=None):
        """
        Evaluate forecast
        
        Parameters:
        -----------
        test_data : pd.DataFrame
            Test data
        column : str
            Column name to evaluate (if None, use the first column)
            
        Returns:
        --------
        dict
            Dictionary with evaluation metrics
        """
        if self.forecast is None:
            raise ValueError("No forecast available")
            
        # If column is not specified, use the first column
        if column is None:
            column = test_data.columns[0]
            
        # Evaluate
        y_true = test_data[column]
        y_pred = self.forecast
        
        # Calculate metrics
        mse = mean_squared_error(y_true, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_true, y_pred)
        
        return {
            'mse': mse,
            'rmse': rmse,
            'mae': mae
        }
        
    def plot_forecast(self, test_data=None, column=None):
        """
        Plot forecast
        
        Parameters:
        -----------
        test_data : pd.DataFrame
            Test data (if None, only plot forecast)
        column : str
            Column name to plot (if None, use the first column)
            
        Returns:
        --------
        matplotlib.figure.Figure
            Plot figure
        """
        if self.forecast is None:
            raise ValueError("No forecast available")
            
        # If column is not specified, use the first column
        if column is None:
            column = self.data.columns[0]
            
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Plot training data
        ax.plot(self.data.index, self.data[column], label='Training Data')
        
        # Plot test data if provided
        if test_data is not None:
            ax.plot(test_data.index, test_data[column], label='Test Data')
            
        # Plot forecast
        ax.plot(self.forecast.index, self.forecast, label='Forecast', color='red')
        
        # Add labels and legend
        ax.set_title('Time Series Forecast')
        ax.set_xlabel('Date')
        ax.set_ylabel(column)
        ax.legend()
        
        return fig
