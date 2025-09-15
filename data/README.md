# 📊 Pasta Data - Datasets Locais

## 🎯 Propósito
Esta pasta é destinada ao armazenamento de datasets locais utilizados no projeto IBM Data Analyst Professional Certificate Capstone. Aqui você encontrará todos os arquivos de dados necessários para executar análises, criar visualizações e gerar relatórios.

## 📁 Estrutura de Arquivos

### Tipos de Datasets Suportados
- **CSV Files** (`.csv`): Dados tabulares principais
- **Excel Files** (`.xlsx`, `.xls`): Planilhas com múltiplas abas
- **JSON Files** (`.json`): Dados estruturados em formato JSON
- **SQL Files** (`.sql`): Scripts de consulta e criação de dados

### Organização Recomendada
```
data/
├── raw/                    # Dados brutos originais
│   ├── sales_data.csv      # Dados de vendas
│   ├── customer_data.xlsx  # Informações de clientes  
│   └── products.json       # Catálogo de produtos
├── processed/              # Dados processados/limpos
│   ├── clean_sales.csv     # Vendas após limpeza
│   └── aggregated_data.csv # Dados agregados
├── external/               # Dados de fontes externas
│   ├── market_data.csv     # Dados de mercado
│   └── economic_indicators.json
└── samples/                # Datasets de exemplo/teste
    ├── sample_sales.csv    # Amostra para desenvolvimento
    └── test_data.json      # Dados para testes
```

## 🔍 Datasets Principais

### 1. Sales Data (sales_data.csv)
- **Descrição**: Dados históricos de vendas da empresa
- **Colunas**: date, product_id, customer_id, quantity, unit_price, total_amount, region
- **Período**: Janeiro 2023 - Atual
- **Uso**: Análise de performance de vendas, trends e forecasting

### 2. Customer Data (customer_data.xlsx)
- **Descrição**: Informações completas dos clientes
- **Abas**: 
  - `customers`: Dados pessoais e demográficos
  - `segments`: Segmentação de clientes
  - `interactions`: Histórico de interações
- **Uso**: Customer analytics, segmentação, análise de churn

### 3. Product Catalog (products.json)
- **Descrição**: Catálogo completo de produtos
- **Estrutura**: ID, nome, categoria, preço, custo, margem
- **Uso**: Análise de rentabilidade, performance por produto

### 4. Market Data (market_data.csv)
- **Descrição**: Dados externos de mercado e competidores
- **Fonte**: APIs externas e relatórios de mercado
- **Uso**: Análise competitiva, benchmarking

## 📈 Como Usar os Datasets

### 1. Carregamento em Python
```python
import pandas as pd
import json

# Carregar CSV
sales_df = pd.read_csv('data/raw/sales_data.csv')

# Carregar Excel (múltiplas abas)
customer_sheets = pd.read_excel('data/raw/customer_data.xlsx', sheet_name=None)
customers_df = customer_sheets['customers']

# Carregar JSON
with open('data/raw/products.json', 'r') as f:
    products_data = json.load(f)
```

### 2. Carregamento em SQL
```sql
-- Importar CSV para PostgreSQL
COPY sales_data FROM 'data/raw/sales_data.csv' 
WITH (FORMAT CSV, HEADER TRUE);

-- Criar tabela temporária
CREATE TEMP TABLE temp_sales AS 
SELECT * FROM sales_data WHERE date >= '2024-01-01';
```

### 3. Carregamento no Excel
- Use **Data > Get Data > From File** para importar CSVs
- Para dados JSON, use **Power Query** para transformação
- Configure **Power Pivot** para análises avançadas

## 🛠️ Ferramentas de Análise

### Python Libraries
- **pandas**: Manipulação e análise de dados
- **numpy**: Operações numéricas
- **matplotlib/seaborn**: Visualizações
- **plotly**: Gráficos interativos
- **scikit-learn**: Machine learning

### SQL Tools
- **PostgreSQL**: Banco principal
- **DBeaver**: Interface gráfica
- **pgAdmin**: Administração PostgreSQL

### BI Tools
- **Tableau**: Visualizações profissionais
- **Power BI**: Dashboards corporativos
- **Excel**: Análises rápidas e pivot tables

## 📋 Qualidade dos Dados

### Validações Implementadas
- ✅ Verificação de valores nulos
- ✅ Validação de tipos de dados
- ✅ Checks de integridade referencial
- ✅ Detecção de outliers
- ✅ Validação de formatos de data

### Scripts de Limpeza
```python
# Exemplo de limpeza básica
from src.utils.data_quality import DataQualityChecker

checker = DataQualityChecker()
quality_report = checker.validate_dataset(
    data=sales_df,
    rules=['no_nulls', 'valid_dates', 'positive_amounts']
)
```

## 🔄 ETL Process

### Extração (Extract)
- APIs externas para dados de mercado
- Exportações de CRM/ERP
- Web scraping (quando autorizado)

### Transformação (Transform)
- Limpeza e padronização
- Cálculo de métricas derivadas
- Agregações e sumarizações
- Joins entre diferentes fontes

### Carregamento (Load)
- PostgreSQL para dados estruturados
- Data warehouse para análises históricas
- Cache em CSV/Parquet para performance

## 📊 KPIs e Métricas Calculadas

### Métricas de Vendas
- **Revenue Growth**: Taxa de crescimento de receita
- **Average Order Value (AOV)**: Valor médio do pedido
- **Units per Transaction**: Unidades por transação

### Métricas de Cliente
- **Customer Acquisition Cost (CAC)**: Custo de aquisição
- **Customer Lifetime Value (CLV)**: Valor do ciclo de vida
- **Churn Rate**: Taxa de cancelamento

### Métricas Operacionais
- **Inventory Turnover**: Giro de estoque
- **Profit Margin**: Margem de lucro por produto
- **Regional Performance**: Performance por região

## 🔒 Segurança e Privacidade

### Dados Sensíveis
- ⚠️ **Nunca commitar** dados reais de clientes
- 🔐 Use **dados anonimizados** para desenvolvimento
- 📝 **GDPR Compliance**: Remover PII quando necessário

### Backup e Versionamento
- 💾 **Backup diário** dos dados críticos
- 📊 **Versionamento** de datasets importantes
- 🔄 **Histórico** de transformações aplicadas

## 🚀 Getting Started

1. **Clone o repositório**
2. **Instale as dependências**: `pip install -r requirements.txt`
3. **Configure as conexões** de banco em `config/database.py`
4. **Execute a validação** dos dados: `python src/utils/data_quality.py`
5. **Inicie a análise** com os notebooks em `notebooks/`

## 📞 Suporte

Para questões sobre os datasets ou processo de análise:
- 📧 **Email**: gabrieldemetrios@gmail.com
- 🐛 **Issues**: Use o GitHub Issues para reportar problemas
- 📖 **Documentação**: Veja `/docs` para guias detalhados

---
*Última atualização: Setembro 2025*
*Versão: 1.0.0*
