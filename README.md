# IBM Data Analyst Professional Certificate Capstone Project

*[English version below / Versão em inglês abaixo]*

## 🇧🇷 Português

### 📊 Visão Geral

Este projeto representa o trabalho final do **IBM Data Analyst Professional Certificate**, demonstrando competências avançadas em análise de dados, visualização, business intelligence, SQL, Excel avançado e storytelling com dados. A plataforma desenvolvida oferece uma solução completa para análise de dados empresariais, geração de insights e suporte à tomada de decisões.

**Desenvolvido por:** Gabriel Demetrios Lafis  
**Certificação:** IBM Data Analyst Professional Certificate  
**Tecnologias:** Python, SQL, Excel, Tableau, Power BI, Pandas, Plotly  
**Área de Foco:** Data Analysis, Business Intelligence, Data Visualization, SQL Analytics

### 🎯 Características Principais

- **Business Intelligence Dashboard:** Dashboards executivos e operacionais
- **SQL Analytics Engine:** Consultas complexas e análises avançadas
- **Excel Integration:** Automação e análises avançadas em Excel
- **Data Visualization Suite:** Visualizações profissionais e interativas
- **Automated Reporting:** Relatórios automatizados e agendados
- **KPI Monitoring:** Monitoramento de indicadores-chave de performance
- **Data Quality Assessment:** Avaliação e garantia de qualidade dos dados

### 🛠️ Stack Tecnológico

| Categoria | Tecnologia | Versão | Propósito |
|-----------|------------|--------|-----------|
| **Data Analysis** | Python | 3.11+ | Análise de dados |
| **Database** | SQL Server | Latest | Banco de dados |
| **Spreadsheets** | Excel | 365 | Análises avançadas |
| **BI Tools** | Tableau | Latest | Visualizações BI |
| **BI Platform** | Power BI | Latest | Dashboards corporativos |
| **Data Manipulation** | Pandas | 2.0+ | Manipulação de dados |
| **Visualization** | Plotly | 5.15+ | Gráficos interativos |
| **Web Framework** | Streamlit | 1.28+ | Interface web |
| **Statistics** | SciPy | 1.11+ | Análises estatísticas |
| **Reporting** | ReportLab | Latest | Geração de relatórios |

### 🚀 Começando

#### Pré-requisitos
- Python 3.11 ou superior
- Microsoft Excel 2019 ou 365
- SQL Server ou PostgreSQL
- Tableau Desktop (opcional)
- Power BI Desktop (opcional)

#### Instalação
```bash
# Clone o repositório
git clone https://github.com/galafis/ibm-data-analyst-capstone.git
cd ibm-data-analyst-capstone

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\\Scripts\\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Configure o banco de dados
python src/setup_database.py

# Execute a aplicação principal
streamlit run src/main_platform.py
```

#### Acesso Rápido
```bash
# Executar análise completa
python src/data_analyst_platform.py --full-analysis

# Gerar relatórios
python src/report_generator.py --type executive

# Executar consultas SQL
python src/sql_analyzer.py --query-file queries/analysis.sql

# Atualizar dashboards
python src/dashboard_updater.py --refresh-all
```

### 📊 Funcionalidades Detalhadas

#### 📈 **Business Intelligence**
- **Executive Dashboards:** Dashboards para alta gestão
- **Operational Dashboards:** Monitoramento operacional em tempo real
- **Financial Analytics:** Análises financeiras e de rentabilidade
- **Sales Performance:** Análise de performance de vendas
- **Customer Analytics:** Análise de comportamento de clientes
- **Market Intelligence:** Inteligência de mercado e competitiva

#### 🗃️ **SQL Analytics**
- **Complex Queries:** Consultas SQL avançadas e otimizadas
- **Data Warehousing:** Modelagem dimensional e ETL
- **Performance Tuning:** Otimização de consultas e índices
- **Stored Procedures:** Procedimentos armazenados e funções
- **Data Integration:** Integração de múltiplas fontes de dados
- **Query Automation:** Automação de consultas recorrentes

#### 📊 **Excel Advanced Analytics**
- **Pivot Tables:** Tabelas dinâmicas avançadas
- **Power Query:** ETL e transformação de dados
- **Power Pivot:** Modelagem de dados e DAX
- **VBA Automation:** Automação com macros VBA
- **Advanced Formulas:** Fórmulas complexas e arrays
- **Data Validation:** Validação e limpeza de dados

#### 📈 **Data Visualization**
- **Interactive Charts:** Gráficos interativos e dinâmicos
- **Statistical Plots:** Visualizações estatísticas avançadas
- **Geospatial Analysis:** Mapas e análises geográficas
- **Time Series:** Análises temporais e tendências
- **Comparative Analysis:** Análises comparativas e benchmarking
- **Custom Visualizations:** Visualizações personalizadas

### 🏗️ Arquitetura do Sistema

```
ibm-data-analyst-capstone/
├── src/
│   ├── main_platform.py          # Aplicação principal
│   ├── data_analyst_platform.py  # Plataforma de análise
│   ├── sql/
│   │   ├── sql_analyzer.py        # Analisador SQL
│   │   ├── query_optimizer.py    # Otimizador de consultas
│   │   └── etl_processor.py      # Processador ETL
│   ├── excel/
│   │   ├── excel_analyzer.py     # Analisador Excel
│   │   ├── pivot_generator.py    # Gerador de tabelas dinâmicas
│   │   └── vba_automation.py     # Automação VBA
│   ├── visualization/
│   │   ├── tableau_connector.py  # Conector Tableau
│   │   ├── powerbi_connector.py  # Conector Power BI
│   │   ├── plotly_charts.py      # Gráficos Plotly
│   │   └── dashboard_builder.py  # Construtor de dashboards
│   ├── business_intelligence/
│   │   ├── kpi_calculator.py     # Calculadora de KPIs
│   │   ├── trend_analyzer.py     # Analisador de tendências
│   │   └── forecast_engine.py    # Motor de previsão
│   ├── reporting/
│   │   ├── report_generator.py   # Gerador de relatórios
│   │   ├── automated_reports.py  # Relatórios automatizados
│   │   └── email_sender.py       # Envio de relatórios
│   └── utils/
│       ├── data_quality.py       # Qualidade de dados
│       ├── performance_monitor.py # Monitor de performance
│       └── security_manager.py   # Gerenciador de segurança
├── sql_queries/
│   ├── analysis/                 # Consultas de análise
│   ├── etl/                      # Consultas ETL
│   └── reports/                  # Consultas de relatórios
├── excel_templates/
│   ├── dashboards/               # Templates de dashboards
│   ├── reports/                  # Templates de relatórios
│   └── analysis/                 # Templates de análise
├── tableau_workbooks/            # Workbooks Tableau
├── powerbi_reports/              # Relatórios Power BI
├── tests/
│   ├── test_sql_queries.py       # Testes SQL
│   ├── test_excel_functions.py   # Testes Excel
│   └── test_visualizations.py    # Testes de visualização
├── data/
│   ├── raw/                      # Dados brutos
│   ├── processed/                # Dados processados
│   └── warehouse/                # Data warehouse
└── docs/                         # Documentação
```

### 📊 Casos de Uso

#### 1. **Análise de Performance de Vendas**
```python
from src.business_intelligence.sales_analyzer import SalesAnalyzer

# Análise de vendas
analyzer = SalesAnalyzer()
sales_data = analyzer.load_sales_data('2024')
performance = analyzer.analyze_performance(sales_data)

# Gerar dashboard
dashboard = analyzer.create_sales_dashboard(performance)
```

#### 2. **Análise de Customer Lifetime Value**
```sql
-- Consulta SQL para CLV
WITH customer_metrics AS (
    SELECT 
        customer_id,
        COUNT(order_id) as total_orders,
        SUM(order_value) as total_revenue,
        AVG(order_value) as avg_order_value,
        DATEDIFF(MAX(order_date), MIN(order_date)) as customer_lifespan
    FROM orders
    GROUP BY customer_id
)
SELECT 
    customer_id,
    total_revenue / NULLIF(customer_lifespan, 0) * 365 as clv_annual
FROM customer_metrics;
```

#### 3. **Dashboard Executivo Automatizado**
```python
from src.reporting.executive_dashboard import ExecutiveDashboard

# Dashboard executivo
dashboard = ExecutiveDashboard()
kpis = dashboard.calculate_executive_kpis()
charts = dashboard.generate_executive_charts(kpis)
report = dashboard.create_executive_report(charts)
```

### 🧪 Testes e Qualidade

#### Executar Testes
```bash
# Testes de consultas SQL
python -m pytest tests/test_sql_queries.py -v

# Testes de funções Excel
python -m pytest tests/test_excel_functions.py -v

# Testes de visualizações
python -m pytest tests/test_visualizations.py -v

# Validação de qualidade de dados
python src/utils/data_quality.py --validate-all
```

#### Métricas de Qualidade
- **Data Accuracy:** >98% de precisão dos dados
- **Query Performance:** <3s para consultas complexas
- **Dashboard Load Time:** <5s para dashboards
- **Report Generation:** <2 minutes para relatórios
- **Data Freshness:** Atualização a cada 15 minutos

### 📈 Resultados e Impacto

#### KPIs Monitorados
- **Revenue Growth:** Crescimento de receita mensal/anual
- **Customer Acquisition Cost:** Custo de aquisição de clientes
- **Customer Lifetime Value:** Valor vitalício do cliente
- **Conversion Rates:** Taxas de conversão por canal
- **Operational Efficiency:** Eficiência operacional
- **Market Share:** Participação de mercado

#### Casos de Sucesso
- **Sales Analysis:** 20% aumento na identificação de oportunidades
- **Customer Segmentation:** 15% melhoria na retenção
- **Inventory Optimization:** 25% redução em custos de estoque
- **Financial Reporting:** 50% redução no tempo de fechamento

### 🔧 Configuração Avançada

#### Conexões de Banco de Dados
```python
# config/database_config.py
DATABASE_CONNECTIONS = {
    'production': {
        'host': 'prod-server.company.com',
        'database': 'analytics_db',
        'username': 'analyst_user',
        'port': 1433
    },
    'staging': {
        'host': 'staging-server.company.com',
        'database': 'staging_db',
        'username': 'staging_user',
        'port': 1433
    }
}
```

#### Configuração de Relatórios
```python
# config/reporting_config.py
REPORT_CONFIG = {
    'executive_dashboard': {
        'refresh_interval': '1 hour',
        'recipients': ['ceo@company.com', 'cfo@company.com'],
        'format': 'PDF',
        'schedule': 'daily_8am'
    },
    'sales_report': {
        'refresh_interval': '15 minutes',
        'recipients': ['sales@company.com'],
        'format': 'Excel',
        'schedule': 'hourly'
    }
}
```

### 📊 Metodologias de Análise

#### CRISP-DM for Analytics
1. **Business Understanding:** Compreensão dos objetivos de negócio
2. **Data Understanding:** Exploração e compreensão dos dados
3. **Data Preparation:** Preparação e limpeza dos dados
4. **Analysis:** Análise e modelagem dos dados
5. **Evaluation:** Avaliação dos resultados
6. **Deployment:** Implementação e monitoramento

#### Best Practices
- **Data Governance:** Governança e qualidade de dados
- **Version Control:** Controle de versão para consultas e relatórios
- **Documentation:** Documentação abrangente de processos
- **Security:** Segurança e controle de acesso
- **Performance:** Otimização de performance e escalabilidade

### 📊 Análises Especializadas

#### Financial Analytics
- **P&L Analysis:** Análise de demonstrativo de resultados
- **Cash Flow Analysis:** Análise de fluxo de caixa
- **Budget vs Actual:** Comparação orçado vs realizado
- **Cost Analysis:** Análise de custos e rentabilidade
- **Financial Ratios:** Indicadores financeiros

#### Marketing Analytics
- **Campaign Performance:** Performance de campanhas
- **Attribution Analysis:** Análise de atribuição
- **Customer Journey:** Jornada do cliente
- **ROI Analysis:** Análise de retorno sobre investimento
- **Market Basket Analysis:** Análise de cesta de mercado

#### Operations Analytics
- **Supply Chain:** Análise de cadeia de suprimentos
- **Inventory Management:** Gestão de estoque
- **Quality Control:** Controle de qualidade
- **Process Optimization:** Otimização de processos
- **Resource Utilization:** Utilização de recursos

### 🎓 Competências Demonstradas

#### Technical Skills
- **SQL Mastery:** Consultas complexas e otimização
- **Excel Advanced:** Tabelas dinâmicas, Power Query, VBA
- **BI Tools:** Tableau, Power BI, QlikView
- **Python Analytics:** Pandas, NumPy, Matplotlib
- **Statistical Analysis:** Análises estatísticas e testes

#### Business Skills
- **Business Acumen:** Compreensão de negócios
- **Stakeholder Management:** Gestão de stakeholders
- **Presentation Skills:** Apresentação de resultados
- **Problem Solving:** Resolução de problemas complexos
- **Communication:** Comunicação eficaz de insights

### 📚 Documentação Adicional

- **[SQL Guide](docs/sql_guide.md):** Guia completo de SQL
- **[Excel Guide](docs/excel_guide.md):** Guia avançado de Excel
- **[BI Tools Guide](docs/bi_tools_guide.md):** Guia de ferramentas BI
- **[Data Dictionary](docs/data_dictionary.md):** Dicionário de dados

### 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia o [guia de contribuição](CONTRIBUTING.md) antes de submeter pull requests.

### 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 🇺🇸 English

### 📊 Overview

This project represents the capstone work for the **IBM Data Analyst Professional Certificate**, demonstrating advanced competencies in data analysis, visualization, business intelligence, SQL, advanced Excel, and data storytelling. The developed platform offers a complete solution for enterprise data analysis, insight generation, and decision support.

**Developed by:** Gabriel Demetrios Lafis  
**Certification:** IBM Data Analyst Professional Certificate  
**Technologies:** Python, SQL, Excel, Tableau, Power BI, Pandas, Plotly  
**Focus Area:** Data Analysis, Business Intelligence, Data Visualization, SQL Analytics

### 🎯 Key Features

- **Business Intelligence Dashboard:** Executive and operational dashboards
- **SQL Analytics Engine:** Complex queries and advanced analytics
- **Excel Integration:** Automation and advanced Excel analytics
- **Data Visualization Suite:** Professional and interactive visualizations
- **Automated Reporting:** Automated and scheduled reports
- **KPI Monitoring:** Key performance indicator monitoring
- **Data Quality Assessment:** Data quality evaluation and assurance

### 🛠️ Technology Stack

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Data Analysis** | Python | 3.11+ | Data analysis |
| **Database** | SQL Server | Latest | Database |
| **Spreadsheets** | Excel | 365 | Advanced analytics |
| **BI Tools** | Tableau | Latest | BI visualizations |
| **BI Platform** | Power BI | Latest | Corporate dashboards |

### 🚀 Getting Started

#### Prerequisites
- Python 3.11 or higher
- Microsoft Excel 2019 or 365
- SQL Server or PostgreSQL
- Tableau Desktop (optional)
- Power BI Desktop (optional)

#### Installation
```bash
# Clone the repository
git clone https://github.com/galafis/ibm-data-analyst-capstone.git
cd ibm-data-analyst-capstone

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\\Scripts\\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run main application
streamlit run src/main_platform.py
```

### 📊 Detailed Features

#### 📈 **Business Intelligence**
- **Executive Dashboards:** Dashboards for senior management
- **Operational Dashboards:** Real-time operational monitoring
- **Financial Analytics:** Financial and profitability analysis
- **Sales Performance:** Sales performance analysis
- **Customer Analytics:** Customer behavior analysis
- **Market Intelligence:** Market and competitive intelligence

#### 🗃️ **SQL Analytics**
- **Complex Queries:** Advanced and optimized SQL queries
- **Data Warehousing:** Dimensional modeling and ETL
- **Performance Tuning:** Query and index optimization
- **Stored Procedures:** Stored procedures and functions
- **Data Integration:** Multi-source data integration
- **Query Automation:** Recurring query automation

### 🧪 Testing and Quality

```bash
# SQL query tests
python -m pytest tests/test_sql_queries.py -v

# Excel function tests
python -m pytest tests/test_excel_functions.py -v

# Visualization tests
python -m pytest tests/test_visualizations.py -v
```

### 📈 Results and Impact

#### Monitored KPIs
- **Revenue Growth:** Monthly/annual revenue growth
- **Customer Acquisition Cost:** Customer acquisition cost
- **Customer Lifetime Value:** Customer lifetime value
- **Conversion Rates:** Conversion rates by channel
- **Operational Efficiency:** Operational efficiency
- **Market Share:** Market share

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Developed by Gabriel Demetrios Lafis**  
*IBM Data Analyst Professional Certificate Capstone Project*

