#!/usr/bin/env python3
"""Test Platform Module"""
import unittest
import os
import sys
import pandas as pd
import numpy as np

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import modules
from src.data_analyst_platform import DataAnalystPlatform

class TestDataAnalystPlatform(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.platform = DataAnalystPlatform()
        self.platform.initialize_modules()
        
        # Create test data
        self.test_data = pd.DataFrame({
            'date': pd.date_range(start='2020-01-01', periods=100, freq='D'),
            'value': np.random.normal(0, 1, 100),
            'category': np.random.choice(['A', 'B', 'C'], 100),
            'revenue': np.random.uniform(1000, 5000, 100),
            'customers': np.random.randint(100, 500, 100)
        })
        
    def test_create_pivot(self):
        """Test create_pivot method"""
        pivot = self.platform.create_pivot(
            self.test_data,
            index='category',
            columns=None,
            values='revenue',
            aggfunc='sum'
        )
        
        self.assertIsInstance(pivot, pd.DataFrame)
        self.assertEqual(pivot.index.name, 'category')
        self.assertEqual(pivot.shape[0], 3)  # 3 categories
        
    def test_calculate_kpis(self):
        """Test calculate_kpis method"""
        kpi_config = {
            'revenue_growth': {
                'type': 'revenue_growth',
                'period_col': 'date',
                'revenue_col': 'revenue'
            }
        }
        
        kpi_results = self.platform.calculate_kpis(self.test_data, kpi_config)
        
        self.assertIsInstance(kpi_results, dict)
        self.assertIn('revenue_growth', kpi_results)
        self.assertIsInstance(kpi_results['revenue_growth'], pd.DataFrame)
        
    def test_analyze_trends(self):
        """Test analyze_trends method"""
        trend_results = self.platform.analyze_trends(
            self.test_data,
            date_col='date',
            value_col='value'
        )
        
        self.assertIsInstance(trend_results, dict)
        self.assertIn('decomposition', trend_results)
        self.assertIn('stationarity', trend_results)
        self.assertIn('moving_average', trend_results)
        self.assertIn('exponential_smoothing', trend_results)
        self.assertIn('outliers', trend_results)
        
    def test_forecast(self):
        """Test forecast method"""
        forecast = self.platform.forecast(
            self.test_data,
            date_col='date',
            value_col='value',
            steps=10,
            model_type='arima',
            model_params={'order': (1, 1, 1)}
        )
        
        self.assertIsInstance(forecast, pd.Series)
        self.assertEqual(len(forecast), 10)

if __name__ == '__main__':
    unittest.main()
