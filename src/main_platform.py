#!/usr/bin/env python3
"""Main Platform Module"""
import argparse
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import modules
from src.excel.excel_analyzer import ExcelAnalyzer
from src.excel.pivot_generator import PivotGenerator
from src.visualization.plotly_charts import PlotlyCharts
from src.visualization.dashboard_builder import DashboardBuilder
from src.business_intelligence.kpi_calculator import KPICalculator
from src.business_intelligence.trend_analyzer import TrendAnalyzer
from src.business_intelligence.forecast_engine import ForecastEngine

class DataAnalystPlatform:
    def __init__(self):
        self.excel_analyzer = None
        self.pivot_generator = None
        self.plotly_charts = None
        self.dashboard_builder = None
        self.kpi_calculator = None
        self.trend_analyzer = None
        self.forecast_engine = None
        
    def initialize_modules(self):
        """Initialize all modules"""
        self.excel_analyzer = ExcelAnalyzer(None)
        self.pivot_generator = PivotGenerator(None)
        self.plotly_charts = PlotlyCharts()
        self.dashboard_builder = DashboardBuilder("IBM Data Analyst Dashboard")
        self.kpi_calculator = KPICalculator()
        self.trend_analyzer = TrendAnalyzer()
        self.forecast_engine = ForecastEngine()
        
    def analyze_excel(self, file_path):
        """
        Analyze Excel file
        
        Parameters:
        -----------
        file_path : str
            Path to Excel file
            
        Returns:
        --------
        dict
            Analysis results
        """
        self.excel_analyzer = ExcelAnalyzer(file_path)
        self.excel_analyzer.load_workbook()
        
        results = {}
        
        # Get sheet names
        sheet_names = self.excel_analyzer.get_sheet_names()
        results['sheet_names'] = sheet_names
        
        # Analyze each sheet
        sheet_analyses = {}
        for sheet_name in sheet_names:
            sheet_analyses[sheet_name] = self.excel_analyzer.analyze_sheet(sheet_name)
            
        results['sheet_analyses'] = sheet_analyses
        
        return results
        
    def create_pivot(self, data, index, columns, values, aggfunc='sum'):
        """
        Create pivot table
        
        Parameters:
        -----------
        data : pd.DataFrame or str
            Data to pivot
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
        self.pivot_generator = PivotGenerator(data)
        pivot = self.pivot_generator.create_pivot(index, columns, values, aggfunc)
        return pivot
        
    def create_dashboard(self, data, charts_config, title="IBM Data Analyst Dashboard"):
        """
        Create dashboard
        
        Parameters:
        -----------
        data : pd.DataFrame
            Data to visualize
        charts_config : list
            List of chart configurations
        title : str
            Dashboard title
            
        Returns:
        --------
        DashboardBuilder
            Dashboard builder object
        """
        self.dashboard_builder = DashboardBuilder(title)
        
        # Create charts
        for config in charts_config:
            chart_type = config.get('type', 'bar')
            chart_title = config.get('title', '')
            
            if chart_type == 'bar':
                fig = self.plotly_charts.create_bar_chart(
                    data,
                    x=config.get('x'),
                    y=config.get('y'),
                    title=chart_title,
                    color=config.get('color')
                )
            elif chart_type == 'line':
                fig = self.plotly_charts.create_line_chart(
                    data,
                    x=config.get('x'),
                    y=config.get('y'),
                    title=chart_title,
                    color=config.get('color')
                )
            elif chart_type == 'scatter':
                fig = self.plotly_charts.create_scatter_plot(
                    data,
                    x=config.get('x'),
                    y=config.get('y'),
                    title=chart_title,
                    color=config.get('color'),
                    size=config.get('size')
                )
            elif chart_type == 'pie':
                fig = self.plotly_charts.create_pie_chart(
                    data,
                    values=config.get('values'),
                    names=config.get('names'),
                    title=chart_title
                )
            else:
                continue
                
            self.dashboard_builder.add_chart(fig, title=chart_title)
            
        return self.dashboard_builder
        
    def calculate_kpis(self, data, kpi_config):
        """
        Calculate KPIs
        
        Parameters:
        -----------
        data : pd.DataFrame
            Data to analyze
        kpi_config : dict
            KPI configuration
            
        Returns:
        --------
        dict
            KPI results
        """
        self.kpi_calculator = KPICalculator(data)
        
        results = {}
        
        # Calculate KPIs based on configuration
        for kpi_name, config in kpi_config.items():
            kpi_type = config.get('type')
            
            if kpi_type == 'revenue_growth':
                results[kpi_name] = self.kpi_calculator.calculate_revenue_growth(
                    period_col=config.get('period_col'),
                    revenue_col=config.get('revenue_col'),
                    periods=config.get('periods')
                )
            elif kpi_type == 'customer_acquisition_cost':
                results[kpi_name] = self.kpi_calculator.calculate_customer_acquisition_cost(
                    period_col=config.get('period_col'),
                    marketing_expense_col=config.get('marketing_expense_col'),
                    new_customers_col=config.get('new_customers_col'),
                    periods=config.get('periods')
                )
            elif kpi_type == 'customer_lifetime_value':
                results[kpi_name] = self.kpi_calculator.calculate_customer_lifetime_value(
                    customer_id_col=config.get('customer_id_col'),
                    revenue_col=config.get('revenue_col'),
                    date_col=config.get('date_col'),
                    time_period=config.get('time_period', 365)
                )
            elif kpi_type == 'conversion_rate':
                results[kpi_name] = self.kpi_calculator.calculate_conversion_rate(
                    period_col=config.get('period_col'),
                    visitors_col=config.get('visitors_col'),
                    conversions_col=config.get('conversions_col'),
                    periods=config.get('periods')
                )
            elif kpi_type == 'churn_rate':
                results[kpi_name] = self.kpi_calculator.calculate_churn_rate(
                    period_col=config.get('period_col'),
                    customers_start_col=config.get('customers_start_col'),
                    customers_end_col=config.get('customers_end_col'),
                    new_customers_col=config.get('new_customers_col'),
                    periods=config.get('periods')
                )
                
        return results
        
    def analyze_trends(self, data, date_col, value_col, config=None):
        """
        Analyze trends
        
        Parameters:
        -----------
        data : pd.DataFrame
            Data to analyze
        date_col : str
            Column name for date
        value_col : str
            Column name for value
        config : dict
            Analysis configuration
            
        Returns:
        --------
        dict
            Trend analysis results
        """
        self.trend_analyzer = TrendAnalyzer()
        self.trend_analyzer.load_data(data, date_col, value_col)
        
        results = {}
        
        # Decompose time series
        if config is None or config.get('decompose', True):
            decomposition = self.trend_analyzer.decompose_time_series(
                column=value_col,
                model=config.get('model', 'additive') if config else 'additive',
                period=config.get('period') if config else None
            )
            
            results['decomposition'] = {
                'trend': decomposition.trend,
                'seasonal': decomposition.seasonal,
                'resid': decomposition.resid
            }
            
        # Test stationarity
        if config is None or config.get('test_stationarity', True):
            stationarity = self.trend_analyzer.test_stationarity(column=value_col)
            results['stationarity'] = stationarity
            
        # Calculate moving average
        if config is None or config.get('moving_average', True):
            window = config.get('ma_window', 7) if config else 7
            ma = self.trend_analyzer.calculate_moving_average(column=value_col, window=window)
            results['moving_average'] = ma
            
        # Calculate exponential smoothing
        if config is None or config.get('exponential_smoothing', True):
            alpha = config.get('es_alpha', 0.3) if config else 0.3
            es = self.trend_analyzer.calculate_exponential_smoothing(column=value_col, alpha=alpha)
            results['exponential_smoothing'] = es
            
        # Detect outliers
        if config is None or config.get('detect_outliers', True):
            method = config.get('outlier_method', 'zscore') if config else 'zscore'
            threshold = config.get('outlier_threshold', 3) if config else 3
            outliers = self.trend_analyzer.detect_outliers(column=value_col, method=method, threshold=threshold)
            results['outliers'] = outliers
            
        return results
        
    def forecast(self, data, date_col, value_col, steps=10, model_type='arima', model_params=None):
        """
        Forecast future values
        
        Parameters:
        -----------
        data : pd.DataFrame
            Data to forecast
        date_col : str
            Column name for date
        value_col : str
            Column name for value
        steps : int
            Number of steps to forecast
        model_type : str
            Type of model to use ('arima', 'sarima', 'linear')
        model_params : dict
            Model parameters
            
        Returns:
        --------
        pd.Series
            Forecasted values
        """
        self.forecast_engine = ForecastEngine()
        self.forecast_engine.load_data(data, date_col, value_col)
        
        # Set default model parameters
        if model_params is None:
            model_params = {}
            
        # Train model
        if model_type == 'arima':
            order = model_params.get('order', (1, 1, 1))
            self.forecast_engine.train_arima_model(column=value_col, order=order)
        elif model_type == 'sarima':
            order = model_params.get('order', (1, 1, 1))
            seasonal_order = model_params.get('seasonal_order', (1, 1, 1, 12))
            self.forecast_engine.train_sarima_model(column=value_col, order=order, seasonal_order=seasonal_order)
        elif model_type == 'linear':
            features = model_params.get('features')
            self.forecast_engine.train_linear_regression(column=value_col, features=features)
        else:
            raise ValueError(f"Unsupported model type: {model_type}")
            
        # Forecast
        forecast = self.forecast_engine.forecast_future(steps=steps, column=value_col)
        
        return forecast
        
    def run(self, args):
        """
        Run the platform
        
        Parameters:
        -----------
        args : argparse.Namespace
            Command-line arguments
            
        Returns:
        --------
        int
            Exit code
        """
        # Initialize modules
        self.initialize_modules()
        
        # Process command-line arguments
        if args.mode == 'excel':
            # Analyze Excel file
            if not args.file:
                print("Error: Excel file path is required")
                return 1
                
            results = self.analyze_excel(args.file)
            print(f"Excel analysis results: {results}")
            
        elif args.mode == 'pivot':
            # Create pivot table
            if not args.file:
                print("Error: Data file path is required")
                return 1
                
            # Load data
            if args.file.endswith('.csv'):
                data = pd.read_csv(args.file)
            elif args.file.endswith(('.xls', '.xlsx')):
                data = pd.read_excel(args.file)
            else:
                print(f"Error: Unsupported file format: {args.file}")
                return 1
                
            # Create pivot table
            if not args.index or not args.values:
                print("Error: Index and values are required for pivot table")
                return 1
                
            pivot = self.create_pivot(
                data,
                index=args.index,
                columns=args.columns,
                values=args.values,
                aggfunc=args.aggfunc or 'sum'
            )
            
            print(f"Pivot table created: {pivot}")
            
            # Export to Excel if output path is provided
            if args.output:
                self.pivot_generator.export_to_excel(pivot, args.output)
                print(f"Pivot table exported to: {args.output}")
                
        elif args.mode == 'dashboard':
            # Create dashboard
            if not args.file:
                print("Error: Data file path is required")
                return 1
                
            # Load data
            if args.file.endswith('.csv'):
                data = pd.read_csv(args.file)
            elif args.file.endswith(('.xls', '.xlsx')):
                data = pd.read_excel(args.file)
            else:
                print(f"Error: Unsupported file format: {args.file}")
                return 1
                
            # Create dashboard
            # This is a simplified implementation
            # In a real scenario, you would load chart configurations from a file
            charts_config = [
                {
                    'type': 'bar',
                    'title': 'Bar Chart',
                    'x': data.columns[0],
                    'y': data.columns[1]
                },
                {
                    'type': 'line',
                    'title': 'Line Chart',
                    'x': data.columns[0],
                    'y': data.columns[1]
                }
            ]
            
            dashboard = self.create_dashboard(data, charts_config, title=args.title or "IBM Data Analyst Dashboard")
            
            # Export dashboard if output path is provided
            if args.output:
                dashboard.create_html_dashboard(args.output)
                print(f"Dashboard exported to: {args.output}")
                
            # Run dashboard if requested
            if args.run:
                dashboard.run_dash_app(host='0.0.0.0', port=8050, debug=True)
                
        elif args.mode == 'kpi':
            # Calculate KPIs
            if not args.file:
                print("Error: Data file path is required")
                return 1
                
            # Load data
            if args.file.endswith('.csv'):
                data = pd.read_csv(args.file)
            elif args.file.endswith(('.xls', '.xlsx')):
                data = pd.read_excel(args.file)
            else:
                print(f"Error: Unsupported file format: {args.file}")
                return 1
                
            # Calculate KPIs
            # This is a simplified implementation
            # In a real scenario, you would load KPI configurations from a file
            kpi_config = {
                'revenue_growth': {
                    'type': 'revenue_growth',
                    'period_col': data.columns[0],
                    'revenue_col': data.columns[1]
                }
            }
            
            kpi_results = self.calculate_kpis(data, kpi_config)
            print(f"KPI results: {kpi_results}")
            
        elif args.mode == 'trend':
            # Analyze trends
            if not args.file:
                print("Error: Data file path is required")
                return 1
                
            # Load data
            if args.file.endswith('.csv'):
                data = pd.read_csv(args.file)
            elif args.file.endswith(('.xls', '.xlsx')):
                data = pd.read_excel(args.file)
            else:
                print(f"Error: Unsupported file format: {args.file}")
                return 1
                
            # Analyze trends
            if not args.date_col or not args.value_col:
                print("Error: Date and value columns are required for trend analysis")
                return 1
                
            trend_results = self.analyze_trends(data, args.date_col, args.value_col)
            print(f"Trend analysis results: {trend_results}")
            
        elif args.mode == 'forecast':
            # Forecast future values
            if not args.file:
                print("Error: Data file path is required")
                return 1
                
            # Load data
            if args.file.endswith('.csv'):
                data = pd.read_csv(args.file)
            elif args.file.endswith(('.xls', '.xlsx')):
                data = pd.read_excel(args.file)
            else:
                print(f"Error: Unsupported file format: {args.file}")
                return 1
                
            # Forecast
            if not args.date_col or not args.value_col:
                print("Error: Date and value columns are required for forecasting")
                return 1
                
            forecast = self.forecast(
                data,
                args.date_col,
                args.value_col,
                steps=args.steps or 10,
                model_type=args.model_type or 'arima'
            )
            
            print(f"Forecast: {forecast}")
            
        else:
            print(f"Error: Unsupported mode: {args.mode}")
            return 1
            
        return 0

def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description='IBM Data Analyst Platform')
    
    # Mode
    parser.add_argument('--mode', choices=['excel', 'pivot', 'dashboard', 'kpi', 'trend', 'forecast'], required=True, help='Mode to run')
    
    # Input file
    parser.add_argument('--file', help='Input file path')
    
    # Output file
    parser.add_argument('--output', help='Output file path')
    
    # Excel mode
    # No additional arguments
    
    # Pivot mode
    parser.add_argument('--index', help='Column(s) to use as index')
    parser.add_argument('--columns', help='Column(s) to use as columns')
    parser.add_argument('--values', help='Column(s) to aggregate')
    parser.add_argument('--aggfunc', help='Aggregation function to use')
    
    # Dashboard mode
    parser.add_argument('--title', help='Dashboard title')
    parser.add_argument('--run', action='store_true', help='Run dashboard')
    
    # KPI mode
    # No additional arguments
    
    # Trend mode
    parser.add_argument('--date-col', help='Column name for date')
    parser.add_argument('--value-col', help='Column name for value')
    
    # Forecast mode
    parser.add_argument('--steps', type=int, help='Number of steps to forecast')
    parser.add_argument('--model-type', choices=['arima', 'sarima', 'linear'], help='Type of model to use')
    
    return parser.parse_args()

def main():
    """Main function"""
    args = parse_args()
    platform = DataAnalystPlatform()
    return platform.run(args)

if __name__ == '__main__':
    sys.exit(main())
