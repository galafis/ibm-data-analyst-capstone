# IBM Data Analyst Capstone - API Reference

## DataAnalystPlatform

The main class that provides access to all platform features.

### Methods

#### `__init__()`

Initialize the platform.

#### `initialize_modules()`

Initialize all modules.

#### `analyze_excel(file_path)`

Analyze an Excel file.

Parameters:
- `file_path` (str): Path to the Excel file.

Returns:
- `dict`: Analysis results.

#### `create_pivot(data, index, columns, values, aggfunc='sum')`

Create a pivot table.

Parameters:
- `data` (pd.DataFrame or str): Data to pivot.
- `index` (str or list): Column(s) to use as index.
- `columns` (str or list): Column(s) to use as columns.
- `values` (str or list): Column(s) to aggregate.
- `aggfunc` (str or function): Aggregation function to use.

Returns:
- `pd.DataFrame`: Pivot table.

#### `create_dashboard(data, charts_config, title="IBM Data Analyst Dashboard")`

Create a dashboard.

Parameters:
- `data` (pd.DataFrame): Data to visualize.
- `charts_config` (list): List of chart configurations.
- `title` (str): Dashboard title.

Returns:
- `DashboardBuilder`: Dashboard builder object.

#### `calculate_kpis(data, kpi_config)`

Calculate KPIs.

Parameters:
- `data` (pd.DataFrame): Data to analyze.
- `kpi_config` (dict): KPI configuration.

Returns:
- `dict`: KPI results.

#### `analyze_trends(data, date_col, value_col, config=None)`

Analyze trends.

Parameters:
- `data` (pd.DataFrame): Data to analyze.
- `date_col` (str): Column name for date.
- `value_col` (str): Column name for value.
- `config` (dict): Analysis configuration.

Returns:
- `dict`: Trend analysis results.

#### `forecast(data, date_col, value_col, steps=10, model_type='arima', model_params=None)`

Forecast future values.

Parameters:
- `data` (pd.DataFrame): Data to forecast.
- `date_col` (str): Column name for date.
- `value_col` (str): Column name for value.
- `steps` (int): Number of steps to forecast.
- `model_type` (str): Type of model to use ('arima', 'sarima', 'linear').
- `model_params` (dict): Model parameters.

Returns:
- `pd.Series`: Forecasted values.

## ExcelAnalyzer

Class for analyzing Excel files.

### Methods

#### `__init__(file_path)`

Initialize the analyzer.

Parameters:
- `file_path` (str): Path to the Excel file.

#### `load_workbook()`

Load the workbook.

Returns:
- `openpyxl.Workbook`: Loaded workbook.

#### `read_sheet(sheet_name)`

Read a sheet.

Parameters:
- `sheet_name` (str): Name of the sheet.

Returns:
- `pd.DataFrame`: Sheet data.

#### `analyze_sheet(sheet_name)`

Analyze a sheet.

Parameters:
- `sheet_name` (str): Name of the sheet.

Returns:
- `dict`: Analysis results.

#### `get_sheet_names()`

Get sheet names.

Returns:
- `list`: List of sheet names.

#### `get_named_ranges()`

Get named ranges.

Returns:
- `list`: List of named ranges.

#### `get_pivot_tables(sheet_name)`

Get pivot tables.

Parameters:
- `sheet_name` (str): Name of the sheet.

Returns:
- `list`: List of pivot tables.

#### `get_formulas(sheet_name)`

Get formulas.

Parameters:
- `sheet_name` (str): Name of the sheet.

Returns:
- `dict`: Dictionary of formulas.

#### `get_charts(sheet_name)`

Get charts.

Parameters:
- `sheet_name` (str): Name of the sheet.

Returns:
- `int`: Number of charts.

## PivotGenerator

Class for generating pivot tables.

### Methods

#### `__init__(data)`

Initialize the generator.

Parameters:
- `data` (pd.DataFrame or str): Data to pivot.

#### `create_pivot(index, columns, values, aggfunc='sum')`

Create a pivot table.

Parameters:
- `index` (str or list): Column(s) to use as index.
- `columns` (str or list): Column(s) to use as columns.
- `values` (str or list): Column(s) to aggregate.
- `aggfunc` (str or function): Aggregation function to use.

Returns:
- `pd.DataFrame`: Pivot table.

#### `export_to_excel(pivot_table, output_path, sheet_name='Pivot')`

Export pivot table to Excel.

Parameters:
- `pivot_table` (pd.DataFrame): Pivot table to export.
- `output_path` (str): Path to save the Excel file.
- `sheet_name` (str): Name of the sheet.

Returns:
- `bool`: True if successful.

## PlotlyCharts

Class for creating Plotly charts.

### Methods

#### `__init__(theme='plotly')`

Initialize the charts.

Parameters:
- `theme` (str): Plotly theme.

#### `create_bar_chart(data, x, y, title=None, color=None, orientation='v')`

Create a bar chart.

Parameters:
- `data` (pd.DataFrame): Data to plot.
- `x` (str): Column name for x-axis.
- `y` (str): Column name for y-axis.
- `title` (str): Chart title.
- `color` (str): Column name for color.
- `orientation` (str): 'v' for vertical, 'h' for horizontal.

Returns:
- `plotly.graph_objects.Figure`: Plotly figure.

#### `create_line_chart(data, x, y, title=None, color=None, line_shape='linear')`

Create a line chart.

Parameters:
- `data` (pd.DataFrame): Data to plot.
- `x` (str): Column name for x-axis.
- `y` (str): Column name for y-axis.
- `title` (str): Chart title.
- `color` (str): Column name for color.
- `line_shape` (str): Shape of the line ('linear', 'spline', etc.).

Returns:
- `plotly.graph_objects.Figure`: Plotly figure.

#### `create_scatter_plot(data, x, y, title=None, color=None, size=None, hover_name=None)`

Create a scatter plot.

Parameters:
- `data` (pd.DataFrame): Data to plot.
- `x` (str): Column name for x-axis.
- `y` (str): Column name for y-axis.
- `title` (str): Chart title.
- `color` (str): Column name for color.
- `size` (str): Column name for point size.
- `hover_name` (str): Column name for hover text.

Returns:
- `plotly.graph_objects.Figure`: Plotly figure.

#### `create_pie_chart(data, values, names, title=None, hole=0)`

Create a pie chart.

Parameters:
- `data` (pd.DataFrame): Data to plot.
- `values` (str): Column name for values.
- `names` (str): Column name for names.
- `title` (str): Chart title.
- `hole` (float): Size of the hole (0-1, 0 for pie, >0 for donut).

Returns:
- `plotly.graph_objects.Figure`: Plotly figure.

#### `create_histogram(data, x, nbins=None, title=None, color=None)`

Create a histogram.

Parameters:
- `data` (pd.DataFrame): Data to plot.
- `x` (str): Column name for values.
- `nbins` (int): Number of bins.
- `title` (str): Chart title.
- `color` (str): Column name for color.

Returns:
- `plotly.graph_objects.Figure`: Plotly figure.

#### `create_box_plot(data, x, y, title=None, color=None)`

Create a box plot.

Parameters:
- `data` (pd.DataFrame): Data to plot.
- `x` (str): Column name for x-axis.
- `y` (str): Column name for y-axis.
- `title` (str): Chart title.
- `color` (str): Column name for color.

Returns:
- `plotly.graph_objects.Figure`: Plotly figure.

#### `create_heatmap(data, title=None, colorscale='Viridis')`

Create a heatmap.

Parameters:
- `data` (pd.DataFrame): Data to plot (should be a correlation matrix or similar).
- `title` (str): Chart title.
- `colorscale` (str): Colorscale name.

Returns:
- `plotly.graph_objects.Figure`: Plotly figure.

#### `save_figure(fig, output_path, format='html')`

Save a figure to a file.

Parameters:
- `fig` (plotly.graph_objects.Figure): Plotly figure to save.
- `output_path` (str): Path to save the figure.
- `format` (str): Format to save ('html', 'png', 'jpg', 'svg', 'pdf').

Returns:
- `bool`: True if successful.

## DashboardBuilder

Class for building dashboards.

### Methods

#### `__init__(title="Data Analysis Dashboard")`

Initialize the dashboard.

Parameters:
- `title` (str): Dashboard title.

#### `add_chart(fig, title=None, width=6, height=400)`

Add a chart to the dashboard.

Parameters:
- `fig` (plotly.graph_objects.Figure): Plotly figure to add.
- `title` (str): Chart title.
- `width` (int): Width in grid units (12 is full width).
- `height` (int): Height in pixels.

Returns:
- `int`: Index of the added chart.

#### `set_layout(layout)`

Set the layout of the dashboard.

Parameters:
- `layout` (list): List of lists, each inner list represents a row. Each item in the inner list is an index of a chart.

Returns:
- `bool`: True if successful.

#### `create_dash_app(server=None)`

Create a Dash app.

Parameters:
- `server` (flask.Flask): Flask server to use.

Returns:
- `dash.Dash`: Dash app.

#### `create_html_dashboard(output_path)`

Create an HTML dashboard.

Parameters:
- `output_path` (str): Path to save the HTML file.

Returns:
- `bool`: True if successful.

#### `run_dash_app(host='0.0.0.0', port=8050, debug=False)`

Run the Dash app.

Parameters:
- `host` (str): Host to run on.
- `port` (int): Port to run on.
- `debug` (bool): Whether to run in debug mode.

## KPICalculator

Class for calculating KPIs.

### Methods

#### `__init__(data=None)`

Initialize the calculator.

Parameters:
- `data` (pd.DataFrame): Data to analyze.

#### `load_data(data)`

Load data for KPI calculation.

Parameters:
- `data` (pd.DataFrame or str): Data to load (DataFrame or path to file).

Returns:
- `bool`: True if successful.

#### `calculate_revenue_growth(period_col, revenue_col, periods=None)`

Calculate revenue growth.

Parameters:
- `period_col` (str): Column name for period (date or period name).
- `revenue_col` (str): Column name for revenue.
- `periods` (list): List of periods to include (if None, use all periods).

Returns:
- `pd.DataFrame`: DataFrame with revenue growth by period.

#### `calculate_customer_acquisition_cost(period_col, marketing_expense_col, new_customers_col, periods=None)`

Calculate customer acquisition cost.

Parameters:
- `period_col` (str): Column name for period (date or period name).
- `marketing_expense_col` (str): Column name for marketing expense.
- `new_customers_col` (str): Column name for new customers.
- `periods` (list): List of periods to include (if None, use all periods).

Returns:
- `pd.DataFrame`: DataFrame with customer acquisition cost by period.

#### `calculate_customer_lifetime_value(customer_id_col, revenue_col, date_col=None, time_period=365)`

Calculate customer lifetime value.

Parameters:
- `customer_id_col` (str): Column name for customer ID.
- `revenue_col` (str): Column name for revenue.
- `date_col` (str): Column name for date (if None, assume all data is for the same period).
- `time_period` (int): Time period in days (default: 365 days = 1 year).

Returns:
- `pd.DataFrame`: DataFrame with customer lifetime value by customer.

#### `calculate_conversion_rate(period_col, visitors_col, conversions_col, periods=None)`

Calculate conversion rate.

Parameters:
- `period_col` (str): Column name for period (date or period name).
- `visitors_col` (str): Column name for visitors.
- `conversions_col` (str): Column name for conversions.
- `periods` (list): List of periods to include (if None, use all periods).

Returns:
- `pd.DataFrame`: DataFrame with conversion rate by period.

#### `calculate_churn_rate(period_col, customers_start_col, customers_end_col, new_customers_col, periods=None)`

Calculate churn rate.

Parameters:
- `period_col` (str): Column name for period (date or period name).
- `customers_start_col` (str): Column name for customers at start of period.
- `customers_end_col` (str): Column name for customers at end of period.
- `new_customers_col` (str): Column name for new customers in period.
- `periods` (list): List of periods to include (if None, use all periods).

Returns:
- `pd.DataFrame`: DataFrame with churn rate by period.

## TrendAnalyzer

Class for analyzing trends.

### Methods

#### `__init__(data=None)`

Initialize the analyzer.

Parameters:
- `data` (pd.DataFrame): Data to analyze.

#### `load_data(data, date_col=None, value_col=None)`

Load data for trend analysis.

Parameters:
- `data` (pd.DataFrame or str): Data to load (DataFrame or path to file).
- `date_col` (str): Column name for date.
- `value_col` (str): Column name for value.

Returns:
- `bool`: True if successful.

#### `decompose_time_series(column=None, model='additive', period=None)`

Decompose time series into trend, seasonal, and residual components.

Parameters:
- `column` (str): Column name to decompose (if None, use the first column).
- `model` (str): Decomposition model ('additive' or 'multiplicative').
- `period` (int): Period for seasonal decomposition (if None, infer from data).

Returns:
- `statsmodels.tsa.seasonal.DecomposeResult`: Decomposition result.

#### `test_stationarity(column=None)`

Test stationarity of time series.

Parameters:
- `column` (str): Column name to test (if None, use the first column).

Returns:
- `dict`: Dictionary with test results.

#### `calculate_moving_average(column=None, window=7)`

Calculate moving average.

Parameters:
- `column` (str): Column name to calculate (if None, use the first column).
- `window` (int): Window size for moving average.

Returns:
- `pd.Series`: Moving average series.

#### `calculate_exponential_smoothing(column=None, alpha=0.3)`

Calculate exponential smoothing.

Parameters:
- `column` (str): Column name to calculate (if None, use the first column).
- `alpha` (float): Smoothing factor (0 < alpha < 1).

Returns:
- `pd.Series`: Exponential smoothing series.

#### `detect_outliers(column=None, method='zscore', threshold=3)`

Detect outliers in time series.

Parameters:
- `column` (str): Column name to detect outliers (if None, use the first column).
- `method` (str): Method to detect outliers ('zscore' or 'iqr').
- `threshold` (float): Threshold for outlier detection.

Returns:
- `pd.Series`: Boolean series indicating outliers.

## ForecastEngine

Class for forecasting future values.

### Methods

#### `__init__(data=None)`

Initialize the engine.

Parameters:
- `data` (pd.DataFrame): Data to forecast.

#### `load_data(data, date_col=None, value_col=None)`

Load data for forecasting.

Parameters:
- `data` (pd.DataFrame or str): Data to load (DataFrame or path to file).
- `date_col` (str): Column name for date.
- `value_col` (str): Column name for value.

Returns:
- `bool`: True if successful.

#### `train_arima_model(column=None, order=(1, 1, 1))`

Train ARIMA model.

Parameters:
- `column` (str): Column name to forecast (if None, use the first column).
- `order` (tuple): ARIMA order (p, d, q).

Returns:
- `statsmodels.tsa.arima.model.ARIMAResults`: Trained model.

#### `train_sarima_model(column=None, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))`

Train SARIMA model.

Parameters:
- `column` (str): Column name to forecast (if None, use the first column).
- `order` (tuple): ARIMA order (p, d, q).
- `seasonal_order` (tuple): Seasonal order (P, D, Q, s).

Returns:
- `statsmodels.tsa.statespace.sarimax.SARIMAXResults`: Trained model.

#### `train_linear_regression(column=None, features=None)`

Train linear regression model.

Parameters:
- `column` (str): Column name to forecast (if None, use the first column).
- `features` (list): List of feature column names (if None, use all columns except target).

Returns:
- `sklearn.linear_model.LinearRegression`: Trained model.

#### `forecast_future(steps=10, column=None)`

Forecast future values.

Parameters:
- `steps` (int): Number of steps to forecast.
- `column` (str): Column name to forecast (if None, use the first column).

Returns:
- `pd.Series`: Forecasted values.

#### `evaluate_forecast(test_data, column=None)`

Evaluate forecast.

Parameters:
- `test_data` (pd.DataFrame): Test data.
- `column` (str): Column name to evaluate (if None, use the first column).

Returns:
- `dict`: Dictionary with evaluation metrics.

#### `plot_forecast(test_data=None, column=None)`

Plot forecast.

Parameters:
- `test_data` (pd.DataFrame): Test data (if None, only plot forecast).
- `column` (str): Column name to plot (if None, use the first column).

Returns:
- `matplotlib.figure.Figure`: Plot figure.
