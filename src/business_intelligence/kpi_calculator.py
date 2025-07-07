#!/usr/bin/env python3
"""KPI Calculator Module"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class KPICalculator:
    def __init__(self, data=None):
        self.data = data
        
    def load_data(self, data):
        """
        Load data for KPI calculation
        
        Parameters:
        -----------
        data : pd.DataFrame or str
            Data to load (DataFrame or path to file)
            
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
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
            
    def calculate_revenue_growth(self, period_col, revenue_col, periods=None):
        """
        Calculate revenue growth
        
        Parameters:
        -----------
        period_col : str
            Column name for period (date or period name)
        revenue_col : str
            Column name for revenue
        periods : list
            List of periods to include (if None, use all periods)
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with revenue growth by period
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # Create a copy of the data
        df = self.data.copy()
        
        # Filter periods if specified
        if periods:
            df = df[df[period_col].isin(periods)]
            
        # Sort by period
        df = df.sort_values(period_col)
        
        # Calculate revenue growth
        df['revenue_growth'] = df[revenue_col].pct_change() * 100
        
        return df[[period_col, revenue_col, 'revenue_growth']]
        
    def calculate_customer_acquisition_cost(self, period_col, marketing_expense_col, new_customers_col, periods=None):
        """
        Calculate customer acquisition cost
        
        Parameters:
        -----------
        period_col : str
            Column name for period (date or period name)
        marketing_expense_col : str
            Column name for marketing expense
        new_customers_col : str
            Column name for new customers
        periods : list
            List of periods to include (if None, use all periods)
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with customer acquisition cost by period
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # Create a copy of the data
        df = self.data.copy()
        
        # Filter periods if specified
        if periods:
            df = df[df[period_col].isin(periods)]
            
        # Sort by period
        df = df.sort_values(period_col)
        
        # Calculate customer acquisition cost
        df['cac'] = df[marketing_expense_col] / df[new_customers_col]
        
        return df[[period_col, marketing_expense_col, new_customers_col, 'cac']]
        
    def calculate_customer_lifetime_value(self, customer_id_col, revenue_col, date_col=None, time_period=365):
        """
        Calculate customer lifetime value
        
        Parameters:
        -----------
        customer_id_col : str
            Column name for customer ID
        revenue_col : str
            Column name for revenue
        date_col : str
            Column name for date (if None, assume all data is for the same period)
        time_period : int
            Time period in days (default: 365 days = 1 year)
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with customer lifetime value by customer
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # Create a copy of the data
        df = self.data.copy()
        
        # Group by customer
        if date_col:
            # Convert date column to datetime if it's not already
            if not pd.api.types.is_datetime64_dtype(df[date_col]):
                df[date_col] = pd.to_datetime(df[date_col])
                
            # Calculate customer lifespan
            customer_stats = df.groupby(customer_id_col).agg({
                date_col: lambda x: (x.max() - x.min()).days,
                revenue_col: 'sum'
            }).reset_index()
            
            # Rename columns
            customer_stats.columns = [customer_id_col, 'lifespan_days', 'total_revenue']
            
            # Calculate CLV (annualized)
            customer_stats['clv'] = customer_stats['total_revenue'] / customer_stats['lifespan_days'] * time_period
            
            # Handle customers with only one purchase (lifespan = 0)
            customer_stats.loc[customer_stats['lifespan_days'] == 0, 'clv'] = customer_stats.loc[customer_stats['lifespan_days'] == 0, 'total_revenue']
        else:
            # If no date column, just sum revenue by customer
            customer_stats = df.groupby(customer_id_col).agg({
                revenue_col: 'sum'
            }).reset_index()
            
            # Rename columns
            customer_stats.columns = [customer_id_col, 'clv']
            
        return customer_stats
        
    def calculate_conversion_rate(self, period_col, visitors_col, conversions_col, periods=None):
        """
        Calculate conversion rate
        
        Parameters:
        -----------
        period_col : str
            Column name for period (date or period name)
        visitors_col : str
            Column name for visitors
        conversions_col : str
            Column name for conversions
        periods : list
            List of periods to include (if None, use all periods)
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with conversion rate by period
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # Create a copy of the data
        df = self.data.copy()
        
        # Filter periods if specified
        if periods:
            df = df[df[period_col].isin(periods)]
            
        # Sort by period
        df = df.sort_values(period_col)
        
        # Calculate conversion rate
        df['conversion_rate'] = df[conversions_col] / df[visitors_col] * 100
        
        return df[[period_col, visitors_col, conversions_col, 'conversion_rate']]
        
    def calculate_churn_rate(self, period_col, customers_start_col, customers_end_col, new_customers_col, periods=None):
        """
        Calculate churn rate
        
        Parameters:
        -----------
        period_col : str
            Column name for period (date or period name)
        customers_start_col : str
            Column name for customers at start of period
        customers_end_col : str
            Column name for customers at end of period
        new_customers_col : str
            Column name for new customers in period
        periods : list
            List of periods to include (if None, use all periods)
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with churn rate by period
        """
        if self.data is None:
            raise ValueError("No data loaded")
            
        # Create a copy of the data
        df = self.data.copy()
        
        # Filter periods if specified
        if periods:
            df = df[df[period_col].isin(periods)]
            
        # Sort by period
        df = df.sort_values(period_col)
        
        # Calculate churned customers
        df['churned_customers'] = df[customers_start_col] + df[new_customers_col] - df[customers_end_col]
        
        # Calculate churn rate
        df['churn_rate'] = df['churned_customers'] / df[customers_start_col] * 100
        
        return df[[period_col, customers_start_col, customers_end_col, new_customers_col, 'churned_customers', 'churn_rate']]
