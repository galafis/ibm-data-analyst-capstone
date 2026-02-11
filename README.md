# IBM Data Analyst Professional Certificate Capstone

![Hero Image](hero_image.png)


---

## PT-BR: Projeto Capstone do IBM Data Analyst Professional Certificate

Plataforma completa de análise de dados empresariais com Business Intelligence, SQL Analytics, Excel avançado e visualizações profissionais.

## 🎯 Visão Geral

Sistema integrado de análise de dados que demonstra competências avançadas em Data Analysis, Business Intelligence, SQL, Excel e ferramentas de visualização para suporte à tomada de decisões empresariais.

### ✨ Características Principais

- **📊 Business Intelligence**: Dashboards executivos e KPIs
- **🗃️ SQL Analytics**: Consultas complexas e otimização
- **📈 Excel Avançado**: Pivot Tables, Power Query, VBA
- **📉 Visualizações**: Tableau, Power BI, Plotly
- **🤖 Automação**: Relatórios automatizados e ETL
- **📋 Qualidade de Dados**: Validação e limpeza

## 🛠️ Stack Tecnológico

### Análise de Dados
- **Python**: Pandas, NumPy, SciPy para análise
- **SQL**: PostgreSQL/SQL Server para consultas
- **Excel**: Power Query, Power Pivot, VBA
- **Streamlit**: Interface web interativa

### Business Intelligence
- **Tableau**: Visualizações profissionais
- **Power BI**: Dashboards corporativos
- **Plotly**: Gráficos interativos
- **Matplotlib/Seaborn**: Visualizações estatísticas

### Automação e ETL
- **Pandas**: Transformação de dados
- **SQLAlchemy**: ORM e conexões DB
- **Schedule**: Automação de tarefas
- **ReportLab**: Geração de relatórios PDF

## 📁 Estrutura do Projeto

```
ibm-data-analyst-capstone/
├── src/
│   ├── main_platform.py           # Aplicação principal
│   ├── data_analyst_platform.py   # Plataforma de análise
│   ├── sql/                       # Módulos SQL
│   │   ├── sql_analyzer.py        # Analisador SQL
│   │   ├── query_optimizer.py     # Otimizador
│   │   └── etl_processor.py       # ETL
│   ├── excel/                     # Módulos Excel
│   │   ├── excel_analyzer.py      # Analisador Excel
│   │   ├── pivot_generator.py     # Pivot Tables
│   │   └── vba_automation.py      # Automação VBA
│   ├── visualization/             # Visualizações
│   │   ├── plotly_charts.py       # Gráficos Plotly
│   │   ├── tableau_connector.py   # Conector Tableau
│   │   └── dashboard_builder.py   # Builder dashboards
│   └── business_intelligence/     # BI
│       ├── kpi_calculator.py      # Calculadora KPIs
│       ├── trend_analyzer.py      # Análise tendências
│       └── forecast_engine.py     # Engine previsão
├── sql/                           # Scripts SQL
├── tests/                         # Testes automatizados
├── docs/                          # Documentação
└── requirements.txt               # Dependências
```

## 🚀 Quick Start

### Pré-requisitos

- Python 3.11+
- Microsoft Excel 2019+
- PostgreSQL ou SQL Server
- Tableau Desktop (opcional)
- Power BI Desktop (opcional)

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/galafis/ibm-data-analyst-capstone.git
cd ibm-data-analyst-capstone
```

2. **Configure o ambiente:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

3. **Configure o banco de dados:**
```bash
python src/setup_database.py
```

4. **Execute a plataforma:**
```bash
streamlit run src/main_platform.py
```

## 📊 Funcionalidades Principais

### Business Intelligence Dashboard
```python
from src.business_intelligence.kpi_calculator import KPICalculator

# Calcular KPIs
kpi_calc = KPICalculator()
kpis = kpi_calc.calculate_all_kpis(data)

print(f"Revenue Growth: {kpis["revenue_growth"]:.2%}")
print(f"Customer Retention: {kpis["retention_rate"]:.2%}")
```

### SQL Analytics Engine
```python
from src.sql.sql_analyzer import SQLAnalyzer

# Análise SQL avançada
analyzer = SQLAnalyzer()
results = analyzer.execute_complex_query("""
    SELECT 
        customer_segment,
        AVG(order_value) as avg_order,
        COUNT(*) as total_orders,
        SUM(revenue) as total_revenue
    FROM sales_data 
    WHERE date >= '2024-01-01'
    GROUP BY customer_segment
    ORDER BY total_revenue DESC
""")
```

### Excel Advanced Analytics
```python
from src.excel.excel_analyzer import ExcelAnalyzer

# Análise Excel automatizada
excel_analyzer = ExcelAnalyzer()
excel_analyzer.load_workbook('data/sales_report.xlsx')

# Criar pivot table
pivot_data = excel_analyzer.create_pivot_table(
    data_range='A1:Z1000',
    rows=['Region', 'Product'],
    values=['Sales', 'Profit'],
    aggfunc='sum'
)
```

### Visualizações Interativas
```python
from src.visualization.plotly_charts import PlotlyCharts

# Gráficos interativos
charts = PlotlyCharts()

# Dashboard de vendas
sales_dashboard = charts.create_sales_dashboard(
    data=sales_data,
    metrics=['revenue', 'units_sold', 'profit_margin']
)

sales_dashboard.show()
```

## 📈 Casos de Uso Empresariais

### 1. Análise de Performance de Vendas
```python
# Análise completa de vendas
sales_analysis = analyzer.analyze_sales_performance(
    period='2024-Q1',
    segments=['Enterprise', 'SMB', 'Consumer'],
    metrics=['revenue', 'growth', 'retention']
)
```

### 2. Customer Analytics
```python
# Análise de comportamento do cliente
customer_insights = analyzer.analyze_customer_behavior(
    cohort_analysis=True,
    churn_prediction=True,
    lifetime_value=True
)
```

### 3. Financial Reporting
```python
# Relatórios financeiros automatizados
financial_report = analyzer.generate_financial_report(
    period='monthly',
    include_forecasts=True,
    export_format='pdf'
)
```

## 🔍 SQL Queries Avançadas

### Análise de Cohort
```sql
-- Análise de cohort de clientes
WITH customer_cohorts AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', first_purchase_date) as cohort_month,
        DATE_TRUNC('month', purchase_date) as purchase_month
    FROM customer_purchases
)
SELECT 
    cohort_month,
    COUNT(DISTINCT customer_id) as cohort_size,
    COUNT(DISTINCT CASE WHEN purchase_month = cohort_month + INTERVAL '1 month' 
          THEN customer_id END) as month_1_retention
FROM customer_cohorts
GROUP BY cohort_month
ORDER BY cohort_month;
```

### Performance de Produtos
```sql
-- Top produtos por margem de lucro
SELECT 
    p.product_name,
    SUM(s.quantity * s.unit_price) as total_revenue,
    SUM(s.quantity * p.cost) as total_cost,
    (SUM(s.quantity * s.unit_price) - SUM(s.quantity * p.cost)) / 
    SUM(s.quantity * s.unit_price) * 100 as profit_margin
FROM sales s
JOIN products p ON s.product_id = p.product_id
WHERE s.sale_date >= CURRENT_DATE - INTERVAL '90 days'
GROUP BY p.product_name
HAVING SUM(s.quantity * s.unit_price) > 10000
ORDER BY profit_margin DESC;
```

## 📊 Excel VBA Automation

### Automação de Relatórios
```vba
Sub GenerateMonthlyReport()
    Dim ws As Worksheet
    Dim lastRow As Long
    
    ' Criar nova planilha para relatório
    Set ws = Worksheets.Add
    ws.Name = "Monthly_Report_" & Format(Date, "yyyy_mm")
    
    ' Importar dados e criar pivot table
    Call ImportDataFromDatabase
    Call CreatePivotTable
    Call FormatReport
    
    ' Salvar e enviar por email
    Call SaveReport
    Call EmailReport
End Sub
```

## 🧪 Testes e Validação

### Executar Testes
```bash
# Testes unitários
pytest tests/unit/

# Testes de integração SQL
pytest tests/test_sql_queries.py

# Testes de Excel
pytest tests/test_excel_functions.py

# Testes de visualização
pytest tests/test_visualizations.py
```

### Validação de Dados
```python
# Validação de qualidade dos dados
from src.utils.data_quality import DataQualityChecker

checker = DataQualityChecker()
quality_report = checker.validate_dataset(
    data=sales_data,
    rules=['no_nulls', 'valid_dates', 'positive_amounts']
)
```

## 📈 KPIs e Métricas

### Métricas de Negócio
- **Revenue Growth**: Crescimento de receita MoM/YoY
- **Customer Acquisition Cost (CAC)**: Custo de aquisição
- **Customer Lifetime Value (CLV)**: Valor do cliente
- **Churn Rate**: Taxa de cancelamento
- **Net Promoter Score (NPS)**: Satisfação do cliente

### Métricas Operacionais
- **Data Quality Score**: Qualidade dos dados
- **Report Generation Time**: Tempo de geração
- **Dashboard Load Time**: Performance dos dashboards
- **Query Execution Time**: Performance SQL

## 🔧 Configuração Avançada

### Conexão com Banco de Dados
```python
# config/database.py
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'analytics_db',
    'user': 'analyst',
    'password': 'secure_password'
}
```

### Configuração de Relatórios
```python
# config/reports.py
REPORT_CONFIG = {
    'schedule': 'daily',
    'recipients': ['manager@company.com'],
    'format': 'pdf',
    'include_charts': True
}
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Gabriel Demetrios Lafis**

- **Certificação**: IBM Data Analyst Professional Certificate
- GitHub: [@galafis](https://github.com/galafis)
- Email: gabrieldemetrios@gmail.com

---

⭐ Se este projeto foi útil, considere deixar uma estrela!

---

## EN-US: IBM Data Analyst Professional Certificate Capstone Project

A comprehensive enterprise data analysis platform with Business Intelligence, SQL Analytics, advanced Excel, and professional visualizations.

## 🎯 Overview

An integrated data analysis system demonstrating advanced competencies in Data Analysis, Business Intelligence, SQL, Excel, and visualization tools to support business decision-making.

### ✨ Key Features

- **📊 Business Intelligence**: Executive dashboards and KPIs
- **🗃️ SQL Analytics**: Complex queries and optimization
- **📈 Advanced Excel**: Pivot Tables, Power Query, VBA
- **📉 Visualizations**: Tableau, Power BI, Plotly
- **🤖 Automation**: Automated reports and ETL
- **📋 Data Quality**: Validation and cleaning

## 🛠️ Technology Stack

### Data Analysis
- **Python**: Pandas, NumPy, SciPy for analysis
- **SQL**: PostgreSQL/SQL Server for queries
- **Excel**: Power Query, Power Pivot, VBA
- **Streamlit**: Interactive web interface

### Business Intelligence
- **Tableau**: Professional visualizations
- **Power BI**: Corporate dashboards
- **Plotly**: Interactive charts
- **Matplotlib/Seaborn**: Statistical visualizations

### Automation and ETL
- **Pandas**: Data transformation
- **SQLAlchemy**: ORM and DB connections
- **Schedule**: Task automation
- **ReportLab**: PDF report generation

## 📁 Project Structure

```
ibm-data-analyst-capstone/
├── src/
│   ├── main_platform.py           # Main application
│   ├── data_analyst_platform.py   # Analysis platform
│   ├── sql/                       # SQL modules
│   │   ├── sql_analyzer.py        # SQL Analyzer
│   │   ├── query_optimizer.py     # Optimizer
│   │   └── etl_processor.py       # ETL
│   ├── excel/                     # Excel modules
│   │   ├── excel_analyzer.py      # Excel Analyzer
│   │   ├── pivot_generator.py     # Pivot Tables
│   │   └── vba_automation.py      # VBA Automation
│   ├── visualization/             # Visualizations
│   │   ├── plotly_charts.py       # Plotly Charts
│   │   ├── tableau_connector.py   # Tableau Connector
│   │   └── dashboard_builder.py   # Dashboard Builder
│   └── business_intelligence/     # BI
│       ├── kpi_calculator.py      # KPI Calculator
│       ├── trend_analyzer.py      # Trend Analysis
│       └── forecast_engine.py     # Forecast Engine
├── sql/                           # SQL scripts
├── tests/                         # Automated tests
├── docs/                          # Documentation
└── requirements.txt               # Dependencies
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Microsoft Excel 2019+
- PostgreSQL or SQL Server
- Tableau Desktop (optional)
- Power BI Desktop (optional)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/galafis/ibm-data-analyst-capstone.git
cd ibm-data-analyst-capstone
```

2. **Configure the environment:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

3. **Configure the database:**
```bash
python src/setup_database.py
```

4. **Run the platform:**
```bash
streamlit run src/main_platform.py
```

## 📊 Core Functionalities

### Business Intelligence Dashboard
```python
from src.business_intelligence.kpi_calculator import KPICalculator

# Calculate KPIs
kpi_calc = KPICalculator()
kpis = kpi_calc.calculate_all_kpis(data)

print(f"Revenue Growth: {kpis["revenue_growth"]:.2%}")
print(f"Customer Retention: {kpis["retention_rate"]:.2%}")
```

### SQL Analytics Engine
```python
from src.sql.sql_analyzer import SQLAnalyzer

# Advanced SQL analysis
analyzer = SQLAnalyzer()
results = analyzer.execute_complex_query("""
    SELECT 
        customer_segment,
        AVG(order_value) as avg_order,
        COUNT(*) as total_orders,
        SUM(revenue) as total_revenue
    FROM sales_data 
    WHERE date >= '2024-01-01'
    GROUP BY customer_segment
    ORDER BY total_revenue DESC
""")
```

### Excel Advanced Analytics
```python
from src.excel.excel_analyzer import ExcelAnalyzer

# Automated Excel analysis
excel_analyzer = ExcelAnalyzer()
excel_analyzer.load_workbook('data/sales_report.xlsx')

# Create pivot table
pivot_data = excel_analyzer.create_pivot_table(
    data_range='A1:Z1000',
    rows=['Region', 'Product'],
    values=['Sales', 'Profit'],
    aggfunc='sum'
)
```

### Interactive Visualizations
```python
from src.visualization.plotly_charts import PlotlyCharts

# Interactive charts
charts = PlotlyCharts()

# Sales dashboard
sales_dashboard = charts.create_sales_dashboard(
    data=sales_data,
    metrics=['revenue', 'units_sold', 'profit_margin']
)

sales_dashboard.show()
```

## 📈 Business Use Cases

### 1. Sales Performance Analysis
```python
# Comprehensive sales analysis
sales_analysis = analyzer.analyze_sales_performance(
    period='2024-Q1',
    segments=['Enterprise', 'SMB', 'Consumer'],
    metrics=['revenue', 'growth', 'retention']
)
```

### 2. Customer Analytics
```python
# Customer behavior analysis
customer_insights = analyzer.analyze_customer_behavior(
    cohort_analysis=True,
    churn_prediction=True,
    lifetime_value=True
)
```

### 3. Financial Reporting
```python
# Automated financial reports
financial_report = analyzer.generate_financial_report(
    period='monthly',
    include_forecasts=True,
    export_format='pdf'
)
```

## 🔍 Advanced SQL Queries

### Cohort Analysis
```sql
-- Customer cohort analysis
WITH customer_cohorts AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', first_purchase_date) as cohort_month,
        DATE_TRUNC('month', purchase_date) as purchase_month
    FROM customer_purchases
)
SELECT 
    cohort_month,
    COUNT(DISTINCT customer_id) as cohort_size,
    COUNT(DISTINCT CASE WHEN purchase_month = cohort_month + INTERVAL '1 month' 
          THEN customer_id END) as month_1_retention
FROM customer_cohorts
GROUP BY cohort_month
ORDER BY cohort_month;
```

### Product Performance
```sql
-- Top products by profit margin
SELECT 
    p.product_name,
    SUM(s.quantity * s.unit_price) as total_revenue,
    SUM(s.quantity * p.cost) as total_cost,
    (SUM(s.quantity * s.unit_price) - SUM(s.quantity * p.cost)) / 
    SUM(s.quantity * s.unit_price) * 100 as profit_margin
FROM sales s
JOIN products p ON s.product_id = p.product_id
WHERE s.sale_date >= CURRENT_DATE - INTERVAL '90 days'
GROUP BY p.product_name
HAVING SUM(s.quantity * s.unit_price) > 10000
ORDER BY profit_margin DESC;
```

## 📊 Excel VBA Automation

### Report Automation
```vba
Sub GenerateMonthlyReport()
    Dim ws As Worksheet
    Dim lastRow As Long
    
    ' Create new worksheet for report
    Set ws = Worksheets.Add
    ws.Name = "Monthly_Report_" & Format(Date, "yyyy_mm")
    
    ' Import data and create pivot table
    Call ImportDataFromDatabase
    Call CreatePivotTable
    Call FormatReport
    
    ' Save and email report
    Call SaveReport
    Call EmailReport
End Sub
```

## 🧪 Testing and Validation

### Run Tests
```bash
# Unit tests
pytest tests/unit/

# SQL integration tests
pytest tests/test_sql_queries.py

# Excel tests
pytest tests/test_excel_functions.py

# Visualization tests
pytest tests/test_visualizations.py
```

### Data Validation
```python
# Data quality validation
from src.utils.data_quality import DataQualityChecker

checker = DataQualityChecker()
quality_report = checker.validate_dataset(
    data=sales_data,
    rules=['no_nulls', 'valid_dates', 'positive_amounts']
)
```

## 📈 KPIs and Metrics

### Business Metrics
- **Revenue Growth**: MoM/YoY revenue growth
- **Customer Acquisition Cost (CAC)**: Acquisition cost
- **Customer Lifetime Value (CLV)**: Customer value
- **Churn Rate**: Churn rate
- **Net Promoter Score (NPS)**: Customer satisfaction

### Operational Metrics
- **Data Quality Score**: Data quality
- **Report Generation Time**: Generation time
- **Dashboard Load Time**: Dashboard performance
- **Query Execution Time**: SQL performance

## 🔧 Advanced Configuration

### Database Connection
```python
# config/database.py
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'analytics_db',
    'user': 'analyst',
    'password': 'secure_password'
}
```

### Report Configuration
```python
# config/reports.py
REPORT_CONFIG = {
    'schedule': 'daily',
    'recipients': ['manager@company.com'],
    'format': 'pdf',
    'include_charts': True
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Gabriel Demetrios Lafis**

- **Certification**: IBM Data Analyst Professional Certificate
- GitHub: [@galafis](https://github.com/galafis)
- Email: gabrieldemetrios@gmail.com

---

⭐ If this project was helpful, consider leaving a star!

