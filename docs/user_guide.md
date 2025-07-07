# IBM Data Analyst Capstone - User Guide

## Introduction

Welcome to the IBM Data Analyst Capstone project! This user guide will help you get started with the platform and explore its features.

## Installation

To install the platform, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/galafis/ibm-data-analyst-capstone.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ibm-data-analyst-capstone
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The platform provides several modes of operation:

### Excel Analysis

To analyze an Excel file:

```bash
python src/main_platform.py --mode excel --file path/to/excel_file.xlsx
```

This will analyze the Excel file and print the results.

### Pivot Table

To create a pivot table:

```bash
python src/main_platform.py --mode pivot --file path/to/data_file.csv --index category --values revenue --output path/to/output.xlsx
```

This will create a pivot table and export it to an Excel file.

### Dashboard

To create a dashboard:

```bash
python src/main_platform.py --mode dashboard --file path/to/data_file.csv --title "My Dashboard" --output path/to/dashboard.html
```

This will create a dashboard and export it to an HTML file.

To run the dashboard:

```bash
python src/main_platform.py --mode dashboard --file path/to/data_file.csv --run
```

This will create a dashboard and run it as a web application.

### KPI Calculation

To calculate KPIs:

```bash
python src/main_platform.py --mode kpi --file path/to/data_file.csv
```

This will calculate KPIs and print the results.

### Trend Analysis

To analyze trends:

```bash
python src/main_platform.py --mode trend --file path/to/data_file.csv --date-col date --value-col value
```

This will analyze trends and print the results.

### Forecasting

To forecast future values:

```bash
python src/main_platform.py --mode forecast --file path/to/data_file.csv --date-col date --value-col value --steps 10 --model-type arima
```

This will forecast future values and print the results.

## Examples

Here are some examples of how to use the platform:

### Example 1: Analyze Excel File

```bash
python src/main_platform.py --mode excel --file examples/sales_data.xlsx
```

### Example 2: Create Pivot Table

```bash
python src/main_platform.py --mode pivot --file examples/sales_data.csv --index region --columns product --values sales --aggfunc sum --output examples/sales_pivot.xlsx
```

### Example 3: Create Dashboard

```bash
python src/main_platform.py --mode dashboard --file examples/sales_data.csv --title "Sales Dashboard" --output examples/sales_dashboard.html
```

### Example 4: Calculate KPIs

```bash
python src/main_platform.py --mode kpi --file examples/sales_data.csv
```

### Example 5: Analyze Trends

```bash
python src/main_platform.py --mode trend --file examples/sales_data.csv --date-col date --value-col sales
```

### Example 6: Forecast Future Values

```bash
python src/main_platform.py --mode forecast --file examples/sales_data.csv --date-col date --value-col sales --steps 12 --model-type sarima
```

## Troubleshooting

If you encounter any issues, try the following:

1. Make sure you have installed all the required dependencies.
2. Check that the input file exists and is in the correct format.
3. Verify that the column names are correct.
4. Check the command-line arguments for typos.

If the issue persists, please open an issue on GitHub.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
