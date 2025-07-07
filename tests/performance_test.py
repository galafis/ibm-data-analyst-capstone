#!/usr/bin/env python3
"""Performance Test Module"""
import os
import sys
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import modules
from src.data_analyst_platform import DataAnalystPlatform

def generate_test_data(rows=1000, categories=5):
    """
    Generate test data
    
    Parameters:
    -----------
    rows : int
        Number of rows
    categories : int
        Number of categories
        
    Returns:
    --------
    pd.DataFrame
        Test data
    """
    return pd.DataFrame({
        'date': pd.date_range(start='2020-01-01', periods=rows, freq='D'),
        'value': np.random.normal(0, 1, rows),
        'category': np.random.choice([f'Category {i}' for i in range(categories)], rows),
        'revenue': np.random.uniform(1000, 5000, rows),
        'customers': np.random.randint(100, 500, rows)
    })

def test_pivot_performance(platform, data_sizes):
    """
    Test pivot performance
    
    Parameters:
    -----------
    platform : DataAnalystPlatform
        Platform instance
    data_sizes : list
        List of data sizes to test
        
    Returns:
    --------
    dict
        Performance results
    """
    results = {
        'data_size': [],
        'time': []
    }
    
    for size in data_sizes:
        data = generate_test_data(rows=size)
        
        start_time = time.time()
        platform.create_pivot(
            data,
            index='category',
            columns=None,
            values='revenue',
            aggfunc='sum'
        )
        end_time = time.time()
        
        results['data_size'].append(size)
        results['time'].append(end_time - start_time)
        
    return results

def test_kpi_performance(platform, data_sizes):
    """
    Test KPI performance
    
    Parameters:
    -----------
    platform : DataAnalystPlatform
        Platform instance
    data_sizes : list
        List of data sizes to test
        
    Returns:
    --------
    dict
        Performance results
    """
    results = {
        'data_size': [],
        'time': []
    }
    
    kpi_config = {
        'revenue_growth': {
            'type': 'revenue_growth',
            'period_col': 'date',
            'revenue_col': 'revenue'
        }
    }
    
    for size in data_sizes:
        data = generate_test_data(rows=size)
        
        start_time = time.time()
        platform.calculate_kpis(data, kpi_config)
        end_time = time.time()
        
        results['data_size'].append(size)
        results['time'].append(end_time - start_time)
        
    return results

def test_trend_performance(platform, data_sizes):
    """
    Test trend performance
    
    Parameters:
    -----------
    platform : DataAnalystPlatform
        Platform instance
    data_sizes : list
        List of data sizes to test
        
    Returns:
    --------
    dict
        Performance results
    """
    results = {
        'data_size': [],
        'time': []
    }
    
    for size in data_sizes:
        data = generate_test_data(rows=size)
        
        start_time = time.time()
        platform.analyze_trends(
            data,
            date_col='date',
            value_col='value'
        )
        end_time = time.time()
        
        results['data_size'].append(size)
        results['time'].append(end_time - start_time)
        
    return results

def test_forecast_performance(platform, data_sizes):
    """
    Test forecast performance
    
    Parameters:
    -----------
    platform : DataAnalystPlatform
        Platform instance
    data_sizes : list
        List of data sizes to test
        
    Returns:
    --------
    dict
        Performance results
    """
    results = {
        'data_size': [],
        'time': []
    }
    
    for size in data_sizes:
        data = generate_test_data(rows=size)
        
        start_time = time.time()
        platform.forecast(
            data,
            date_col='date',
            value_col='value',
            steps=10,
            model_type='arima',
            model_params={'order': (1, 1, 1)}
        )
        end_time = time.time()
        
        results['data_size'].append(size)
        results['time'].append(end_time - start_time)
        
    return results

def plot_results(results, title):
    """
    Plot performance results
    
    Parameters:
    -----------
    results : dict
        Performance results
    title : str
        Plot title
        
    Returns:
    --------
    matplotlib.figure.Figure
        Plot figure
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(results['data_size'], results['time'], marker='o')
    
    ax.set_title(title)
    ax.set_xlabel('Data Size (rows)')
    ax.set_ylabel('Time (seconds)')
    ax.grid(True)
    
    return fig

def main():
    """Main function"""
    platform = DataAnalystPlatform()
    platform.initialize_modules()
    
    data_sizes = [100, 500, 1000, 5000, 10000]
    
    # Test pivot performance
    pivot_results = test_pivot_performance(platform, data_sizes)
    pivot_fig = plot_results(pivot_results, 'Pivot Performance')
    pivot_fig.savefig('pivot_performance.png')
    
    # Test KPI performance
    kpi_results = test_kpi_performance(platform, data_sizes)
    kpi_fig = plot_results(kpi_results, 'KPI Performance')
    kpi_fig.savefig('kpi_performance.png')
    
    # Test trend performance
    trend_results = test_trend_performance(platform, data_sizes)
    trend_fig = plot_results(trend_results, 'Trend Performance')
    trend_fig.savefig('trend_performance.png')
    
    # Test forecast performance
    forecast_results = test_forecast_performance(platform, data_sizes)
    forecast_fig = plot_results(forecast_results, 'Forecast Performance')
    forecast_fig.savefig('forecast_performance.png')
    
    print("Performance tests completed")
    print("Pivot performance:", pivot_results)
    print("KPI performance:", kpi_results)
    print("Trend performance:", trend_results)
    print("Forecast performance:", forecast_results)

if __name__ == '__main__':
    main()
